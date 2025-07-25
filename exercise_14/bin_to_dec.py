binary = input("Enter a binary number: ")

binary_list = [int(bit) for bit in binary[::-1]]
exponents = range(len(binary))

decimal_value = 0
for bit, exponent in zip(binary_list,exponents):
    decimal_value += bit * (2 ** exponent)
    
print(f"The binary number {binary} equals {decimal_value} in decimal.")