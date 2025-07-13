marks = {
    "ayush": 100,
    "zubia": 50,
    "deepu": 23,
    0: "ayush"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"ayush": 99, "harsh": 20}) # Updates the value of 'ayush' and adds a new key-value pair 'harsh': 20
# print(marks)

print(marks.get('ayush')) # 100
print(marks.get('ayush2')) # None
# V/S 
print(marks['ayush']) # 100
# print(marks['ayush2']) # error

print(len(marks)) # 4