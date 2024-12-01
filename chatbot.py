# Simple chatbot implementation

def chatbot():
    print("Hello! I'm your chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hello', 'hi', 'hey']:
            print("Bot: Hello! How can I assist you today?")
        
        elif user_input == 'how are you':
            print("Bot: I'm just a chatbot, but I'm doing well, thank you!")
        
        elif user_input == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        
        elif 'your name' in user_input:
            print("Bot: I'm Chatbot. What's your name?")
        
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Bot: You're welcome!")
        
        elif 'help' in user_input:
            print("Bot: Sure! How can I assist you? You can ask me things like 'how are you' or 'what's your name'.")
        
        else:
            print("Bot: Sorry, I didn't quite understand that. Can you ask something else?")
        

# Start the chatbot conversation
chatbot()
