# Import libraries to improve user experience
import time
import os

while True:
    try:
        # Ask the user to enter a positive integer
        user_num = int(input('Please enter a positive integer: '))

        # If the number is greater than 0, calculate the sum and exit the loop
        if user_num > 0:
            # Formula n*(n+1)//2
            sum_of_all = user_num * ( user_num + 1 ) // 2 # Use integer division (//)
            print(f'The sum of all numbers from 1 to {user_num} is {sum_of_all}')
            break
        
        # If the number is less than or equal to 0, prompt the user to enter a new number
        else:
            print('Error: Please enter a positive integer greater than zero.')
            time.sleep(2)
            os.system('clear')

    # If the user enters invalid input (like a string), prompt them to try again
    except ValueError:
        print('Invalid input. Please enter a valid number')
        time.sleep(2)
        os.system('clear')