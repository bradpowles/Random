import os
read = []
for file in os.listdir("."):
    if file.endswith("here.py") and file not in read:
        exec("import " + file[:-3] + '\n' + file[:-3] + ".setup()")
    read.append(file)

# mobs.json in the future
class mobs:
    types = []
# end

print(mobs.types[0].weaknesses)