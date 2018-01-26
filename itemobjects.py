import os

moblist = []

for file in os.listdir("./Item_Objects"):
    if file.endswith(".py"):
        moblist.append(file)


class mobs:
    types = []
    pass
########

class mobnamegoeshere:
    weaknesses = ['Tom Bell']
    def magicalpowers(self):
        number = 1
        return number

def setup():
    mobs.types.append(mobnamegoeshere)

######
mobnamegoeshere()

print(mobs.types[0].weaknesses)