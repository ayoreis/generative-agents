from openai import Completion

MODEL = "gpt-3.5-turbo"


# TODO handle API errors
def complete(prompt: str, max_tokens: int | None = None) -> str:
    """`max_tokens` is tokens after prompt"""

    completion = Completion.create(model=MODEL, prompt=prompt, max_tokens=max_tokens)

    return completion.choices[0].text
