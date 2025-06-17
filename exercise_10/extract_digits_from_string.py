# String containing letters and numbers
text = "abc123def45gh6"

# Use list comprehension with .isdigit() to filter digits and convert them to integers
digits = [int(x) for x in text if x.isdigit()]

# Print the resulting list of integers
print(digits)