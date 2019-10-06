from socket import *

ClientM = gethostname()
HOST = gethostname()
PORT = 4444
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
messageFromServer = bytes.decode(server.recv(BUFFER_SIZE))
print(messageFromServer)

def showMenu():
    print('\n# Menu')
    print('# [S] Sign your Student ID into the class')
    print('# [C] Check your status')
    print('# Empty to exit program')
    print('\n')

while True:

    showMenu()

    menu = input('Action: ')
    server.send(str.encode(menu))

    if menu == 's':
        studentid = input('Your student ID: ')
        server.send(str.encode(studentid))

        if bytes.decode(server.recv(BUFFER_SIZE)) == 'ok':
            print('\n' + '> Signed successfully' + '\n')
        else:
            print('\n' + bytes.decode(server.recv(BUFFER_SIZE)) + '\n')

        input('Enter to back to menu..')

    if menu == 'c':
        print('\n# Check your signed status')
        studentid = input('> Student ID: ')
        server.send(str.encode(studentid))
        print('\n' + bytes.decode(server.recv(BUFFER_SIZE)) + '\n')

        input('Enter to back to menu..')

    elif not menu:
        break

server.close()
print('Exiting...')
