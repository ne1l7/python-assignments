class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "Age:", self.age)


class Worker(Human):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary

    def show_worker(self):
        self.show()
        print("ID:", self.id, "Salary:", self.salary)


class Boss(Worker):
    def __init__(self, name, age, id, salary, dept):
        super().__init__(name, age, id, salary)
        self.dept = dept

    def show_boss(self):
        self.show_worker()
        print("Department:", self.dept)


while True:
    print("\n1.Human 2.Worker 3.Boss 4.Exit")
    c = input("Choice: ")

    if c == "1":
        n = input("Name: ")
        a = int(input("Age: "))
        obj = Human(n, a)
        obj.show()

    elif c == "2":
        n = input("Name: ")
        a = int(input("Age: "))
        i = input("ID: ")
        s = float(input("Salary: "))
        obj = Worker(n, a, i, s)
        obj.show_worker()

    elif c == "3":
        n = input("Name: ")
        a = int(input("Age: "))
        i = input("ID: ")
        s = float(input("Salary: "))
        d = input("Dept: ")
        obj = Boss(n, a, i, s, d)
        obj.show_boss()

    else:
        break