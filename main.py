import random

# vector = ["name", "level", "questions solved"];
# data.txt is the name of where the user data will be stored
# formatting data?
# formatting data is simple use ##//## to separate each vector :)

# loading the user in with their data
fp = open("users.txt", "r")
names = []
for line in fp:
    names = line.strip().split(",")

first = input("Create New User or Login? (N/L) \n")
if first.lower() == "n":
    name = input("enter name (will be saved to disk) \n")
    file = open("users.txt", "a")
    listy = f"{name},"
    file.write(listy)
if first.lower() == "l":
    print("What is your username?")
    for users in names:
        print(f"{users}")
    getuser = input("type your username: ")
    if getuser in names:
        print("Loading your data")
        fp = open("data.txt", "r")
        # implement storage here
        print("Done!")

print("Welcome to Math Off\nIn this program you will solve math problems to increase your mental math abilities and "
      "face off opponents.\nI wish you the best of luck in your journey and hope the best for you.")

game_mode = int(input("Select your Game mode! \n 1.) Solo Leveling \n 2.) Multiplayer \n 3.) QuickTime\n"))

if game_mode == 1:


    i = 0
    while i < 10:
        questionType = random.randint(0,3)

        if questionType == 0:
            numberOne = random.randint(1, 10)
            numberTwo = random.randint(1, 10)
            userAnswer = int(input(f"{numberOne} + {numberTwo}?\n"))
            if userAnswer == numberOne + numberTwo:
                print("Correct")
            else:
                print("Incorrect!")
                while userAnswer != (numberTwo + numberOne):
                    userAnswer = int(input(f"{numberOne} + {numberTwo}?\n"))
        if questionType == 1:

            numberOne = random.randint(1, 10)
            numberTwo = random.randint(1, 10)
            while numberOne < numberTwo:
                numberTwo = random.randint(1, 10)
            userAnswer = int(input(f"{numberOne} - {numberTwo}?\n"))
            if userAnswer == numberOne - numberTwo:
                print("Correct")
            else:
                print("Incorrect!")
                while userAnswer != (numberTwo - numberOne):
                    userAnswer = int(input(f"{numberOne} - {numberTwo}?\n"))
        if questionType == 2:

            numberOne = random.randint(1, 10)
            numberTwo = random.randint(1, 10)

            userAnswer = int(input(f"{numberOne} * {numberTwo}?\n"))
            if userAnswer == numberOne * numberTwo:
                print("Correct")
            else:
                print("Incorrect!")
                while userAnswer != (numberTwo * numberOne):
                    userAnswer = int(input(f"{numberOne} * {numberTwo}?\n"))
        if questionType == 3:

            numberOne = random.randint(1, 10)
            numberTwo = random.randint(1, 10)

            while numberOne % numberTwo != 0:
                numberOne = random.randint(1, 10)
                numberTwo = random.randint(1, 10)

            userAnswer = int(input(f"{numberOne} / {numberTwo}?\n"))
            if userAnswer == numberOne / numberTwo:
                print("Correct")
            else:
                print("Incorrect!")
                while userAnswer != (numberTwo / numberOne):
                    userAnswer = int(input(f"{numberOne} / {numberTwo}?\n"))
        i += 1


