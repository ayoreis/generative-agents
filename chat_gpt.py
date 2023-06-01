from typing import TypedDict, Literal, List
from openai import ChatCompletion

class Message(TypedDict):
    role: Literal['user', 'assistant']
    content: str

class ChatGPT:
    MODEL = 'gpt-3.5-turbo'

    def __init__(self):
        self.messages: List[Message] = []

    def message(self, content: str) -> str:
        self.messages.append({ 'role': 'user', 'content': content })

        completion = ChatCompletion.create(
            model=self.MODEL,
            messages=self.messages,
        )

        message = completion.choices[0].message

        role = message.role
        content = message.content

        self.messages.append({ 'role': role, 'content': content })

        return content
