import math  # imports the math module in order to perform the square root and b root of a functions

while True:  # the while loop makes it so that the calculator will run continuously unless the user wants it to stop

    try:
        a = float(input("Enter your first number..."))  # creates the variable a
        b = float(input("Enter your second number..."))  # creates the variable b
    except ValueError:  # If the user fails to input a number for either a or b, this will cause the program to restart
        print('Please enter a number')
        print('try Again')
        continue
    try:
        operation = int(input("enter the number for the operation you would like to perform...\n"
                              "  1= Addition \n "
                              " 2= Subtraction \n "
                              " 3= Multiplication \n "
                              " 4= Division \n "
                              " 5= Exponents \n "
                              " 6= Square root of a \n "
                              " 7= a to the root of b"))  # creates the operation variable and picks the operation the calculator will perform
    except ValueError:  # This will loop the user back to the beginning of the program if they
        print("INVALID INPUT!!")
        print("Please enter the number associated with the operation you want to perform")
        continue

    if operation == 1:  # Addition
        print("You have chosen addition")  # tells the user the operation they chose
        c = a + b  # performs the operation
        print(f'c = {c}')  # outputs the operation
        try:  # checks the program for an error
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program"))  # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
    elif operation == 2:  # Subtraction
        print("You have chosen subtraction")  # tells the user the operation they chose
        c = a - b
        print(f'c = {c}')
        try:  # checks for an error if the user were to enter something other than an integer
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program as well"))
            # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
    elif operation == 3:  # Multiplication
        print("You have chosen multiplication")
        c = a * b  # performs the operation
        print(f'c = {c}')  # outputs the operation
        try:  # checks the program for an error
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program"))
            # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
    elif operation == 4:  # Division
        print("You have chosen division")
        try:
            c = a / b
        except ZeroDivisionError:
            print(f'c = 0')
        else:
            print(f'c= {c}')
        try:  # checks the program for an error
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program"))
            # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
    elif operation == 5:  # Exponents
        print("You have chosen exponents")
        c = a ** b
        print(f'c = {c}')
        try:  # checks the program for an error
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program"))
            # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning, and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
    elif operation == 6:  # square root
        print("You have chosen square root")
        print(f'the square root of {a} is, ', math.sqrt(a))
        try:  # checks the program for an error
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program"))  # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
    elif operation == 7:  # Nth root
        print('you have chosen the nth root of a number')  # tells the user the operation
        try:
            c = a ** (1.0 / b)
        except ZeroDivisionError:
            c = a ** 0
            print(f'the {b}th root of {a} = {c}')
        else:
            print(f'the {b}th root of {a} = {c}')
        try:  # checks the program for an error
            continuation = int(input(
                "Would you like to do another operation? Enter 1 for Yes or 2 for No (entering any other number will terminate the program"))  # asks the user if they want to stop calculating or continue
        except ValueError:
            print("Invalid Input!")
            print("please enter 1 or 2")
            continue  # if the user enters an invalid option it will force them to start over
        if continuation == 1:  # It will loop the user back to the beginning and they can continue to calculate
            pass
        elif continuation == 2:  # will end the program
            print("okay. calculator shutting down...")
            break
        else:
            print('Ending program because you did not choose 1 or 2')
            break
