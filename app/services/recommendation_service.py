from app.retrieval.retriever import (
    retrieve_assessments
)


def recommend_assessments(query):

    results = retrieve_assessments(

        query,

        top_k=5
    )

    recommendations = []

    for item in results:

        recommendations.append({

            "name": item["name"],

            "url": item["url"],

            "test_type": "K"
        })

    return recommendations