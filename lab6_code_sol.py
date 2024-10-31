# Programmers:  [your name here]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program

#Initialize Program Constants
INITIAL_BALANCE = 1000
SENTINEL = 'E'

# Purpose: Display the available options for the user.
# Parameters: None
# Return: None
def display_menu():
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")
    
# Purpose: Add a user-specified amount to the current balance.
# Parameters: balance  The current account balance.
# Return: Updated balance after the deposit.
def deposit(balance):
    amount = input_amount('Enter the deposit amount: ')
    return balance + amount

# Purpose: Subtract a user-specified amount from the current balance and 
#          warn if the balance goes negative.
# Parameters: balance  The current account balance.
# Return: Updated balance after the withdrawal.
def withdraw(balance):
    amount = input_amount('Enter the withdraw amount: ')
    result = balance - amount
    if result < 0:
        print('Your balance is negative')
    return result

# Purpose: Get a valid non-negative integer amount from the user.
# Parameters: prompt (str): A string to display when asking for input.
# Return: int: Valid non-negative integer amount or 0 if input is invalid.
def input_amount(prompt):
    amount = input(prompt)
    if not amount.isdigit() or int(amount) < 0:
        return 0
    else:
        return int(amount)

# Purpose: Display the current balance to the user.
# Parameters: balance  The current account balance.
# Return: None
def view_balance(balance):
    print(f'Your current balance is {balance:.2f}')

# Purpose: Manage the program flow, take user input, and 
#          call the appropriate actions based on user choices.
# Parameters: None
# Return: None
def main():

    current_balance = INITIAL_BALANCE
    choice = ''

    while choice != SENTINEL:

        display_menu()
        choice = input('Enter your choice: ').upper().strip()

        if choice == 'D':
            current_balance = deposit(current_balance)
        elif choice == 'W':
            current_balance = withdraw(current_balance)
        elif choice == 'V':
            view_balance(current_balance)
        elif choice == 'E':
           print("Thank you for using the ATM program. Goodbye!")
        else:
            print("Error: Invalid choice. Please enter D, W, V, or E.")

main()






