class calculator:
    function = 'Carry out calculations.'
    def add(self):
        number = 1
        return number


def setup():
    f = open('programs.json', 'a')
    f.write(str(calculator)+'\n')

