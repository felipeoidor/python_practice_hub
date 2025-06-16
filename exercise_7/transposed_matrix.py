# Transpose matrix with for
# Create matrix
matrix = [[9,5,1],
          [7,6,1],
          [8,3,5]]

# Create a new list to store the transposed matrix
transposed = []

# Transpose the matrix
for i in range(len(matrix[0])):
    # Create a new list to store each row of the transposed matrix
    transposed_row = []
    # Iterate over the rows of the original matrix
    for row in matrix:
        transposed_row.append(row[i])
    # Add the transpose row to the new matrix
    transposed.append(transposed_row)   

# Print result
print("With for:\n"
      f"-Matrix: {matrix}\n"
      f"-Transposed Matrix: {transposed}")

# Transpose matrix with list comprehension

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Print result
print("With list comprehension:\n"
      f"-Matrix: {matrix}\n"
      f"-Transposed Matrix: {transposed}")