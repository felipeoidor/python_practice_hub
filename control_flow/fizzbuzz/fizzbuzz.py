def main():

    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number.")    

    for a in range(1, n+1):
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        elif a % 3 == 0: 
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)

if __name__ == "__main__":
    main()