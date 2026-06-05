def user_recommendation():
    print(" Welcome to Recommendation System")

    movies = {
        "action": ["RRR", "Pushpa: The Rise", "Sye Raa Narasimha Reddy"],
        "comedy": ["Jathi Ratnalu", "MAD", "Nuvvu Naaku Nachchav"],
        "romance": ["Sita Ramam", "Tholi Prema", "Geetha Govindam"],
        "thriller": ["Kshanam", "Goodachari", "Bhaagamathie"]
    }

    books = {
        "fiction": ["Harry Potter series", "The Hobbit", "Percy Jackson"],
        "self help": ["Atomic Habits", "The Power of Now", "Think and Grow Rich"],
        "mystery": ["Sherlock Holmes", "Gone Girl", "The Girl with the Dragon Tattoo"],
        "fantasy": ["Game of Thrones", "Lord of the Rings", "The Witcher"]
    }

    while True:
        print("\n Choose an option:")
        print("1. Movies")
        print("2. Books")
        print("3. Exit")

        user_option = input("Enter user_option 1/2/3): ")

        if user_option == "1":
            print("\nAvailable movie genres:")
            for genre in movies:
                print("-", genre)

            genre = input("Enter genre: ").lower()

            if genre in movies:
                print("\n Recommended Movies:")
                for item in movies[genre]:
                    print("-", item)
            else:
                print(" No recommendations found.")

        elif user_option == "2":
            print("\nAvailable book genres:")
            for genre in books:
                print("-", genre)

            genre = input("Enter genre: ").lower()

            if genre in books:
                print("\n📖 Recommended Books:")
                for item in books[genre]:
                    print("-", item)
            else:
                print(" No recommendations found.")

        elif user_option == "3":
            print(" Exiting... Thank you!")
            break

        else:
            print("⚠️ Invalid user_option ! Please try again.")
user_recommendation()
