#Import modules
import sys
import random

choice="Yes"
while (choice=="Yes"):

    #Enter user name
    name=input("Enter your name: ")
    print("\t\t\t\t Hi ",name," Welcome to GameInt")
    #Generate Random Number
    random_num= random.sample(range(1,6),4)
    
    #Game information   
    print("\nNumber to Guess- XXXX\t\t\t Colour mapping: 1- white 2- blue 3- Red")
    print("\t\t\t\t\t\t\t 4- yellow 5- Green 6- Purple \n")
    print("------------------------------------------------------------------------------------------")
    print("""GAME INSTRUCTIONS
        \n   Enter a digit at once \n   Enter 0000 to end the game \n   Enter digits in range 1 to 6 """)
    
    # Display menu and select Start/End for continue/Stop the game
    choice_to_play=0
    print ("\n\tGame Menu\n\t=========")
    print ("\t 1 - Start")
    print ("\t 2 - Stop\n")
    while(choice_to_play not in [1,2]):
        choice_to_play=int(input("Enter your Choice : "))
        # This reads either 1 or 2 from the player        
    # End of While loop choice_to_play 
    if (choice_to_play==2):
        # stop the program execution
        print("Game Stopped. - Thank you!")
        sys.exit()
    else:    
        print("-------------------------------------------------------------------------------------------")
            
        attempts=1
        points=0
        for i in range(1,9):
                      
            #Code breaker input digits for the guess num
            guess_numbers=[]
            n=1
            while (n< 5 ):
               guess=input("Enter your guess for the digit " +str(n)+ ": ")
               if (guess=="0000"):
                   print("Thank you for playing!!!")
                   sys.exit()
               else:
                   guess_digit=int(guess)
                   if (guess_digit<1):
                       print ("Number must be greater than 0")
                   else:
                       if (guess_digit> 6):
                           print ("Number must be less than 7")
                       else:
                           guess_numbers.append(guess_digit)
                           n=n+1

            #print(guess_numbers)
            result=[]
            if(guess_numbers[0]==random_num[0]):
                result.append("1")
            elif(guess_numbers[0]==random_num[1] or guess_numbers[0]==random_num[2] or guess_numbers[0]==random_num[3]):
                result.append("0")
            else:
                result.append(".")

            if(guess_numbers[1]==random_num[1]):
                result.append("1")
            elif(guess_numbers[1]==random_num[0] or guess_numbers[1]==random_num[2] or guess_numbers[1]==random_num[3]):
                result.append("0")
            else:
                result.append(".")

            if(guess_numbers[2]==random_num[2]):
                result.append("1")
            elif(guess_numbers[2]==random_num[0] or guess_numbers[2]==random_num[1] or guess_numbers[2]==random_num[3]):
                result.append("0")
            else:
                result.append(".")

            if(guess_numbers[3]==random_num[3]):
                result.append("1")
            elif(guess_numbers[3]==random_num[0] or guess_numbers[3]==random_num[1] or guess_numbers[3]==random_num[2]):
                result.append("0")
            else:
                result.append(".")

            #print(attempt number,code maker's guess num,result)
            print("\nAttempt No","\t\t\t","Guess","\t\t\t","Results")
            print(str(attempts),"\t\t\t\t",guess_numbers[0],guess_numbers[1],guess_numbers[2],guess_numbers[3],"\t\t",result[0],result[1],result[2],result[3])
            print("\n___________________________________________________________________________________________")

            #Calculate the points for attempt   
            if(result==['1','1','1','1']):
                print("\nCongratulations!!! you won the game...\n")
                points = 100 - (attempts-1) * 12.5
                print("You have scored",points,"points.")
                break
            else:
                attempts=attempts+1
            if (attempts == 9):
                print (" \nSorry you lost the game. The correct answer is ", random_num[0],random_num[1],random_num[2],random_num[3])
        choice=str(input(" \nDo you want to play another game? (Yes/ No) :"))


  
