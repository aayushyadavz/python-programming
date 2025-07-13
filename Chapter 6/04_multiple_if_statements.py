age = int(input("Enter a valid age: "))

# if statement number 1
if(age%2 == 0):
    print("Age is even.")
# end of if statement number 1

# if statement number 2
if(age >= 18):
    print("You are above the age of consent.")

elif(age < 0):
    print("You are entering an invalid negative age.")

elif(age == 0):
    print("You are entering 0 which is not a valid age.")

else:
    print("You are below the age of consent.")
# end of if statement number 2

print("End of Program!")