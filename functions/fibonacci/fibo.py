memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    elif n < 2:
        return n
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    
    return memo[n]


def main():
    while True:

        try:
            n = int(input("Enter how many Fibonacci numbers to display: "))
            for a in range(n):
                print(f"Fibonacci ({a}) = {fibo(a)}")
            break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()