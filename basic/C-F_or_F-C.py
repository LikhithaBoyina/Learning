#Program to convert Celsius to Fahrenheit and Fahrenheit to Celsius

#TestCase-1
# ----------------------------------------
# Enter the degree to be converted C or F : F
# Enter temperature value in terms of Farenheit :  4.5
# 4.50 degree Fahrenheit is equal to -15.28 degree Celsius

# Testcase-2
# --------------------------------------------------
# Enter the degree to be converted C or F : C
# Enter temperature value in terms of Celsius :  6.6
# 6.60 degree Celsius is equal to 43.88 degree Farenheit

#function to convert degrees from Celsius to Fahrenheit
def CelsiusToFahrenheit():
    Celsius = float(input("Enter temperature value in terms of Celsius :  "))
    Fahrenheit = (Celsius * 1.8) + 32
    print('%.2f degree Celsius is equal to %.2f degree Farenheit'%(Celsius,Fahrenheit))

# function to covert degrees from Fahrenheit
def FahrenheitToCelsius():
    Fahrenheit = float(input("Enter temperature value in terms of Farenheit :  "))
    Celsius = (Fahrenheit - 32) / 1.8
    print('%.2f degree Fahrenheit is equal to %.2f degree Celsius'%(Fahrenheit,Celsius))
    
def main():
    Degree = input("Enter the degree to be converted C or F : ")
    if(Degree == 'C'):
        CelsiusToFahrenheit()
    else:
        FahrenheitToCelsius()

if __name__=="__main__": 
    main()