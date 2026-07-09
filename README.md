# LLM Orchestrator Framework

A lightweight Python framework for building LLM-powered applications with automatic tool calling.

This project was built from scratch to understand how modern LLM orchestration works without relying on frameworks such as LangChain or LlamaIndex.

---

## Features

* Automatic tool registration
* Tool metadata extraction using Python introspection
* Conversion of internal tool definitions to LLM-compatible schemas
* Automatic tool execution
* Conversation history management
* Support for multiple tool calls in a single LLM response
* Separation between internal tool representation and LLM-facing schema

---

## Project Structure

```text
.
├── orchestrator.py      # Core orchestration logic
├── tool_registry.py     # Tool registration and execution
├── main.py                       
├── llm_client.py        # LLM communication layer
├── tools/
│   ├── tool.py          # Internal tool representation
│   └── calculator.py
│   └── llm_tool.py      # LLM-compatible tool DTO
│   └── ...
└── config/
    └── app_config.py
│   └── logging_config.py
```

---

## Architecture

```text
                +----------------------+
                |      User Input      |
                +----------+-----------+
                           |
                           v
                  +--------+--------+
                  |  Orchestrator   |
                  +--------+--------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
     LLM Client                 Tool Registry
             |                           |
             |                   Registered Tools
             |                           |
             +-------------+-------------+
                           |
                    Tool Execution
                           |
                           v
                     Final Response
```

---

## Workflow

1. User submits a prompt.
2. The Orchestrator sends the conversation and available tools to the LLM.
3. The LLM either:

   * responds directly, or
   * requests one or more tool calls.
4. The Registry executes the requested tools.
5. Tool results are added to the conversation.
6. The updated conversation is sent back to the LLM.
7. The LLM generates the final response.

---

## Tool Registration

Tools are registered once and become automatically available to the LLM.

Example:

```python
registry.register(multiply)
registry.register(add)
```

The Registry is responsible for:

* storing tool definitions
* exposing LLM tool schemas
* executing requested tools

---

## Internal Tool Model

Each registered function is converted into an internal `Tool` object containing:

* name
* description
* parameter types
* return type
* function reference

This representation is never exposed directly to the LLM.

---

## LLM Tool Model

The internal `Tool` is transformed into an LLM-compatible schema.

Example:

```json
{
  "type": "function",
  "function": {
    "name": "multiply",
    "description": "Multiply two integers",
    "parameters": {
      "type": "object",
      "properties": {
        "a": {
          "type": "integer"
        },
        "b": {
          "type": "integer"
        }
      },
      "required": [
        "a",
        "b"
      ]
    }
  }
}
```

---

## Conversation Flow

Example conversation:

```text
User
↓
Assistant (Tool Call)
↓
Tool Result
↓
Assistant (Final Answer)
```

Conversation history is maintained as standard chat messages.

---

## Current Capabilities

* Automatic tool discovery
* Automatic schema generation
* Automatic tool execution
* Recursive tool-calling loop
* Multiple tool call execution
* Conversation history preservation
* Framework independent of application logic

---

## Planned Improvements

* Conversation object instead of raw message list
* Error handling for failed tool execution
* Unknown tool handling
* Provider abstraction (Groq, OpenAI, Ollama, etc.)
* Streaming responses
* Structured JSON output
* Token usage tracking
* Context window management
* RAG integration as a tool
* Plugin-based tool loading

---

## Purpose

This project is intended as a learning framework to understand the internals of LLM applications rather than relying on high-level abstractions.

The goal is to understand how modern AI frameworks perform:

* tool registration
* schema generation
* tool execution
* conversation orchestration
* recursive LLM interactions

before moving to production frameworks such as LangChain or LlamaIndex.
