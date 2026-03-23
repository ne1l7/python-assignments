print("4.1 Dictionary Creation and Access")
student = {"name": "Bob", "age": 22, "city": "Pune"}
print("Dictionary:", student)

# Access values
print("Name:", student["name"])
print("Age:", student.get("age"))

print("\n4.2 Update Dictionary")
student["age"] = 23
print("Updated Age:", student)

student["course"] = "CSE"
print("Added Course:", student)

print("\n4.3 Delete Elements")
city_removed = student.pop("city")
print("Removed city:", city_removed)
print("After removing city:", student)

del student["name"]
print("After deleting name:", student)

student.clear()
print("After clearing:", student)

print("\n4.4 Combine Dictionaries")
d1 = {"x": 1, "y": 2}
d2 = {"z": 3}

new_dict = d1.copy()
new_dict.update(d2)
print("Combined Dictionary:", new_dict)