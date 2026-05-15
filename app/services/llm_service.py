import os

from dotenv import load_dotenv

import google.generativeai as genai


load_dotenv()


genai.configure(

    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(

    "gemini-1.5-flash"
)


def generate_ai_response(

    query,

    recommendations
):

    try:

        formatted_assessments = ""


        for item in recommendations:

            formatted_assessments += f"""

            Assessment:
            {item['name']}

            URL:
            {item['url']}

            """


        prompt = f"""

        You are an SHL assessment recommendation assistant.

        User hiring requirement:
        {query}

        Recommended assessments:
        {formatted_assessments}

        Explain:
        - why these assessments fit
        - what skills they evaluate
        - keep response concise and professional
        """


        response = model.generate_content(

            prompt
        )


        return response.text


    except Exception as e:

        print("Gemini Error:")

        print(e)

        return "I found relevant SHL assessments based on your hiring requirements."