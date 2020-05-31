# Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.


# Method 1: use function

def print_name(first, last):
    print(last + ' ' + first)


print_name('Lily', 'Kite')


# Method 2: use input()

first_name = input("Your First Name: ")
last_name = input("Your Last Name: ")
print("Hello, " + last_name + " " + first_name)
