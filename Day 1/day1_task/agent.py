import json
import os
from openai import OpenAI


# ============================================================
# GROQ CLIENT
# ============================================================

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# ============================================================
# TOOL 1: READ PRIVATE COURSE DATA
# ============================================================

def read_course_data():
    courses = []

    with open("expenses.txt", "r") as file:
        for line in file:
            name, price = line.strip().split(",")

            courses.append({
                "name": name.strip(),
                "price": int(price.strip())
            })

    return courses


# ============================================================
# TOOL 2: FIND COURSE COMBINATIONS
# ============================================================

def find_course_combinations(budget):
    courses = read_course_data()

    combinations = []

    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):

            total = courses[i]["price"] + courses[j]["price"]

            if total <= budget:
                combinations.append({
                    "course1": courses[i]["name"],
                    "course2": courses[j]["name"],
                    "total": total
                })

    return combinations


# ============================================================
# TOOLS GIVEN TO THE LLM
# ============================================================

tools = [
    {
        "type": "function",
        "name": "read_course_data",
        "description": "Read private course and price data from the course data file.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "find_course_combinations",
        "description": "Find every pair of courses that fits within the user's budget.",
        "parameters": {
            "type": "object",
            "properties": {
                "budget": {
                    "type": "number",
                    "description": "Maximum amount the user can spend."
                }
            },
            "required": ["budget"]
        }
    }
]


# ============================================================
# AGENT INSTRUCTIONS
# ============================================================

instructions = """
You are an AI agent.

The user's course prices are private data stored in expenses.txt.

You must use the available tools to access the private data.

Your process is:

1. Understand the user's request.
2. Select an appropriate tool.
3. Use the tool.
4. Observe the tool result.
5. Continue using tools if necessary.
6. Give a final answer.

Never invent course prices.

When answering, clearly list the course combinations that fit
within the user's budget.
"""


# ============================================================
# USER QUESTION
# ============================================================

QUESTION = (
    "I can pay Rs. 30,000. "
    "Which two courses can I take together?"
)


# ============================================================
# AGENT LOOP
# ============================================================

def agent(question):

    # First request to the LLM
    response = client.responses.create(
        model="openai/gpt-oss-20b",
        instructions=instructions,
        input=question,
        tools=tools
    )

    # Agent loop
    while True:

        # Find tool calls requested by the LLM
        tool_calls = [
            item
            for item in response.output
            if item.type == "function_call"
        ]

        # If there are no more tool calls,
        # the agent has finished.
        if not tool_calls:
            return response.output_text

        tool_outputs = []

        # Execute each requested tool
        for call in tool_calls:

            arguments = json.loads(call.arguments)

            # --------------------------------------------
            # TOOL 1
            # --------------------------------------------

            if call.name == "read_course_data":

                result = read_course_data()

            # --------------------------------------------
            # TOOL 2
            # --------------------------------------------

            elif call.name == "find_course_combinations":

                result = find_course_combinations(
                    arguments["budget"]
                )

            # --------------------------------------------
            # UNKNOWN TOOL
            # --------------------------------------------

            else:

                result = {
                    "error": "Unknown tool"
                }

            # Show tool usage in terminal
            print("\n[Agent Tool Used]")
            print(call.name)

            print("[Tool Result]")
            print(result)

            # Prepare result for the next LLM call
            tool_outputs.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": json.dumps(result)
            })

        # ------------------------------------------------
        # SEND TOOL RESULT BACK TO THE LLM
        # ------------------------------------------------

        response = client.responses.create(
            model="openai/gpt-oss-20b",
            instructions=instructions,
            input=[
                {
                    "role": "user",
                    "content": question
                },
                {
                    "role": "user",
                    "content": (
                        "The following are the results returned "
                        "by the tools. Use them to answer the "
                        "original question:\n\n"
                        + json.dumps(tool_outputs)
                    )
                }
            ],
            tools=tools
        )


# ============================================================
# RUN AGENT
# ============================================================

print("Q:", QUESTION)
print("\nAgent:")

result = agent(QUESTION)

print(result)