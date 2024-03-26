# Python program to calculate area of triangle

# Take base and height inputs from the user

base = int(input("Enter lenght of the base : "))
height = int(input("Enter height of the trainge : "))

# formula for area of triangle is (1/2*base*height)

# store the value in a variable called areaoftriangle

areaoftriangle = (0.5*base*height)
print("Area of triangle with base %d and height %d is %d"%(base,height,areaoftriangle))