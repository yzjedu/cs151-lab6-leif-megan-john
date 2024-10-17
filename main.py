# Programmers:  Leif LaBianca, Megan Wijdoogen, John Elehwany
# Course:  CS151, Professor Zee
# Due Date:  Thursday October 24, 12:15
# Programming Assignment:  Lab5
# Problem Statement:  Running an ATM loop that can deposit to, withdraw from, and view the balance
# Data In: Path choice as a single letter, deposit/withdraw amount if necessary
# Data Out:  Amount of balance remaining if necessary
# Credits: All original code

# defines reused variables at the very beginning
account_balance = 1000
selected_option = ''
continue_cycle = True

# outputs introduction to user
print('Welcome to the ATM.\nYou have a starting balance of 1000$.\nPlease use it wisely.\n')

# program will loop as long as exit is not selected setting continue_cycle to boolean false
while continue_cycle:
    # pass_thru is used for withdraw and deposit instances and defaults to false for error checking
    pass_thru = False
    # requests path choice from user
    selected_option = input("Would you like to deposit, withdraw, view your balance, or exit?\nPlease express your answer in the form of the option's first letter: ")
    # if user selects deposit, user inputs the amount they want to deposit and is added to balance if valid
    if selected_option.lower() == 'd':
        while not pass_thru:
            deposit_amount = input("\nHow much money would you like to deposit? ")
            if deposit_amount.isdigit():
                deposit_amount = int(deposit_amount)
                if deposit_amount > 0:
                    account_balance = account_balance + deposit_amount
                    print(f'Succesfully deposited {deposit_amount} dollars.\nYour balance is now {account_balance} dollars.\n')
                    pass_thru = True
                else:
                    print('Your value cannot be zero. Please try again.')
            else:
                print('Your input must be a positive whole number expressed in integer form. Please try again.')
    # if the user wants to withdraw and has no money, it prints an error and loops back
    elif selected_option.lower() == 'w' and account_balance == 0:
        print('You have a balance of zero and cannot withdraw at this time. Please select another option.\n')
    # if user selects withdraw, user inputs the amount they want to withdraw and is subtracted to balance if valid
    elif selected_option.lower() == 'w':
        while not pass_thru:
            withdraw_amount = input("\nHow much money would you like to withdraw? ")
            if withdraw_amount.isdigit():
                withdraw_amount = int(withdraw_amount)
                if withdraw_amount > 0 and withdraw_amount <= account_balance:
                    account_balance = account_balance - withdraw_amount
                    print(f'Succesfully withdrawn {withdraw_amount} dollars.\nYour balance is now {account_balance} dollars.\n')
                    pass_thru = True
                elif withdraw_amount > 0 and withdraw_amount >= account_balance:
                    print(f'Your value cannot be more than your account balance ({account_balance}$). Please try again.')
                else:
                    print('Your value cannot be zero. Please try again.')
            else:
                print('Your input must be a positive whole number expressed in integer form. Please try again.')
    # if the user selects to view, it outputs the accounts current balance
    elif selected_option.lower() == 'v':
        print(f'Your current account balance is {account_balance}$.\n')
    # if the user selects exits, it outputs an exit message and sets continue_cycle to boolean False
    elif selected_option.lower() == 'e':
        print('Thank you for using our ATM!')
        continue_cycle = False
    # otherwise it prints an error and reiterates to the user how to input a valid answer
    else:
        print('Invalid option. Please try again.\nRemember to express your choice as the first letter of the option (d, w, v, e).\n')