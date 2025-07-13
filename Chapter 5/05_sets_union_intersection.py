s1 = {1, 45, 6, 78}
s2 = {1, 65, 78, 5}

print(s1.union(s2)) 
# Union: combines all elements from both sets, removing duplicates → {1, 65, 5, 6, 45, 78}

print(s1.intersection(s2)) 
# Intersection: returns only the elements common to both sets → {1, 78}