name = "aayush yadav"

print(len(name)) # 12
print(name.endswith("sh")) # False
print(name.count("a")) # 4
print(name.capitalize()) # Aayush yadav
print(name.find("yadav")) # 7
print(name.replace("aayush", "anvesh")) # anvesh yadav

# Note: Strings are immutable, which means we cannot change the original string by modifying it directly or by running functions on it. Any operation that appears to modify a string actually creates and returns a new string.