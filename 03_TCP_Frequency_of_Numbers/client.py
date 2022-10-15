import socket



IP='127.0.0.1'
PORT=12346

def main():
	#creating a socket at client side

	clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#CONNECTING WITH THE SERVER SOCKET

	data=input("Please enter your message : ")


	clientSocket.connect((IP,PORT))
	#sending the data

	clientSocket.send(bytes(data,"utf-8"))

	#receive answer from  server
	data=clientSocket.recv(2048)
	data=data.decode("utf-8")
	print(data)
	clientSocket.close()
main()
