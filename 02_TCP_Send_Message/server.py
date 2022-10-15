import socket

IP='127.0.0.1'
PORT=12345


def main():
	incoming=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	incoming.bind((IP,PORT))
	incoming.listen(5)

	while True:
		connection,address=incoming.accept()
		print(f"The Client connected is {address[0]} on PORT {address[1]}")
		#receiving data from client
		data=connection.recv(1024)
		data=data.decode("utf-8")
		
		print("Data Received is : ",data)
		break
if __name__=="__main__":
	main()
