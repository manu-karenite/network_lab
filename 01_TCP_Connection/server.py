import socket

IP='127.0.0.1'
PORT=12345


def main():
	#creating a socket
	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.bind((IP,PORT))
	#making TCP Socket listen to 10 connections at time
	serverSocket.listen(10)

	while True:
		#making socket accept from TCP Connection

		client,address=serverSocket.accept()
		print(f'The Client Connected is {address[0]} and on Port No. {address[1]}')
		break
if __name__=="__main__":
	main()
