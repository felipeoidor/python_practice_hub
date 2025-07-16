def binary_system(user):
    if user >= 2:
        binary_system(user//2)
        print(user%2, end="")
    else:
        print(user, end="")


while True:
    try:

        user = int(input("Please introduce a number: "))
        print(f"The binary representation of {user} is ", end="")
        binary_system(user)
        break

    except ValueError:
        print("Please enter a number in decimal system. Try again.")