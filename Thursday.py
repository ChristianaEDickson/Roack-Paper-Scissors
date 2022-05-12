from tkinter import Menu
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.RPS
posts = db.RPS
post_id = posts.insert_one({"p": 1}).inserted_id
print(post_id)
import random

#menu
def menu():
    print("[1] New Game")
    print("[2] View Leaderboard")
    print("[3] Update Username")
    print("[4] Delete Username")
    print("[0] Quit")

option = 5
while option != 0:
    menu()
    option = int(input("Enter your response: "))
    if option == 0:
        break
    elif option ==1:
        print("Welcome!")
        user_wins = 0
        computer_wins = 0
        options = ["rock", "paper", "scissors"]
        while True:
            user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            if user_input == "q":
                break
            if user_input not in options:
                continue
            random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
            computer_pick = options[random_number]
            print("Computer picked", computer_pick + ".")
            if user_input == "rock" and computer_pick == "scissors":
                print("You won!")
                user_wins += 1
            elif user_input == "paper" and computer_pick == "rock":
                print("You won!")
                user_wins += 1
            elif user_input == "scissors" and computer_pick == "paper":
                print("You won!")
                user_wins += 1
            else:
                print("You lost!")
                computer_wins += 1
        print("You won", user_wins, "times.")
        print("The computer won", computer_wins, "times.")
        UserID = input("Enter a username ")
        mydict = {"username": UserID, "Top_Score": user_wins}
        db.Leader_Board.insert_one(mydict)
    elif option ==2:
        for x in db.Leader_Board.find():
            print(x)
            
    elif option ==3:
       #update code
        collection = db.Leader_Board
        nu = input("Enter a new username: ")
        collection.update_one({"username": f'{UserID}'}, {'$set': {"username": f'{nu}'}})
    
    
    elif option ==4:
        collection = db.Leader_Board
        UserID = input("Enter a your username: ")
        collection.delete_many({"username": f'{UserID}'})

print("Goodbye")
