import random

import sys
sys.path.append('../..')

from i import input_function

#set up while loop to loop through menu until user quits
exit = 0
while exit == 0:
    print("Problems in this set: \n 1.Name input   2.Madlib   3.Madlib 2   4.Age   5.Rock Paper Scissors")
    print("Select prob_num 1, 2, 3, 4, or 5")
    prob_num = 0
    #limit problem input to 1, 2, 3, 4, or 5
    while prob_num != "1" and prob_num != "2" and prob_num != "3" and prob_num != "4" and prob_num != "5":
        prob_num = input()

    if prob_num =="1":
        #ask user for name
        print("What is your name?")
        name = input()
        print("hello, "+name+", and welcome to my program.")

    elif prob_num =="2":
        #take input words for madlib
        print("Please input the following parts of speech:")
        adjective = input("Adjective: ")
        noun1 = input("Noun: ")
        verb = input("Past-tense verb: ")
        noun2 = input("Another noun: ")
        #the quick brown fox jumped over the lazy dog
        print("The quick, ",adjective,noun1,verb,"over the lazy ",noun2,".")

    elif prob_num =="3":
        #take input words for madlib
        print("Please input the following parts of speech:")
        feeling = input("Irrational and persistent feeling: ")
        gerund1 = input("Gerund: ")
        reflective = input("Reflective surface: ")
        gerund2 = input("Another gerund: ")
        utility = input("Utility vehicle: ")
        #almost cut my hair
        print("It increases my "+feeling+", like "+gerund1+" into the "+reflective+" and "+gerund2+" a "+utility+".")

    elif prob_num =="4":
        #ask user how many years old they are
        age = float(input("How many years old are you? (in decimal values only)"))

        #set up try except to catch age < 0 error
        valid = False
        while valid == False:
            try:
                #print all matching responses
                if age >= 0 and age < 16:
                    print("You can't do much yet.")
                if age >= 16:
                    print("You can drive.")
                if age >= 18:
                    print("You can vote.")
                if age >= 21:
                    print("You can enjoy a beer.")
                if age >= 55:
                    print("You get the senior discount.")
                valid = True
            except age < 0:
                print("Not born yet. Try again.")

    elif prob_num =="5":
        #array for play names
        plays = ["Rock", "Paper", "Scissors"]
        #request user input
        print("Choose a number: 1. Rock, 2. Paper, or 3. Scissors? ")
        user = int(input_function("int"))

        #generate computer's play
        computer = random.randrange(1,3)

        #display results
        print("\n")
        print("You have chosen ",plays[user - 1],".")
        print("Computer has chosen ",plays[computer - 1],".")
        print("\n")
        print("User: ",plays[user - 1]," vs. Computer: ",plays[computer - 1])

        if user > computer:
            print(plays[user - 1]+" beats "+plays[computer - 1]+"! User wins!")
        elif computer > user:
            print(plays[computer - 1]+" beats "+plays[user - 1]+"! Computer wins!")
        elif user == computer:
            print("both players have "+plays[user - 1]+"! Tie!")

    #check if user wants to exit; if user does not want to exit, continue while loop with exit = 0
    path_var = input("Press any key (besides q) to return to problem menu, or q to quit: ")
    if path_var == "q":
        exit = 1




