import openai
import os
import azure.functions as func
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        posts = req_body.get("posts")
        topic = req_body.get("topic")

        examples = "\n".join(f"- {p}" for p in posts)
        prompt = f"Here are some past social media posts:\n{examples}\n\nWrite a new post about '{topic}' in a similar style."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=100
        )

        return func.HttpResponse(response.choices[0].text.strip(), status_code=200)

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
