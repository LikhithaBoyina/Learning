# Program to solve quadratic equation i.e...,ax2+bx+c = 0
a = int(input("Enter 'a' value : "))
b = int(input("Enter 'b' value : "))
c = int(input("Enter 'c' value : "))

d = ((b**2) - (4*a*c))**0.5

# we will have two solutions as follows while solving quadratic equation

sol1 = (-b+d)/2*a
sol2 = (-b-d)/2*a

print("By solving %dx\u00B2+%dx+%d we get "%(a,b,c),sol1,sol2)
# "x\u00B2"  Unicode for superscript 2 (²)