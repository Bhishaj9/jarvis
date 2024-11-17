from openai import OpenAI
# client = OpenAI()
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named  Jarvis akillesd in general tasks like google and alexa"},
        {"role": "user", "content": "what is coding"},
    ]
)

print(completion.choices[0].message)