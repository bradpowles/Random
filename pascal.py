import math


def alpha(n, r):
    list=[1]
    for i in range(n):
        print(list)
        if len(list) == n:
            print(list[r])
        newlist=[]
        newlist.append(list[0])
        for i in range(len(list)-1):
            newlist.append(list[i]+list[i+1])
        newlist.append(list[-1])
        list=newlist


def beta(n, r):
    nf = math.factorial(n)
    rf = math.factorial(r)
    nrf = math.factorial((n-r))
    out = rf*nrf
    out = nf/out
    print(out)

beta(1000, 100)