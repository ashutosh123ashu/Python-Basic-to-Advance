# WA function to find max of three

def max(num1, num2, num3):
    if(num1>num2):
        max = num1
    else:
        max = num2
    
    if(num3>max):
        print("Maximim is: ",num3)
    else:
        print("Maximum is: " , max)
    
max(123,45,92)

# WAP to convert degree celcius to farenheight.

def farh(cel):
    return (cel*(9/5)) + 32

c = 25
f = farh(c)

print("Farenheight temperature is " + str(f))