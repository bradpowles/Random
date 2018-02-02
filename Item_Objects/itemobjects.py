import os
read = []
f = open('programs.json', 'w')
for file in os.listdir("."):
    if file.endswith("r.py") and file not in read:
        exec("import " + file[:-3] + '\n' + file[:-3] + ".setup()")
    read.append(file)

# programs.json interpreter
class programs:
    def __init__(self):
        self.program = []
        for line in open('programs.json', 'r'):
            self.program.append(line)
    def all(self):
        return self.program

# end

for i in programs().all():
    print('-----')
    print(i)
    print(eval(i).function)
    print('-----')