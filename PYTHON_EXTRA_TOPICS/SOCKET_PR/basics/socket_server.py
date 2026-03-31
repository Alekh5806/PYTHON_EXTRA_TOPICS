import socket 
import encodings
# here we are creating the socket object using the socket() function of the socket module. The socket() function takes two arguments, the first one is the address family and the second one is the socket type. The address family can be either AF_INET for IPv4 or AF_INET6 for IPv6. The socket type can be either SOCK_STREAM for TCP or SOCK_DGRAM for UDP. In this example, we are creating a TCP socket using the AF_INET address family and the SOCK_STREAM socket type.
s = socket.socket()
print("socket created successfully")

# we can use any port number ranges between 0 to 65535 but the port number between 0 to 1023 are reserved for the well-known services like http,ftp,ssh etc. so we can use the port number above 1023 for custom applications.
s.bind(('localhost',9999))

ip = socket.gethostbyname('localhost')
print("the ip address of the server is ",ip)


# listen for the connections from the client using the listen() function of the socket object which takes the argument as the number of connections that we want to allow in the queue. In this example, we are allowing 3 connections in the queue. The listen() function will put the server socket in the listening state and it will wait for the client to connect to the server socket. Once the client is connected to the server socket, the listen() function will return the client socket object and the address of the client. The listen() function will also allow the server to accept multiple connections from the clients and it will put the incoming connections in the queue until the server is ready to accept them. If the queue is full and a new client tries to connect to the server socket, then the client will receive an error message indicating that the connection was refused.
s.listen(3)
print("waiting for the connections")

# for accepting the connection from the client we will going to use the while loop and accept() function of the socket object which will going to wait for the client to connect and once the client is connected it willl return the client socket object and the address of the client.
while True:
  c , addr = s.accept()
  name = c.recv(1024).decode('utf-8')
  print("client connected with the address", addr , name)
  
  # here we are sending the welcome message to the client using the send() function of the client socket object. The send() function takes the argument as the message that we want to send to teh client and we need to encode the message before sending it to the client because the send() sunction only accepts the bytes-like objects and the encode() function is used to convert the string into bytes-leke objects.
  message = "welcome to the socket programming created by Alekh"
  c.send(message.encode('utf-8'))
  c.close()

