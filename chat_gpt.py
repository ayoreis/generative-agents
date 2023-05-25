from typing import NamedTuple, Literal, Optional, List
from openai import ChatCompletion

class Message(NamedTuple):
    role: Literal['user', 'assitant']
    content: str

class ChatGPT:
    MODEL = 'gpt-3.5-turbo'

    def __init__(self):
        self.messages: List[Message] = []

    def message(self, content: str) -> str:
        self.messages.append(Message('user', content))

        completion = ChatCompletion.create(
            model=self.MODEL,
            messages=self.messages,
        )

        (role, content) = completion.choises[0].message

        self.messages.append(Message(role, content))

        return content
