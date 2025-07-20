# Codsoft_TaskNo_1_
Artificial Intelligence task_no_1
Simple Rule-Based Chatbot
This is a **basic chatbot** implemented in Python using `if-else` statements. It responds to user inputs based on predefined rules. This project is ideal for beginners to understand how natural language processing and conversation flow work at a basic level.
Features
- Responds to common greetings like "hi", "hello", "hey"
- Can tell you its name
- Responds to "how are you"
- Provides current system time
- Handles basic help queries
- Ends the conversation with "bye", "exit", or "quit"
How It Works
The chatbot uses a `while` loop to keep the conversation going and `if-elif-else` statements to match user inputs against specific patterns or keywords.
Example:
```python
if user_input in ['hi', 'hello', 'hey']:
    print("Chatbot: Hello! How can I help you today?")
