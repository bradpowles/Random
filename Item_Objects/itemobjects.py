import os
read = []
for file in os.listdir("."):
    if file.endswith("r.py") and file not in read:
        exec("import " + file[:-3] + '\n' + file[:-3] + ".setup()")
    read.append(file)

# mobs.json in the future
class programs:
    types = []
# end

for i in programs.types:
    print('-----')
    print(i)
    print(i.function)
    print('-----')