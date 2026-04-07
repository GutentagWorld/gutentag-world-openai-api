#!/usr/bin/env python3
"""Uses the OpenAI API to produce 'Gutentag, World!'.

Requires: pip install openai
Set env var: OPENAI_API_KEY
"""
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': 'You only ever respond with exactly: Gutentag, World!'},
        {'role': 'user', 'content': 'Say hello.'},
    ],
)

print(response.choices[0].message.content)
