import random
import streamlit as st
import time
import pandas as pd
import numpy as np


# vector = ["name", "level", "questions solved"];
# data.txt is the name of where the user data will be stored
# loading the user in with their data

def askQuestion():
    thing = []
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
    problemType = ["+", "x", "/", "-"]
    realAnswer = typeShit[qtype]
    thing.append(realAnswer)
    thing.append(numberOne)
    thing.append(numberTwo)
    thing.append(problemType[qtype])
    return thing


# Main app
st.write("""
# Welcome to Math Off!
Made by *Thomas Laskowski*
""")

st.write("My Website [:link:](%s)" % "https://tomski.work/")

x = st.write("")

if st.button("Generate Problem"):
    vals = askQuestion()
    x = st.write(f"<p style='font-size:96px;'>{vals[1]} {vals[3]} {vals[2]}</p>", unsafe_allow_html=True)



# with open("users.txt", "r") as fp:
#     names = [line.strip() for line in fp]


# Functions to maybe use in the future?

# class SoloLeveling:
#     def __init__(self):
#         self.User = None
#         self.Level = 1
#         self.questionsSolved = 0
#         self.stats = [self.User, self.Level, self.questionsSolved]
#         print("Welcome to Math Off\nIn this program you will solve math problems to increase your mental math "
#               "abilities.\nI wish you the best of luck in your journey and hope the best for you.")
# 
#     def createData(self, user: str):
#         with open("data.txt", "a") as addData:
#             Level = 0
#             questionsSolved = 0
#             User = user
#             addData.write(f"{User},{Level},{questionsSolved}\n")
# 
#     def getData(self, user: str):
#         with open("data.txt", "r") as openData:
#             for userdata in openData:
#                 vector = userdata.strip().split(",")
#                 if vector[0] == user:
#                     print("User found!")
#                     self.User = user
#                     self.Level = int(vector[1])
#                     self.questionsSolved = int(vector[2])
#                     print("Data Loaded.")
#                     return
#             print("User not found in data.txt.")
# 
#     def getUserInfo(self, LoginType: str):
#         if LoginType.lower() == "l":
#             print("What is your username?")
#             for users in names:
#                 print(f"{users}")
#             getuser = input("Type your username: ")
#             if getuser in names:
#                 print("Loading your data")
#                 self.getData(getuser)
#                 print("Done!")
#             else:
#                 print("Username not found.")
#         elif LoginType.lower() == "n":
#             newUsername = input("What is the Username you want to use? : ")
#             self.createData(newUsername)
#             self.getData(newUsername)
# 
#     def askQuestion(self):
#         qtype = random.randint(0, 3)
# 
#         numberOne = 1
#         numberTwo = 11
# 
#         if qtype == 2:
#             while numberOne % numberTwo != 0:
#                 numberOne = random.randint(1, 10)
#                 numberTwo = random.randint(1, 10)
#         else:
#             while numberOne < numberTwo:
#                 numberOne = random.randint(1, 10)
#                 numberTwo = random.randint(1, 10)
# 
#         typeShit = [(numberOne + numberTwo), (numberOne * numberTwo), (numberOne / numberTwo), (numberOne - numberTwo)]
#         problemType = ["+", "*", "/", "-"]
#         realAnswer = typeShit[qtype]
#         userAnswer = -1
# 
#         while userAnswer != realAnswer:
#             userAnswer = int(input(f"{numberOne} {problemType[qtype]} {numberTwo} ?\n"))
#             if userAnswer == realAnswer:
#                 print("Correct!")
#             else:
#                 print("Incorrect")
# 
#     def saveData(self, solvedQuestions: int):
#         with open("data.txt", "r") as fp:
#             lines = fp.readlines()
# 
#         with open("data.txt", "w") as fp:
#             for userprofile in lines:
#                 temp = userprofile.strip().split(",")
#                 if temp[0] == self.User:
#                     temp[2] = str(int(temp[2]) + solvedQuestions)
#                 fp.write(",".join(temp) + "\n")
# 
#     def startSession(self, qAmount: int):
#         for i in range(qAmount):
#             self.askQuestion()
#         self.questionsSolved += qAmount
#         self.saveData(qAmount)
