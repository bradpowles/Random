import os

def isConnected():
    if os.system("ping 8.8.8.8") == 0:
        return True
    else:
        return False

print(isConnected())
