from temperature import celsius_to_fahrenheit as cf
from temperature import fahrenheit_to_celsius as fc
from temperature import celsius_to_kelvin as ck

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

ch = input("Enter option: ")

if ch == "1":
    temp = float(input("Enter Celsius value: "))
    ans = cf.convert(temp)
    print("Converted to Fahrenheit:", ans)

elif ch == "2":
    temp = float(input("Enter Fahrenheit value: "))
    ans = fc.convert(temp)
    print("Converted to Celsius:", ans)

elif ch == "3":
    temp = float(input("Enter Celsius value: "))
    ans = ck.convert(temp)
    print("Converted to Kelvin:", ans)

else:
    print("Invalid input")