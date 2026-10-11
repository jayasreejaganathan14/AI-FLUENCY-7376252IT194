# Day 1 AI Fluency Training Task

## Scenario

The user asks:

"I can pay Rs. 30,000. Which two courses can I take together?"

Course prices are stored privately in `expenses.txt`.

## 1. Plain Chatbot

The plain chatbot uses an LLM without access to the private course-price data.

It cannot determine the actual course combinations from `expenses.txt`.

File:

`chatbot.py`

## 2. Rule-Based Workflow

The rule-based workflow reads the private course data and uses predefined programming rules to check every pair of courses.

File:

`workflow.py`

## 3. AI Agent

The AI agent uses:

- an LLM
- private course data
- tools
- an agent loop

The agent can use tools to read the course data and find combinations within the user's budget.

File:

`agent.py`

## Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Uses LLM | Yes | No | Yes |
| Uses private data | No | Yes | Yes |
| Uses tools | No | No | Yes |
| Uses loop | No | Fixed programming loop | Agent loop |
| Flexible | Yes | Limited | Yes |
| Handles fixed rules | No | Yes | Yes |

## Files

- `chatbot.py` - Plain chatbot
- `workflow.py` - Rule-based workflow
- `agent.py` - AI agent
- `expenses.txt` - Private course-price data
- `analysis.md` - Detailed analysis
- `Output/` - Screenshots

## How to Run

Activate the virtual environment and run:

```bash
python chatbot.py
python workflow.py
python agent.py