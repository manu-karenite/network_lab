import socket


IP='127.0.0.1'
PORT=12345

def main():
	outgoing=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	outgoing.connect((IP,PORT))
	data=input("Print Enter the message : ")
	outgoing.send(bytes(data,"UTF-8"))
	

main()
