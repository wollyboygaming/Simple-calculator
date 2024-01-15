# This Function adds Two Numbers Together

def add(x , y): 
    return  x + y

# This Funtion Subracts (Takes Away) Two Numbers

def Subract(x,y):
    return  x - y 

# This Funtion Multiplies (Times) two numbers

def Multiplies(x,y):
    return  x * y 

# This Funtion Divides two Numbers 

def Divide(x,y):
     return x / y 

print ("Select Operation you would Like to Do")
print ("Select 1 for Plus (Addition) ")
print("Select 2 for Subtraction (Take away)")
print ("Select 3 For multiplication (Multiply)")
print ("Select 4 For Division (divide)")

while True:
# This Part Takes the Answer From the User 
    choice = input ("Enter The Number Of Your Wanted Operation Here:   ")

# This Checks if the Numbers 1-4 are selected
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter First Number"))
            num2 = float(input("Enter Second Number"))
        except ValueError:
            print ("Invalid Number. Select A number from the Options Above")
            continue
        if choice == '1':
            print (num1, "+", num2, "=", add(num1, num2))
            
        
        elif choice == '2':
            print (num1, '-' ,num2, "=", add(num1,num2))


        elif choice == "3":
            print (num1, "*", num2, "=", Multiplies(num1, num2))


    elif choice == "4":
            
     print (num1, "/", num2, "=", Divide(num1, num2))
            


# Check If the End User wants to Do more calculations
# Break Loop if They Want to stop
     
     next_calculation = input ("Do You want to Solve Another Problem?  (Yes/No): ")

     if next_calculation == "no":
         break
     
     else:
         print ("Invalid Answer")

