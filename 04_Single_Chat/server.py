import socket

IP='127.0.0.1'
PORT=12345


def printMessage(address,data):
	print(f'{address[0]} : {address[1]} ----> {data}')

def main():
	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.bind((IP,PORT))
	serverSocket.listen(9)

	while True:
		clientConnection,address=serverSocket.accept()

		while True:

			#receive data from Client
			data=clientConnection.recv(2048)
			data=data.decode("utf-8")
			if data=="q" or data=="quit":
				break
	
			else:
				printMessage(address,data)
				#read the message from user to reply
				reply=input("Enter the message to reply or q to quit : ")
				if reply=='q' or reply=='quit':
					break
				#send it back to client
				clientConnection.send(bytes(reply,"utf-8"))
		break
	serverSocket.close()


main()
