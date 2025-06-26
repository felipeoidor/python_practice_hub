# Create a dictionary for memoization
memo = {}

def fibo(n):

    # If n is already in the dictionary, return the cached result
    if n in memo:
        return memo[n]

    # Base cases: The first two fibonacci numbers (0 and 1)
    if n < 2:
        result = n
    
    # Recursive call to compute the fibonacci number 
    else:
        result = fibo(n-1) + fibo(n-2)
    
    # Stores the result in the dictionary using n as the key
    memo[n] = result
    return memo[n]

# Print the first 100 Fibonacci numbers
for a in range(100):
    print(f"fibo {a}: {fibo(a)}")