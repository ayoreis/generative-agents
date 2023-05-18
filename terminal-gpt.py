from typing import List, Dict, Literal
import os
import openai

import openai_api

BOLD = '\033[1m'
WHITE = '\033[37m'
END = '\033[0m'

messages: List[Dict[Literal['user', 'assistant'], str]] = []

print(f'\n{BOLD}TERMINAL-GPT{END}\n')

while True:
    question = input(f'{BOLD}{WHITE}You:{END} ')

    completion = openai.ChatCompletion.create(
        model = 'gpt-4',

        messages = [
            *messages,

            {
                'role': 'user',
                'content': question
            }
        ]
    )

    model = completion.model
    message = completion.choices[0].message
    answer = message.content

    messages.append(message)

    print(f'{BOLD}{WHITE}AI {END}{BOLD}({model}){WHITE}:{END} {answer}')
