num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"Greatest number is {num1}") 

elif(num2>num1 and num2>num3 and num2>num4):
    print(f"Greatest number is {num2}")

elif(num3>num1 and num3>num2 and num3>num4):
    print(f"Greatest number is {num3}")

elif(num4>num1 and num4>num2 and num4>num3):
    print(f"Greatest number is {num4}")