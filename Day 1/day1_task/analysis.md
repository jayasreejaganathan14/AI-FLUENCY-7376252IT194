# Day 1 Task: Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## Scenario

The chosen scenario is course selection based on a user's private course-price data.

The user asks:

"I can pay Rs. 30,000. Which two courses can I take together?"

The course prices are stored privately in `expenses.txt`.

---

## 1. Plain Chatbot

The plain chatbot uses an LLM to respond to the user's question.

It does not have access to the private course-price file. Therefore, it cannot reliably determine which courses are available within the user's actual budget.

It mainly generates a response using the language model.

The chatbot does not use external tools, predefined business rules, or a tool-use loop.

Its main limitation in this scenario is private-data access.

---

## 2. Rule-Based Workflow

The rule-based workflow does not use an LLM.

It reads the private course-price file and follows predefined programming rules.

The workflow checks every possible pair of courses, calculates the total price, and checks whether the total is less than or equal to Rs. 30,000.

The process is fixed and deterministic.

Its limitation is flexibility. If the user's request changes significantly, new rules may need to be manually programmed.

---

## 3. AI Agent

The AI agent combines an LLM, tools, and a loop.

The agent first understands the user's request.

It can then select and use tools to access the private course data and calculate suitable course combinations.

The tool result is returned to the agent. The agent observes the result and continues the process until it can provide a final answer.

This demonstrates the LLM + Tools + Loop concept.

The agent is more flexible than the fixed workflow because the LLM can determine which tool is appropriate for the task.

---

## 4. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for conversation | Low because rules are fixed | High |
| Decision-making | LLM-generated response | Predefined conditions | LLM-based tool selection |
| Tool usage | None | Direct program logic | Uses tools |
| Private-data access | No | Yes | Yes through tools |
| Multi-step task handling | Limited | Fixed steps | Dynamic multi-step loop |
| Automation | Limited | High for fixed tasks | High |
| Reliability | May lack private data | Predictable for defined rules | Depends on tools and agent reasoning |

---

## 5. Suitability Analysis

For this scenario, the three approaches behave differently.

The plain chatbot is useful for general conversational questions but cannot directly access the private course-price data.

The rule-based workflow can access the private data and reliably calculate course combinations. However, its process is fixed and requires predefined rules.

The AI agent can use tools to access private data and can perform multiple steps using an agent loop. This makes it suitable when the task requires flexible decisions and tool usage.

The appropriate approach therefore depends on whether the task is simple conversation, a fixed predictable process, or a flexible multi-step task involving tools.

---

## 6. Conclusion

A plain chatbot is appropriate when a user mainly needs natural-language responses and no private-data access or external actions are required.

A rule-based workflow is appropriate when the process is predictable and can be completely described using predefined rules and conditions.

An AI agent is appropriate when a task requires an LLM to reason about the request, select and use tools, observe results, and continue through multiple steps.

The main difference is that a chatbot mainly generates responses, a workflow follows predefined rules, and an agent combines an LLM with tools and a loop to complete a task.