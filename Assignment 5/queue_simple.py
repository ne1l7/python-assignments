class SimpleQueue:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def remove(self):
        if len(self.data) == 0:
            print("Queue empty")
            return None
        return self.data.pop(0)

q = SimpleQueue()
print("Queue demo")
q.add(10)
q.add(20)
print(q.remove())
