""" CAPSTONE PROJECT.
This project allows the user to access two different financial calculators.
Calculators: investment calculator and a home loan repayment calculator.
"""
import math

# User receives a greeting message and is prompted to choose a preferred calculator.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
print("")

if user_selection.lower() == "investment":

    # User selects preferred interest type.
    interest = input("Please enter your interest type (simple or compound): ")
    print("")
    try:
        # If user enters 'simple', collect user financial details and calculate simple interest.
        if interest.lower() == "simple":
            principal = float(input("Enter your deposit amount: £ "))
            rate = float(input("What is your interest rate: % "))
            time = float(input("How many years are you planning on investing?: "))
            print("")

            # Catch potential negative integer from user and return appropriate error message.
            if principal < 0 or rate <= 0 or time <= 0:
                print("Invalid entry! Please enter a number greater than zero.\n")

            # Calculate the amount to be paid to the user and output this to the user.
            else:
                amount = principal * (1 + rate * time)
                print(f"By the end of {time} years, you will be paid: £ {amount}\n")

        # If user enters 'compound', collect user financial details and calculate compound interest.
        elif interest.lower() == "compound":
            principal = float(input("Enter your deposit amount: £ "))
            rate = float(input("What is your interest rate: % "))
            time = float(input("How many years are you planning on investing?: "))
            print("")

            # Catch potential negative integer from user input and return appropriate error message.
            if principal < 0 or rate <= 0 or time <= 0:
                print("Invalid entry! Please enter a number greater than zero.\n")

            # Calculate the amount to be paid to the user and output this to the user.
            else:
                amount = principal * math.pow((1+rate),time)
                print(f"By the end of {time} years, you will be paid: £ {amount}\n")

        # Catch any invalid entry from user and return appropriate error message
        elif interest.lower() != "simple" and interest.lower() != "compound":
            print("Invalid option! Please try entering either 'simple' or 'compound'.\n")
    except ValueError as ve:
        print(f"Invalid entry!\nError message: {ve}\nPlease enter a valid number only.\n")


# If user chooses to calculate repayment on bond, collect user financial details.
elif user_selection.lower() == "bond":
    try:
        house_value = float(input("What is the value of your house: £ "))
        rate = float(input("Please enter your repayment rate: % "))
        monthly_rate = (rate / 100) / 12
        time = float(input("In how many months do you intend to repay the bond?: "))
        print("")

        # Catch potential negative integer from user input and return appropriate error message.
        if house_value < 0 or rate < 0 or monthly_rate < 0:
            print("Invalid entry! Please enter a number greater than zero.\n")

        else:
            # Calculate the amount to be repayed and output this to user.
            repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate)**(-time))
            print(f"Every month, you will have to repay £ {repayment}\n")

    # Catch potential ValueError or ZeroDivisionError and return appropriate error message to user.
    except (ValueError, ZeroDivisionError) as e:
        print(f"Invalid entry!\nError message: {e}\n")

else:
    print("Invalid entry! Please try again.\n") # Display error message for invalid entry.
