import random
import math

# Load all usernames from the file
with open("data.txt", "r") as fp:
    # Extract only the usernames (first item of each line)
    names = [line.strip().split(",")[0] for line in fp]


class SoloLeveling:
    def __init__(self):
        self.User = None
        self.Level = 1
        self.questionsSolved = 0
        self.xp = 0
        self.required_xp = int(pow((self.Level + 1 / 0.07), 2) + math.log10(self.Level + 1))
        print(
            "Welcome to Math Off\nIn this program you will solve math problems to increase your mental math abilities.\n"
            "I wish you the best of luck in your journey and hope the best for you.")

    # This Function creates a new user in the Data in the TXT File.
    def createData(self, user: str):
        with open("data.txt", "a") as addData:
            Level = 0
            questionsSolved = 0
            xp = 0
            addData.write(f"{user},{Level},{xp},{questionsSolved}\n")

    def getData(self, user: str):
        with open("data.txt", "r") as openData:
            for userdata in openData:
                vector = userdata.strip().split(",")
                if vector[0] == user:
                    print("User found!")
                    self.User = user
                    self.Level = int(vector[1].strip())
                    self.xp = int(vector[2].strip())
                    self.questionsSolved = int(vector[3].strip())
                    self.required_xp = int(pow((self.Level + 1 / 0.07), 2) + math.log10(self.Level + 1))
                    print(self.required_xp)
                    print("Data Loaded.")
                    return
            print("User not found in data.txt.")

    def getUserInfo(self):
        LoginType = input("L for Login, N for Create User\n")
        if LoginType.lower() == "l":
            print("What is your username?")
            getuser = input("Type your username: ")
            if getuser in names:
                print("Loading your data")
                self.getData(getuser)
            else:
                print("Username not found.")
                for i in names:
                    print(i)
                newortry = input("Try Again (T) or Create New Account (N)?")
                if newortry.lower() == "t":
                    print("What is your username?")
                    getuser = input("Type your username: ")
                    if getuser in names:
                        print("Loading your data")
                        self.getData(getuser)
                    else:
                        print("Restart Program try again.")
                if newortry.lower() == "n":
                    newUsername = input("What is the Username you want to use? : ")
                    self.createData(newUsername)
                    self.getData(newUsername)
        elif LoginType.lower() == "n":
            newUsername = input("What is the Username you want to use? : ")
            self.createData(newUsername)
            self.getData(newUsername)

    def displayStats(self):
        print(f"Your current level is {self.Level}, and you have solved {self.questionsSolved} questions. \n"
              f"You need {self.required_xp - self.xp} more xp to level up ({self.xp} / {self.required_xp}). ")

    def askQuestion(self):
        qtype = random.randint(0, 3)
        numberOne = 1
        numberTwo = 11

        if qtype == 2:
            while numberOne % numberTwo != 0:
                numberOne = random.randint(1, 10)
                numberTwo = random.randint(1, 10)
        else:
            while numberOne < numberTwo:
                numberOne = random.randint(1, 10)
                numberTwo = random.randint(1, 10)

        typeShit = [(numberOne + numberTwo), (numberOne * numberTwo), (numberOne / numberTwo), (numberOne - numberTwo)]
        problemType = ["+", "*", "/", "-"]
        realAnswer = typeShit[qtype]
        userAnswer = -1

        while userAnswer != realAnswer:
            userAnswer = int(input(f"{numberOne} {problemType[qtype]} {numberTwo} ?\n"))
            if userAnswer == realAnswer:
                print("Correct!")
                return True
            else:
                print("Incorrect")

    def saveData(self, solvedQuestions: int, levelup: bool):
        with open("data.txt", "r") as fp:
            lines = fp.readlines()

        with open("data.txt", "w") as fp:
            for userprofile in lines:
                temp = userprofile.strip().split(",")
                if not levelup:
                    temp[2] = str((int(temp[2].strip()) + (int((math.sqrt(self.required_xp) * int(solvedQuestions))))))
                    temp[3] = str(int(temp[3].strip()) + int(solvedQuestions))
                else:
                    temp[1] = str(self.Level)
                    temp[2] = str(0)
                    temp[3] = str(int(temp[3].strip()) + int(solvedQuestions))
                fp.write(",".join(temp) + "\n")

    # Required Function Should Be Altered After Play Testing
    def checkLevelUp(self):
        print(self.required_xp)
        if self.xp >= self.required_xp:
            print(f"Leveled Up!\n You are now level {self.Level + 1}!")
            self.xp = 0
            self.Level = self.Level + 1
            return True
        else:
            return False

    def startSession(self, qAmount: int):
        for _ in range(qAmount):
            self.askQuestion()
        self.questionsSolved += qAmount
        if self.checkLevelUp():
            self.saveData(qAmount, True)
        else:
            self.saveData(qAmount, False)
        self.displayStats()


main = SoloLeveling()
main.getUserInfo()
main.startSession(10)
main.checkLevelUp()
