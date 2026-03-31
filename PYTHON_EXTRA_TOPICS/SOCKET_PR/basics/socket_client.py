import socket

c =  socket.socket()

# here we are connecting the client socket to the server socket using the connec() function that takes the two arguments , the first one is the address of the server and the second one is the port number on which the server is listening for the connections. In this example, we are connecting to the server running on the localhost and listening on the port number 9999.
c.connect(('localhost',9999))

# here we are going to take the name of the user as input from the client side and then we will send the name of the user to the server side using the send() function of the client socket object. The send() function takes the argument as the message that we want to send to the server and we need to encode the message before sending it to the server because the send() function only accepts the bytes-like objects and the encode() function is used to convert the string into bytes-like objects.
name = input("enter your name : ")
c.send(name.encode('utf-8'))


# here we wangt to recieve the message from the server side so will going to use the recv() function of the client socket object which takes the argument as the buffer size that we want to recieve from the server. The recv() function will return the message that we have recieved from the server side and we need to decode the message before printing it becz the recv() function returns the message in bytes-like format and the decode() function is used to convert the byts like  objects into string format.abs
message_server = c.recv(1024)
print("message from the server is ",message_server.decode('utf-8'))