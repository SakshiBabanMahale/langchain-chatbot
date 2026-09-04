from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


SYSTEM_PROMPT = """
You are a helpful and friendly AI assistant.

Your responsibilities:
- Answer the user's questions clearly and accurately.
- Maintain context from previous messages in the conversation.
- Give concise but useful explanations.
- If you are unsure about something, say so instead of making up information.
- Be polite and professional.
"""


def create_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])