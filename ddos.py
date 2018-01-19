import threading, os

class ddos:
    ip = ''

    def __init__(self):
        pass

    def dos(self, ip):
        os.system('ping {}'.format(ip))
        pass

    def run(self):
        for i in range(1, 4):
            cThread = threading.Thread(target=self.dos, args=(self.ip))
            cThread.start()

ddos.ip = '192.168.0.1'
ddos().run()
