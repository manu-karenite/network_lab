import socket

IP='127.0.0.1'
PORT=12346


def solve(data):
	#data is string here
	data=data.split(" ")
	data=[int(x) for x in data if x!=""]
	d={}
	for x in data:
		if x in d:
			d[x]+=1
		else:
			d[x]=1

	s=""
	for x in d:
		s+=str(x)+" : "+str(d[x])+" ;  "
	return s

def main():
	#creating a socket at server side
	
	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.bind((IP,PORT))
	serverSocket.listen(10)


	while True:
		#accept the connection from client
		clientSocket,address=serverSocket.accept()
		print(f'Connected to {address[0]} : {address[1]}')

		#receive data from client
		data=clientSocket.recv(2048)
		data=data.decode("utf-8")
		print("Data Received is ",data)
		#data received is list of numbers
		ans=solve(data)
		#we need to send this answer back to clientSocket
		# we will use the clientSocket
		clientSocket.send(bytes(ans,"utf-8"))
		serverSocket.close()
		break

if __name__=='__main__':
	main()
