import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_text(text: str, target_language: str) -> str:
    prompt = f"Translate the following English text to {target_language}:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a translation engine that translates English to {target_language}."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
