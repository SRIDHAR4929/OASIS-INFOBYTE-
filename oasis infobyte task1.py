import datetime
import webbrowser

while True:
    command = input("Enter command: ").lower()

    if command == "hello":
        print("Assistant: Hello! How can I help you?")

    elif command == "time":
        print("Current Time:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif command == "date":
        print("Today's Date:", datetime.date.today())

    elif command.startswith("search"):
        query = command.replace("search", "")
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif command == "exit":
        print("Assistant: Goodbye!")
        break

    else:
        print("Assistant: Sorry, I don't understand.")
