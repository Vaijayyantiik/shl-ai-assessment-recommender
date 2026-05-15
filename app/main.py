from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.models.schemas import (
    ChatRequest
)

from app.services.recommendation_service import (
    recommend_assessments
)

from app.services.llm_service import (
    generate_ai_response
)

from app.database.db import (
    engine,
    Base,
    SessionLocal
)

from app.database.models import (
    ChatHistory,
    Recommendation
)


app = FastAPI()


Base.metadata.create_all(
    bind=engine
)


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.get("/")
def home():

    return {
        "message": "SHL Conversational Assessment Recommender API"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    messages = request.messages

    latest_message = messages[-1].content


    vague_keywords = [

        "assessment",

        "assessments",

        "assement",

        "assements",

        "test",

        "tests",

        "hiring",

        "developer",

        "job",

        "role"
    ]


    user_query = latest_message.lower().strip()


    is_vague = (

        len(user_query.split()) <= 2

        or user_query in vague_keywords
    )


    if is_vague:

        return {

            "reply": "Could you specify the skills, experience level, or role you are hiring for? Example: Python developer, leadership role, finance manager, communication skills.",

            "recommendations": [],

            "end_of_conversation": False
        }


    recommendations = recommend_assessments(

        latest_message
    )


    reply_message = generate_ai_response(

        latest_message,

        recommendations
    )


    db = SessionLocal()


    chat_entry = ChatHistory(

        user_message=latest_message,

        bot_reply=reply_message
    )

    db.add(chat_entry)


    for item in recommendations:

        recommendation_entry = Recommendation(

            assessment_name=item["name"],

            assessment_url=item["url"],

            test_type=item["test_type"]
        )

        db.add(recommendation_entry)


    db.commit()

    db.close()


    return {

        "reply": reply_message,

        "recommendations": recommendations,

        "end_of_conversation": True
    }