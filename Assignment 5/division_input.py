try:
    num = 10
    d = int(input("Enter number: "))
    print(num/d)
except ZeroDivisionError:
    print("Zero not allowed")
except ValueError:
    print("Invalid input")
finally:
    print("Done")
