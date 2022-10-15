import socket

IP='127.0.0.1'
PORT=12345

def main():
	clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	clientSocket.connect((IP,PORT))
	while True:
		message=input("Enter the Message or q to quit :  ")
		#send to server

		clientSocket.send(bytes(message,"utf-8"))

		#get data from server
		data=clientSocket.recv(2048)
		data=data.decode("utf-8")
		if data=="q" or data=="quit":
			break
		print("Server ---->",data)

	clientSocket.close()

main()
