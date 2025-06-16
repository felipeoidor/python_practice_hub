# Create a list of squares of even numbers from 1 to 10 using list comprehension
squares = [x**2 for x in range(1,11) if x % 2 == 0]
# Prints the resulting list
print(squares) 