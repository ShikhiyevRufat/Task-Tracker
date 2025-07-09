from main import start_app

if __name__ == "__main__":
    while True:
        start_app()
        again = input("\nDo you want to continue? (y/n): ")
        if again.lower() != "y":
            break
