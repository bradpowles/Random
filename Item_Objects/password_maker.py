class password_maker:
    function = 'Make Passwords.'
    def password(self):
        number = 1
        return number


def setup():
    f = open('programs.csv', 'a')
    f.write(str(password_maker)+'\n')

