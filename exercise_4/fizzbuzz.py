# Print numbers from 1 to 100
for num in range(1,101):

    # If num is divisible by both 3 and 5, print "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')    

    # If num is divisible by 5, print "Buzz"
    elif num % 5 == 0:
        print('Buzz')
    
    # If num is divisible by 3, print "Fizz"
    elif num % 3 == 0:
        print('Fizz')
    
    # If none of the above, just print num 
    else:
        print(num)