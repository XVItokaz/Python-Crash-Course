prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to got to " + city.title() + "!")

    