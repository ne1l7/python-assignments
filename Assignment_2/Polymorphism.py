class Transport:
    def run(self):
        print("Transport is moving")

class Bike(Transport):
    def run(self):
        print("Bike is running")

class Bus(Transport):
    def run(self):
        print("Bus is moving")

# Polymorphism
t = [Bike(), Bus()]

for i in t:
    i.run()