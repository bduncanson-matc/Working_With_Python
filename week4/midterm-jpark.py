#! /usr/bin/env python3
# Variables
firstName = "Bryan"
lastName = "Duncanson"
password_database = {
    "Username": "dnedry",
    "Password": "please"
}
command_database = {
    "a. reboot": "OK. I will reboot all park system.",
    "b. shutdown": "Ok. I will shot down all park systems.",
    "c. done": "I hate all this hacker stuff.",
}
listPWDBKeys = list(password_database)
listCDBKeys = list(command_database)
magicWord = "You didnt say the magic word"
white_rabbit_object = 0
counter = 0

# Driver code
print(f"Name: {firstName:<>6}>{lastName:<>10}>")

while counter < 3 and white_rabbit_object == 0:  # counter less 3 and wro == 0
    input_user = input(f"{listPWDBKeys[0]::<9}")  # getting practice with fstrings
    input_password = input(f"{listPWDBKeys[1]::<9}")
    if input_user == password_database["Username"] and input_password == password_database["Password"]:  # username/pw validation
            white_rabbit_object = 1  # allowing user to proceed
            print("Hi, Dennis.  You're still the best hacker in Jurassic Park.")# This move was made in the early 90s and at that time they taught me 2 spaces after a period then :D
    else:
        counter += 1 # increment to limit limited attempts
        print(f"{magicWord}. {counter}")  # add failure string plus pw count
if white_rabbit_object == 1:  # Successful authentication loop
    print("Please enter a command")
    for key in command_database:
        print(f"{key}")
    user_command = input()
    if user_command == listCDBKeys[0] or user_command.lower() == "a" or user_command.lower == "reboot":
        print(command_database[listCDBKeys[0]])
    elif user_command == listCDBKeys[1] or user_command.lower() == "b" or user_command.lower == "shutdown":
        print(command_database[listCDBKeys[1]])
    elif user_command == listCDBKeys[2] or user_command.lower() == "c" or user_command.lower == "done":
        print(command_database[listCDBKeys[2]])
    else:
        print("The Lysine Contingency has been put in to effect.")
elif counter == 3:
    newLineMagicWord = f"{magicWord}!\n"
    print(f"{newLineMagicWord*25}")