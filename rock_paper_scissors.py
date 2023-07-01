import csv
import sys
import random

print("*"*20,"FR. AGNEL SCHOOL, NEW DELHI ","*"*20)
print("*"*20,"Rock, Paper, Scissors- Game ","*"*20)

def get_user_ID():
    try:
        with open("leaderboard.csv" , "r" , newline = "") as file:
            try:
                reader = csv.reader(file)
                length = 0
                for row in reader:
                    length += 1
            except EOFError:
                length = 0
        return str(1 + length)
    except FileNotFoundError:
        f = open("leaderboard.csv" , "w" , newline = "")
        f.close()
        return 1

def check_user_id(id):
    try:
        with open("leaderboard.csv" , "r" , newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id:
                    return True
        return False
    except FileNotFoundError:
        f = open("leaderboard.csv" , "w" , newline = "")
        f.close()
        return False

def new_user():
    print ("Please enter your name")
    name = input().title()
    if name:
        print (f"Please remember that your user ID is {get_user_ID()}")
        with open("leaderboard.csv" , "a" , newline = "") as file:
            lst = [get_user_ID() , name , 0]
            writer = csv.writer(file)
            writer.writerow(lst)
    else:
        print ("Please enter a valid name from next time")

def update_record(id , score):
    with open("leaderboard.csv" , "r" , newline = "") as file:
        reader = csv.reader(file)
        lst = []
        for row in reader:
            lst.append(row)

    for record in lst:
        if record[0] == id:
            record[2] = str(int(record[2]) + score)

    with open("leaderboard.csv" , "w" , newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(lst)

def display_records():
    try:
        with open("leaderboard.csv" , "r" , newline = "") as file:
            reader = csv.reader(file)
            lst = []
            for row in reader:
                lst.append(row)
        if lst:
            print ("ID \t\t\t NAME \t\t\t SCORE")
            for record in lst:
                for data in record:
                    print (data , end = "\t\t\t")
                print ()
        print ("NO RECORDS EXIST !!!!!")

    except FileNotFoundError:
        f = open("leaderboard.csv" , "w" , newline = "")
        f.close()
        print ("NO RECORDS EXIST !!!!!")

def display_particular_record(id):
    try:
        with open("leaderboard.csv" , "r" , newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id:
                    print ("ID \t\t\t NAME \t\t\t\t  SCORE")
                    print (f"{row[0]} \t\t\t {row[1]} \t\t\t {row[2]}")
                    return
            print ("PLEASE ENTER A VALID USER ID !!!!!")

    except FileNotFoundError:
        f = open("leaderboard.csv" , "w" , newline = "")
        f.close()
        print ("NO RECORDS EXIST !!!!!")


def game_round():
    score = 0
    print ("Winning Rules of the Rock paper scissor game as follows")
    print ("Rock vs Paper->Paper wins")
    print ("Rock vs Scissors->Rock wins")
    print ("Paper vs Scissors->Scissors wins")
    print ()
    print ("Here are your choice")
    print ("1. Rock")
    print ("2. Paper")
    print ("3. Scissors")
    print ("Please enter your choice")

    choice = int(input())
    while choice < 1 and choice > 4 and choice:
        try:
            choice = int(input())
        except ValueError:
            print ("Please enter a valid choice")

    comp = random.randint(1,3)

    if choice == comp:
        return 0

    elif choice == 1 and comp == 3:
        return 2

    elif choice == 2 and comp == 1:
        return 2

    elif choice == 3 and comp == 2:
        return 2

    else:
        return -1

def main_game():
    ID = input("Please enter the user ID ").rstrip()

    valid = check_user_id(ID)
    while valid:
        print ("Do you want to play ? (Y/N) ")
        choice = input()

        if choice.lower() == "n":
            break

        elif choice.lower() != "y":
            print ("Please enter a valid choice")
            continue

        else:
            score = 5 * game_round()
            update_record(ID , score)
            if score > 0:
                print ("You won the round")
            elif score == 0:
                print ("Round tied")
            elif score < 0:
                print ("You lost the round")

    if not(valid):
        print ("Please enter a valid user ID")


def main_menu():
    while True:
        print ("1. Display all the records")
        print ("2. Display particular record")
        print ("3. Add a new record")
        print ("4. Play a game")
        print ("5. Quit")
        print ()
        choice = int(input("Please enter your choice(1/2/3/4/5) "))

        if choice == 1:
            display_records()
        elif choice == 2:
            id = input("Please enter the ID of the person you want to show record for")
            if check_user_id(id):
                display_particular_record(id)
            else:
                print ("NO RECORDS EXIST !!!!!")
        elif choice == 3:
            new_user()
        elif choice == 4:
            main_game()
        elif choice == 5:
            break
        else:
            print ("Please enter a valid choice")
        print ('\n\n')
main_menu()
