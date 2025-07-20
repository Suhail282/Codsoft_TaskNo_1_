def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I help you today?")
        
        elif "your name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot.")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning well!")
        
        elif "help" in user_input:
            print("Chatbot: Sure! You can ask me about my name, how I am, or just say hello.")
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print("Chatbot: The current time is", now.strftime("%H:%M:%S"))
        
        elif user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
chatbot()
#sucessfully chatbot created!!!
