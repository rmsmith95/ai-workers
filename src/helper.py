import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']