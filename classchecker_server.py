from socket import *
from datetime import datetime

HOST = gethostname()
PORT = 4444
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

def signToFile(studentid):

    now = datetime.now().strftime("%Y-%m-%d|%H:%M:%S")

    f = open('signed_student.txt', 'a')
    f.write(str(now)+'|'+studentid+'\n')
    f.close()

def findID(studentid):

    f = open('signed_student.txt', 'r')

    while True:
        s = f.readline()
        data = s.rstrip().split('|');
        
        if s == '':
            return False

        if data == None:
            return False
        elif data[2] == studentid:
            client.send(str.encode(data[2] + ' is already signed at ' + data[0] + ' ' + data[1]))
            return True

while True:
    print('Waitng for connection...')
    client, address = server.accept()
    print('Connected: ', address)

    client.send(str.encode('\n> Student Class Checker v0.1a'))

    while True:
        accept_menu = bytes.decode(client.recv(BUFFER_SIZE)).lower()

        if not accept_menu:
            print('Server> Client Disconnected!')
            client.close()
            break

        elif accept_menu == 's':
            studentid = bytes.decode(client.recv(BUFFER_SIZE))

            if findID(studentid) == False:
                signToFile(studentid)
                client.send(str.encode('ok'))
                print('Server> #', studentid, 'just sign to the class!')
            else:
                client.send(str.encode('This ID is already signed!'))
                print('Server> #', studentid, 'tried to re-signed!')

        elif accept_menu == 'c':

            studentid = bytes.decode(client.recv(BUFFER_SIZE))
            print('Server> #', studentid, 'is checking status!')
            
            if findID(studentid) == False:
                client.send(str.encode('Not Found!'))

        else:
            print(accept_menu)
            client.send(str.encode('Server> Client is using wrong operation..'))


    

            


