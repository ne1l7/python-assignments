print("1.1 List Creation and Access")
numbers = [5, 15, 25, 35, 45]
print("List:", numbers)
print("Element at index 2:", numbers[2])

print("\n1.2 Add and Remove")
numbers.append(55)
print("After append:", numbers)

numbers.insert(1, 10)
print("After insert:", numbers)

numbers.remove(25)
print("After remove:", numbers)

last = numbers.pop()
print("Popped:", last)
print("List now:", numbers)

print("\n1.3 Sorting")
numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

print("\n1.4 Reverse")
numbers.reverse()
print("Reversed:", numbers)