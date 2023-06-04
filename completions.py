from openai import Completion

MODEL = "gpt-3.5-turbo"


def complete(prompt: str):
    completion = Completion.create(
        model=MODEL,
        prompt=prompt,
    )

    return completion.choices[0].text
