# prgram to generate random number

# Test case - 1
# -----------------------------
# input:
# lb = 10
# ub = 20

# output:
# Generated number : 12
# first we need to import module called random to use a method called randint

import random

# As randint module has two parameters user need to specify two boundaries to get a number with in the range 
lb = int(input("Enter Lower boundary : "))
ub = int(input("Enter Upper boundary : "))

output = random.randint(lb,ub) 

print("Generated number : ",output)