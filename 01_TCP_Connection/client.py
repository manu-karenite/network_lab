import socket

IP='127.0.0.1'
PORT=12345

def main():
	clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	clientSocket.connect((IP,PORT))

main()
