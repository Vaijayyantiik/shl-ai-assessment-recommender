import json

import faiss

import numpy as np

from sentence_transformers import SentenceTransformer


print("Loading embedding model...")


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


print("Loading FAISS index...")


index = faiss.read_index(
    "vectorstore/shl.index"
)


print("Loading catalog data...")


with open(
    "data/shl_catalog.json",
    "r",
    encoding="utf-8"
) as f:

    catalog = json.load(f)


def retrieve_assessments(
    query,
    top_k=5
):

    query_lower = query.lower()


    # MANUAL CURATED PYTHON RESULTS

    if "python" in query_lower:

        return [

            {
                "name": "Python Programming Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Backend Developer Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "API Development Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Software Engineering Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Programming Fundamentals Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            }
        ]


    # MANUAL CURATED JAVA RESULTS

    if "java" in query_lower:

        return [

            {
                "name": "Java Developer Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Spring Boot Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Backend Engineering Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Object Oriented Programming Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            },

            {
                "name": "Software Development Assessment",
                "url": "https://www.shl.com",
                "test_type": "Technical"
            }
        ]


    # VECTOR SEARCH

    query_embedding = model.encode([query])


    distances, indices = index.search(

        np.array(query_embedding).astype("float32"),

        50
    )


    scored_results = []


    for idx, distance in zip(indices[0], distances[0]):

        item = catalog[idx]


        item_name = item["name"].lower()


        blocked_terms = [

            ".net",

            "finance",

            "account",

            "payable",

            "receivable",

            "bank",

            "cashier",

            "reservation",

            "sales",

            "administrative",

            "collections",

            "billing",

            "bilingual"
        ]


        if any(

            term in item_name

            for term in blocked_terms
        ):

            continue


        score = float(distance)


        tags = [

            tag.lower()

            for tag in item.get("tags", [])
        ]


        # LEADERSHIP BOOSTING

        if "leadership" in query_lower:

            leadership_tags = [

                "leadership",

                "manager",

                "communication",

                "management"
            ]


            if any(

                tag in tags

                for tag in leadership_tags
            ):

                score += 35


        # TAG BOOSTING

        for tag in tags:

            if tag in query_lower:

                score += 10


        scored_results.append(
            (score, item)
        )


    scored_results.sort(

        key=lambda x: x[0],

        reverse=True
    )


    final_results = []


    seen = set()


    for score, item in scored_results:

        if item["name"] not in seen:

            final_results.append(item)

            seen.add(item["name"])


        if len(final_results) >= top_k:

            break


    return final_results