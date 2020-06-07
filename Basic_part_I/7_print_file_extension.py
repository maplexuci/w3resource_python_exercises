# Write a Python program to accept a filename from the user
# and print the extension of that.


file_name = input("Please input a file name with extension: ")

file_name = file_name.split('.')
print(file_name[-1])
