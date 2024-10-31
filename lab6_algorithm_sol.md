### Create Constants 
- Initialize the Initial Balance and Sentinel
- `INITIAL_BALANCE` = 1000
- `SENTINEL` = 'E'
---------------------------------
### Algorithm for `menu`
- **Purpose**: To display the available options for the user.
- **Name**: display_menu
- **Parameters**: none
- **Return**: none
- **Algorithm**:
  1. Print a message showing the menu options: 
    - D for Deposit,
    - W for Withdraw, 
    - V for View Balance, and 
    - E for Exit.
---------------------------------
### Algorithm for `deposit`
- **Purpose**: To add a user-specified amount to the current balance.
- **Name**: deposit
- **Parameters**: balance (current account balance)
- **Return**: Updated balance after the deposit
- **Algorithm**:
  1. Call `input_amount` with the prompt to enter the deposit amount.
  2. Add the returned amount to the `balance`.
  3. Return the updated `balance`.
---------------------------------
### Algorithm for `withdraw`
- **Purpose**: To subtract a user-specified amount from the current balance and warn if the balance goes negative.
- **Name**: withdraw
- **Parameters**: balance (current account balance)
- **Return**: Updated balance after the withdrawal
- **Algorithm**:
  1. Call `input_amount` with the prompt to enter the withdrawal amount.
  2. Subtract the returned amount from the `balance` and store the result.
  3. If the result is less than 0, print a warning that the balance is negative.
  4. Return the updated `balance`.
---------------------------------
### Algorithm for `input_amount`
- **Purpose**: To get a valid non-negative integer amount from the user.
- **Name**: input_amount
- **Parameters**: prompt (a string to display when asking for input)
- **Return**: Valid non-negative integer amount or 0 if input is invalid
- **Algorithm**:
  1. Display the `prompt` and get user input as `amount`.
  2. If `amount` is not a digit or is less than 0:
     1. Return 0.
  3. Otherwise:
     1. Return the integer value of `amount`.
---------------------------------
### Algorithm for `view_balance`
- **Purpose**: To display the current balance to the user.
- **Name**: view_balance
- **Parameters**: balance (current account balance)
- **Return**: none
- **Algorithm**:
  1. Print the current balance formatted to two decimal places.
---------------------------------
### Algorithm for `main`
- **Purpose**: To manage the program flow, take user input, and call the appropriate functions based on user choices.
- **Name**: main
- **Parameters**: none
- **Return**: none
- **Algorithm**:
  1. Initialize `current_balance` to `INITIAL_BALANCE`.
  2. Initialize `choice` as an empty string.
  3. While `choice` is not equal to `SENTINEL`:
     1. Call `menu` to display options.
     2. Get user input for `choice`, convert to uppercase, and strip whitespace.
     3. If `choice` is 'D':
        1. Call `deposit` and update `current_balance`.
     4. Else if `choice` is 'W':
        1. Call `withdraw` and update `current_balance`.
     5. Else if `choice` is 'V':
        1. Call `view_balance`.
     6. Else if `choice` is 'E':
        1. Print a thanks message.
     7. Else:
        1. Print 'Invalid choice'.
  4. End of the `main` function.
  ---------------------------------