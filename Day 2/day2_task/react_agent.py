import json

from config import client, MODEL
from tools import TOOL_FUNCTIONS


QUESTION = (
    "I have Rs. 1,200. "
    "Which two books can I buy together within my budget? "
    "The available books are exactly Python Basics, "
    "Data Structures, and Machine Learning."
)


def run_react_agent(question):

    print("=== ReAct Agent ===")

    print("Question:")
    print(question)

    # Available books in our scenario
    book_names = [
        "Python Basics",
        "Data Structures",
        "Machine Learning"
    ]

    observations = []

    # ReAct: Action -> Observation

    for book_name in book_names:

        arguments = {
            "book_name": book_name
        }

        print(
            f"\n[Action] get_book_price({arguments})"
        )

        function = TOOL_FUNCTIONS["get_book_price"]

        result = function(**arguments)

        print(
            f"[Observation] {result}"
        )

        observations.append(
            {
                "book_name": book_name,
                "price": result
            }
        )

    # Send tool observations to the LLM

    observation_text = json.dumps(
        observations
    )

    messages = [

        {
            "role": "system",
            "content": (
                "You are a ReAct-style agent. "
                "Use only the tool observations provided. "
                "Do not invent book names or prices. "
                "Compare all possible pairs of the three books. "
                "The budget is Rs. 1,200. "
                "Identify every pair that fits within the budget "
                "and mention the pair that exceeds the budget. "
                "Give a concise final answer. "
                "Do not reveal private chain-of-thought."
            )
        },

        {
            "role": "user",
            "content": (
                question
                + "\n\nTool observations:\n"
                + observation_text
            )
        }

    ]

    response = client.chat.completions.create(

        model=MODEL,

        messages=messages,

        temperature=0
    )

    return response.choices[0].message.content


answer = run_react_agent(
    QUESTION
)


print("\nFinal Answer:")

print(answer)