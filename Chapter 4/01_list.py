friends = ["Ayush", "Zubia", 5, 5.6, False, "Harsh"]

print(friends[0]) # Ayush

# Note: Unlike strings, lists are mutable:
friends[0] = "Prajjwal" 
print(friends) # ['Prajjwal', 'Zubia', 5, 5.6, False, 'Harsh']

print(friends[1:3]) # ['Zubia', 5]