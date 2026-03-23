print("2.1 Set Creation")
set1 = {1, 2, 3, 4, 5}
print("Set1:", set1)

print("Elements in Set:")
for i in set1:
    print(i, end=" ")
print()

print("\n2.2 Union")
set2 = {4, 5, 6, 7}
print("Set2:", set2)

union = set1 | set2
print("Union:", union)

print("\n2.3 Intersection")
inter = set1 & set2
print("Intersection:", inter)

print("\n2.4 Difference")
diff1 = set1 - set2
print("Set1 - Set2:", diff1)

diff2 = set2 - set1
print("Set2 - Set1:", diff2)