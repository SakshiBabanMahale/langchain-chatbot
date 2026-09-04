# LangChain AI Chatbot

This project is a simple conversational AI chatbot built using Python, LangChain, and Google Gemini. The main purpose of the project is to understand how an LLM can be connected with LangChain and how conversation memory can be used to make the chatbot remember previous messages.

The chatbot runs through the command line and supports normal multi-turn conversations.

## Features

- Conversational AI using Google Gemini
- Built using LangChain
- Supports multi-turn conversations
- Remembers previous messages during a session
- Uses a system prompt to control chatbot behavior
- API key is stored securely using environment variables
- Basic error handling
- Simple command-line interface
- Modular Python project structure

## Technologies Used

- Python
- LangChain
- Google Gemini
- langchain-google-genai
- python-dotenv
- Git
- GitHub
- VS Code

## System Architecture

The chatbot follows a simple flow:

User
↓
main.py
↓
LangChain Chatbot
↓
System Prompt + Conversation History + User Input
↓
Google Gemini LLM
↓
Generated Response
↓
User

The main LangChain chain works like this:

User Input → Prompt → Gemini Model → Response

Conversation history is added to the prompt before sending the request to the Gemini model.

## Project Structure

```text
LangChain-Chatbot/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── prompts.py
│   ├── chatbot.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md