# Python program to check if year is a leap year or not

#testcase-1
#------------------------------------------------
# Enter a year: 2000
# Output:
# 2000 is a leap year

#leap year function
def leapyear(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print("%d is a leap year"%(year))

 
    elif (year % 4 ==0) and (year % 100 != 0):
        print("%d is a leap year"%(year))

    else:
        print("%d is not a leap year"%(year))

def main():
    year = int(input("Enter a year: "))
    leapyear(year) #function call

if __name__=="__main__": 
    main()