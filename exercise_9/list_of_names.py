# List of names
names = ["alice", "Bob", "Charlie", "david", "Eve"]

# New list with names in uppercase, only if they start with a capital letter
uppercase_name = [x.upper() for x in names if x[0].isupper() ]

# print result
print(uppercase_name)