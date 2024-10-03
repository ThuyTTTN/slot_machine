MAX_LINES = 3 #constant value that will not change


#collect user's deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():    #valid whole number
            amount = int(amount)    #want to make sure the amount is converted to integer
            if amount > 0:
                break #if amount > 0, then break out of the 'while' loop and returns the 'amount'
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount        

# ask number of lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():    #valid whole number
            lines = int(lines)    #want to make sure the amount is converted to integer
            if 1 <= lines <= MAX_LINES:
                break #if 1 <= lines <= MAX_LINES, then break out of the 'while' loop and returns the 'get number of lines'
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines  


# ask how much to bet on each line 


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
    
main()