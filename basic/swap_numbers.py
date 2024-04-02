# Program to swap two numbers

# Test Case-1
# -------------------------------------------------
# a = 5
# b = 6

# Output:
# Before swapping :
# a = 4
# b = 5
# After swapping :
# a = 5
# b = 4


a = int(input("Enter number : "))
b = int(input("Enter another number : "))

print("Before swapping : ")
print("a = %d \nb = %d"%(a,b))

# to swap number we need a temeporary variable to hold number of a variable until it get swaped

temp = a # from right to left number in variable a is placed in temporary variable temp
a = b # from right to left number in variable b is placed in a variable
b = temp # now the number in a is swaped to b using temp variable

print("After swapping : ")
print("a = %d \nb = %d"%(a,b))


