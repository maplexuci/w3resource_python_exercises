# Write a Python program that accepts an integer (n)
# and computes the value of n+nn+nnn


# Method 1

def cal_rep_nums(nums):
    double = str(nums)*2
    triple = str(nums)*3

    double = int(double)
    triple = int(triple)

    return nums + double + triple


print(cal_rep_nums(5))


# Method 2

a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1+n2+n3)
