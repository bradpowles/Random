class Calculator():
    function = 'Carry out calculations.'
    def add(self):
        number = 1
        return number


def setup():
    f = open('programs.csv', 'a')
    f.write(str(Calculator)+'\n')

