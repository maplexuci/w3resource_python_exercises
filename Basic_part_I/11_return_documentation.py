# Write a Python program to print the
# documents (syntax, description etc.) of Python built-in function(s)


# Method 1:

def get_doc(fuc):
    return help(fuc)


get_doc(sum)


# Method 2:

def get_doc(fuc):
    print(fuc.__doc__)


get_doc(abs)
