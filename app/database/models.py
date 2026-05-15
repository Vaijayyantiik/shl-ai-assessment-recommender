from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import Text


from app.database.db import Base


class ChatHistory(Base):

    __tablename__ = "chat_history"


    id = Column(

        Integer,

        primary_key=True,

        index=True
    )

    user_message = Column(

        Text
    )

    bot_reply = Column(

        Text
    )


class Recommendation(Base):

    __tablename__ = "recommendations"


    id = Column(

        Integer,

        primary_key=True,

        index=True
    )

    assessment_name = Column(

        String
    )

    assessment_url = Column(

        String
    )

    test_type = Column(

        String
    )