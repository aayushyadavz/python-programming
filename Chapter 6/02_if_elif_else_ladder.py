age = int(input("Enter a valid age: "))

# if elif else ladder:
if(age >= 18):
    print("You are above the age of consent.")

elif(age < 0):
    print("You are entering an invalid negative age.")

elif(age == 0):
    print("You are entering 0 which is not a valid age.")

else:
    print("You are below the age of consent.")

print("End of Program!")