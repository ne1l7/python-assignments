name = input("Enter file: ")
try:
    f = open(name, "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File missing")
