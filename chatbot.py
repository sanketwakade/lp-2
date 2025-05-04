def chatbot():
    print("RetailBot: Hello! Welcome to ABC Retail. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "store hours" in user_input or "open" in user_input:
            print("RetailBot: Our store is open from 9 AM to 9 PM, Monday to Saturday.")
        elif "location" in user_input or "where" in user_input:
            print("RetailBot: We are located at 123 Main Street, Springfield.")
        elif "product" in user_input or "have" in user_input:
            print("RetailBot: Could you please specify the product name?")
        elif "laptop" in user_input:
            print("RetailBot: Yes, we have a variety of laptops in stock. You can check them out on our website.")
        elif "order status" in user_input or "track order" in user_input:
            print("RetailBot: Please enter your order number for tracking.")
        elif "12345" in user_input:
            print("RetailBot: Order #12345 is currently being processed and will be shipped tomorrow.")
        elif "bye" in user_input or "exit" in user_input:
            print("RetailBot: Thank you for visiting ABC Retail. Have a great day!")
            break
        else:
            print("RetailBot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
