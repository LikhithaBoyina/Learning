# Function to know the number is even or odd

#TestCase-1
# ------------------------------------------
# Enter a number : 5
# output:
# 5 is odd number

def Even_Or_Odd(n): # here n is the parameter of the function
    if(n%2 == 0): #condition to check n is even or odd 
        print("%d is even number "%(n)) # if the condition is true prints this statement
    else:
        print("%d is odd number "%(n)) # else condition is false prints this statement

# main function 
        
def main():
    number = int(input("Enter a number : "))
    Even_Or_Odd(number)

if __name__=="__main__": 
    main()