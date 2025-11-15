#!/usr/bin/env python3
# Examples: https://python.useinstructor.com/examples/
# instructor workflow: https://python.useinstructor.com/concepts/#typical-workflow
# it helps to retry request to LLMs incase verifcation fails against validators.

from pydantic import BaseModel, Field
import instructor
from typing import Literal, List 
import openai
from openai import OpenAI

client = instructor.from_openai(OpenAI())

# https://python.useinstructor.com/examples/single_classification/
class ClassificationResponse(BaseModel):
    """A few-shot example of text classification"""
    label: Literal["SPAM", "NOT_SPAM"] = Field(description="the predicted class label")

def classify(data) -> ClassificationResponse:
    return client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=ClassificationResponse,
        messages=[
            {
                "role": "user",
                "content": f"classify the following text: <text>{data}</text>",
            },
        ]
    )

def classify_spam():
    # K shot learning
    # in-context learning
    # https://www.promptingguide.ai/techniques/fewshot
    for text, target in [
        ("Hey Karthikeyan! You're awesome", "NOT_SPAM"),
        ("I am a nigerian prince and I need your help.", "SPAM")
    ]:
        predict = classify(text)
        assert predict.label == target
        print(f"predict: {predict}")
    

# https://python.useinstructor.com/examples/multiple_classification/
LABELS = Literal["ACCOUNT", "BILLING", "GENERAL_QUERY"]

class MultiClassPrediction(BaseModel):
    lables: List[LABELS] = Field(description="select the labels that apply to the support ticket")

def multi_classify(data) -> MultiClassPrediction:
    return client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=MultiClassPrediction,
        messages=[
            {
                "role": "system",
                "content": "You are a support agent at a tech company. Only select the labels that apply to the support ticket",
            },
            {
                "role": "user",
                "content": f"Classify the following support ticket: <text>{data}</text>",
            },
        ],
    )

def classify_support_tickets():
    tickets = ["my account is locked and I can't access my billing info",
               "I need help with my subscription",
               "How do I change my payment method?",
               "Can you tell me the status of my order?",
               "I have a question about the account features",
               ]
    for ticket in tickets:
        prediction = multi_classify(ticket)
        print(f">prediction: {prediction}")


# https://python.useinstructor.com/examples/bulk_classification/
_async_client = instructor.from_openai(
        openai.AsyncOpenAI(),
)


async def tag_request(request: TagRequest) -> TagResponse:
    predictions = await asyncio.gather(
            *[tag_single_request(text, request.tags) for text in request.texts]
    )
    # TODO



# classify_support_tickets()





