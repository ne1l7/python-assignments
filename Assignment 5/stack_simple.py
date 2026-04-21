class SimpleStack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop_item(self):
        if len(self.data) == 0:
            print("Empty")
            return None
        return self.data.pop()

s = SimpleStack()
s.push(5)
s.push(10)
print(s.pop_item())
