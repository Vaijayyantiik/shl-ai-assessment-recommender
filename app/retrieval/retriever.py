from sentence_transformers import SentenceTransformer

import faiss

import pickle

import numpy as np


print("Loading embedding model...")


model = SentenceTransformer(

    "all-MiniLM-L6-v2"
)


print("Loading FAISS index...")


index = faiss.read_index(

    "vectorstore/shl.index"
)


print("Loading catalog data...")


with open(

    "vectorstore/catalog.pkl",

    "rb"

) as f:

    catalog = pickle.load(f)


TECH_KEYWORDS = {

    "python": [

        "python",

        "programming",

        "developer",

        "coding",

        "software",

        "backend"
    ],

    "java": [

        "java",

        "developer",

        "programming",

        "software",

        "backend"
    ],

    "leadership": [

        "manager",

        "leadership",

        "supervisor",

        "communication",

        "teamwork"
    ],

    "communication": [

        "communication",

        "interpersonal",

        "customer-service",

        "manager",

        "client"
    ],

    "finance": [

        "finance",

        "accounting",

        "bookkeeping",

        "auditing",

        "banking"
    ]
}


def keyword_score(query, text):

    score = 0

    query = query.lower()

    text = text.lower()


    for category in TECH_KEYWORDS:

        if category in query:

            for keyword in TECH_KEYWORDS[category]:

                if keyword in text:

                    score += 3


    for word in query.split():

        if word in text:

            score += 1


    return score


def retrieve_assessments(

    query,

    top_k=5
):

    query_embedding = model.encode(

        [query]
    )

    distances, indices = index.search(

        np.array(query_embedding),

        20
    )

    scored_results = []


    for idx in indices[0]:

        item = catalog[idx]

        combined_text = f"""

        {item.get('name', '')}

        {item.get('description', '')}

        {' '.join(item.get('tags', []))}

        """

        semantic_score = 1

        keyword_boost = keyword_score(

            query,

            combined_text
        )

        tag_boost = 0

        query_words = query.lower().split()

        for tag in item.get("tags", []):

            if tag.lower() in query_words:

                tag_boost += 5


        total_score = semantic_score + keyword_boost + tag_boost

        scored_results.append(

            (

                total_score,

                item
            )
        )


    scored_results.sort(

        reverse=True,

        key=lambda x: x[0]
    )


    final_results = []

    seen = set()


    for score, item in scored_results:

        if item["url"] not in seen:

            seen.add(item["url"])

            final_results.append(item)

        if len(final_results) == top_k:

            break


    return final_results


if __name__ == "__main__":

    query = "Python backend engineer"

    results = retrieve_assessments(query)

    print("\nResults:\n")

    for item in results:

        print(item)