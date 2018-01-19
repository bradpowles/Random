class GlobalMem:
    a = 6
    def __init__(self):
        self.a = 7

    def something(self):
        print(self.a)

GlobalMem().something()

