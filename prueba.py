import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

#create a function to reply
def reply(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    return response.choices[0].text

print(reply("Human: Hello, how are you doing today?\nAI:"))