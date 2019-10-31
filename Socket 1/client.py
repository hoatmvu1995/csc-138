from socket import*

serverName = 'sp3'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')

clientSocket.send(sentence.encode())
modifiedMessage = clientSocket.recv(1024)

print('From Server', modifiedMessage.decode())

clientSocket.close()
