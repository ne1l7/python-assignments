try:
    x = 0
    print(100/x)
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("End")
