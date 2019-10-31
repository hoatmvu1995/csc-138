#import socket module
from socket import *

#provide server port number
serverPort = 8100
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket
serverSocket.bind(('', serverPort))

#listen for the connection
serverSocket.listen(1)


while True:
	#establish the connection
	print("Ready to serve...")

	#create a connection socket for accepted client
	connectionSocket, addr = serverSocket.accept()


	try:
		#receive the message
		message = connectionSocket.recv(1024)

		#print the message
		print(message)

		#determine the file name
		filename = message.split()[1]

		#open the file 
		f = open(filename[1:])

		#read the file
		outputdata = f.read()

		#send http header to the socket
		connectionSocket.send("""HTTP/1.1 200 OK""".encode())

		#provide the requested file that the client try to GET to the socket
		connectionSocket.send('HelloWorld.html'.encode())

		#send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())

		connectionSocket.close()

	except IOError:
		#Send response message for file not found
		connectionSocket.send("""\n404 Not Found\n""".encode())

		#close the client socket
		connectionSocket.close()

#close the server socket
serverSocket.close()
