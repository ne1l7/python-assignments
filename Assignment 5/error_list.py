a = ["10", "abc", 30]

try:
    total = int(a[0]) + int(a[1])
    print(total)
except ValueError:
    print("Conversion error")
except:
    print("Some error")
