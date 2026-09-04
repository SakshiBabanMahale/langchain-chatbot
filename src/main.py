from chatbot import chatbot


def main():
    print("=================================")
    print("      LangChain AI Chatbot")
    print("=================================")
    print("Type 'exit' to end the conversation.\n")

    session_id = "default"

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        if not user_input.strip():
            print("Chatbot: Please enter a message.\n")
            continue

        try:
            response = chatbot.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )

            print(f"Bot: {response.text}\n")

        except Exception as error:
            print(f"Error: {error}\n")


if __name__ == "__main__":
    main()