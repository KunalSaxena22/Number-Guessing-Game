#UNIcompiler
#NUMBER GUESSING GAME
#1st Task

import random
from random import randint

print("This Game Is Very Tricky \nSo hope you are enjoing")

n = input("Please Enter your name => ")
print("Hello "+ n +" Wellcome to Number Guessing Game ")

def fun():
    rand_no = randint(1, 100)
    a = rand_no / 2;
    b = rand_no * 2;
    print("Please select the number between 1 to 100. \nYou have only 5 chances to win the Game")
    i = 1
    r = 1
    while i<=5:
        number = int(input("Enter the number=> "))
        if number <= 1 or number > 100:
            print("\n"+n+"Please Enter a number between 1 to 100 ")
            continue
        elif number < rand_no:
            print("\n"+n+" The Secret Number Is Greater Then your guessed number")
            print("HINT=> The Secret number is related to this two number "+str(a)+", "+str(b)+"  Please find it")
            print("Now " + str(5 - i) +  " Chances left")
            i = i + 1
        elif number > rand_no:
            print("\n"+n+" The Secret Number Is Smaller Then your guessed number")
            print("HINT=> The Secret number is related to this two number "+str(a)+", "+str(b)+"  Please find it")
            print("Now " + str(5 - i) + " Chances left")
            i = i + 1
        elif number == rand_no:
            print("\nCongrats " + n + " You Won The Game")
            r = 0
            break
        else:
            print("This is an invalid number.   please try again")
            print("Now" + str(5 - i) + " Chances left")
            continue
    if r==1:
        print("Ooops you lost the amazing game!!")
        print("The correct number is "+ str(rand_no))

def main():
    fun()
    while True:
        more = input("Play again to won the game.\nIf you want to play. press 'y'=> ")
        if more == "y":
            fun()
        else:
            break

main()
print("\nTHANKYOU "+n+" for playing the game!")

