#!/usr/bin/env python3
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
  model="gpt-4o-mini",
  input="Write a short long novel about otters in space.",
  background=True,
)

print(resp.status)
