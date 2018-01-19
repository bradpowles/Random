import time
start = time.time()
for num in range(1,100001):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            # print(num)
            break
end = time.time() - start
print(end)