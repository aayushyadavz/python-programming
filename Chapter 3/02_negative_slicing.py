name = "Ayush"

print(name[-4:-2]) # yu
# Equivalent positive indexing for the above:
print(name[1:3]) # yu

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])

# (ii) Slicing with skip value:
a = "0123456789"
print(a[1:7:3])  
# [1:7] means start from index 1 (inclusive) to index 7 (exclusive)
# The string from index 1 to 6 is "123456"
# [1:7:3] means take every 3rd character starting from index 1
# So it will pick index 1 ('1') and index 4 ('4')
# Output: "14"

b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:9:4])
