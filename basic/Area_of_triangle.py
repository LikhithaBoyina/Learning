# Python program to calculate area of triangle

# Test case - 1
# --------------------------------------
# input:
# base = 6
# height = 8
# output:
# Area of triangle with base 6 and height 8 is 24

# Take base and height inputs from the user

base = int(input("Enter lenght of the base : "))
height = int(input("Enter height of the trainge : "))

# formula for area of triangle is (1/2*base*height)

# store the value in a variable called areaoftriangle

areaoftriangle = (0.5*base*height)
print("Area of triangle with base %d and height %d is %d"%(base,height,areaoftriangle))