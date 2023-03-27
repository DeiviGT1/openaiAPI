import openai

openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = "Hello, how are you?"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
)

response = completion.choices[0].text
print(response)