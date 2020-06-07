# Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.


value = input("Please give some comma seperated numbers: ")

ls = value.split(',')
tup = tuple(ls)

print(ls, tup)
