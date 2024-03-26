# prgram to generate random number
# first we need to import module called random to use a method called randint

import random

# As randint module has two parameters user need to specify two boundaries to get a number with in the range 
a = int(input("Enter Lower boundary : "))
b = int(input("Enter Upper boundary : "))

c = random.randint(a,b)

print("Generated number : ",c)