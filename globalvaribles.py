class GlobalMem:
    pass

GlobalMem.a = 10

def func():
    print(GlobalMem.a)

func()
