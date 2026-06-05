def Taskbot():
    print("Taskbot: Hello! Type 'bye' to exit.")

    while True:
        user_prompt = input("You: ").lower()

        if user_prompt== "bye":
            print("Taskbot: Goodbye!")
            break

        elif "hello" in user_prompt or "hi" in user_prompt:
            print("Taskbot: Hi there!")

        elif "your name" in user_prompt:
            print("Taskbot: I am a simple Taskbot.")

        elif "how are you" in user_prompt:
            print("Taskbot: I'm fine!")

        elif "help" in user_prompt:
            print("Taskbot: Ask me basic questions like greetings.")

        elif "color" in user_prompt:
            fav_color = input("Taskbot: What is your favorite color? ")
            print("Taskbot: Wow!", fav_color, "is a nice color!")

        elif "add" in user_prompt:
            print("Taskbot: Enter two numbers:")
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print("Taskbot: Sum is", a + b)

        else:
            print("Taskbot: Sorry, I don't understand.")
Taskbot()
