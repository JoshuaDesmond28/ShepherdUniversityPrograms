import random  # impots random in order to use its functions for the dice


def Craps():
    while True:  # will run while the program is true
        print("Hello \n Welcome to 7/11! \n This is a gambling dice game")  # tells the user what the program is
        try:  # this will lock the user into a loop preventing them from entering anything that is not greater than 1
            while True:  # this while loop will continue to lock the user in until bid>1
                bid = float(input(
                    "Enter the amount you would like to bet. Your bet must be higher than 1"))  # will turn a string into a float
                if bid > 1:  # checks to see if bid is greater than one
                    print(f'You are betting ${bid}')  # tells the user their bid
                    break  # breaks out of this while loop

                elif bid < 1 or bid == 1:  # checks to see if bid is not greater than one.
                    print('You need to bet more than 1')
                    continue  # continues the loop

        except ValueError:  # this will keep the program from crashing incase the user enters a letter or such
            print("You must not have entered something more than 1")
            continue  # continues the loop
        x1 = random.randrange(1, 7)  # defines dice 1
        x2 = random.randrange(1, 7)  # defines dice 2
        dice_roll = x1 + x2  # defines the dice roll
        print(f"you rolled a {dice_roll}")  # tells the user what they rolled
        match dice_roll:  # begins a switch to determine what to do with the dice rolled

            # WINNING CONDITIONS
            case 7:  # the user wins if a 7 is rolled
                print('you won!')
                bid += 1  # adds 1 to the bid
                print(f'your bid is now ${bid}')
                break  # breaks the while loop and ends the game

            case 11:  # the user wins if 11 is rolled
                print("you won!")  # informs the user of the result
                bid += 1  # adds 1 to the bid
                print(f'your bid is now ${bid}')
                break  # breaks the while loop and ends the game

            # LOSING CONDITIONS

            case 2:  # user will lose if the roll is a 2
                print('you lost!')
                bid -= 1  # updates the bid to 1 lower since they lost
                print(f'your bid is now ${bid}')
                break  # breaks out of the will loop and ends the game

            case 3:  # user loses if roll is a 3
                print('you lost!')
                bid -= 1  # updates the bid to 1 lower since they lost
                print(f'your bid is now ${bid}')
                break  # breaks out of the while loop and ends the game

            case 12:  # if the dice is equal to 12
                print('you lost!')
                bid -= 1  # updates the bid to 1 lower since they lost
                print(f'your bid is now ${bid}')
                break  # breaks out of the while loop and ends the game

            # DEFAULT CONDITION

            case _:  # the default case if the user did not win or lose
                print('you did not win or lose')  # informs the user the outcome and what follows.
                print('we will play again')
                while True:  # a new loop to roll the dice until the user wins or loses
                    x1 = random.randrange(1, 7)
                    x2 = random.randrange(1, 7)
                    dice_roll = x1 + x2  # the dice is redefined and will roll until the user wins or loses
                    if dice_roll == bid:  # sees if the dice_roll equals the bid
                        print(
                            f"you won because you rolled a {dice_roll} and that is equal to your bid of {bid}")  # if it does, then it will tell the user they won
                        bid += 1
                        print(f'your bid is now ${bid}')
                        break  # breaks out of the second while loop
                    elif dice_roll == 7:  # checks if the dice rolled a 7.
                        print(
                            f'you lost because you rolled a {dice_roll} before a {bid} which would have equaled your bid of ${bid}')  # if a 7 is rolled. the user is told they lost
                        bid -= 1
                        print(f'your bid is now ${bid}')
                        break  # breaks out of the second while loop
                    else:  # this will continue rolling the dice until one of the two conditions are met
                        print(f'you rolled a {dice_roll}')
                        print('rolling again...')
                break  # breaks out of the default cases of the switch. Ends the code if the if statement above is met


def play_again(): #  creates a new function to decide if the player wants to play again or not
    while True:  #while loop to prevent the user from crashing the game
        try: #creates a try loop to prevent errors
            cont = input(f"Would you like to continue playing?")
            if cont.lower() == 'yes': #plays again if user says yes
                print(f'okay we will continue playing')
                Craps()
            elif cont.lower() == 'no': #breaks if the user enters no
                print('okay we will end the game')
                break
            else:
                print('you did not enter yes or no')
        except ValueError:
            print('please enter the appropriate value') #will accept value errors to prevent the code from crashing


Craps()
play_again()
