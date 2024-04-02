# Python Program to calculate the square root


# Test Case - 1
#----------------------------------------------
# number = 4

# Output:
# The square root of 4 is 2.00

# Take the input from the user
number = int(input('Enter a number: '))

sqrt = number ** 0.5
# Here "** 0.5" number to the power of 0.5 i.e...square root 
print('The square root of %d is %.2f'%(number ,sqrt))
# Finally prints square root of the number with .2 decimal points