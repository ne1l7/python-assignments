print("3.1 Tuple Creation")
tup = (2, 4, 6, 8, 10)
print("Tuple:", tup)

print("Element at index 2:", tup[2])
print("Slice (1 to 3):", tup[1:4])

print("\n3.2 Nested Tuple")
nt = (10, 20, (30, 40), 50)
print("Nested Tuple:", nt)
print("Access inner element:", nt[2][0])

print("\n3.3 Repetition")
rep = tup * 3
print("Repeated:", rep)

print("\n3.4 Concatenation")
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenated:", t3)