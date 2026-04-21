try:
    x = int("abc")
    y = 1/x
except ValueError:
    print("Wrong value")
except ZeroDivisionError:
    print("Zero issue")
