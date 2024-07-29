age = int(input("What is your age? (Please remember to put in only your age as numbers. For example '23')"))

if age < 4:
    print("Your admission cost is €0.")

elif age < 18:
    print("Your admission cost is €5.")

else:
    print("Your admission cost is €10.")

