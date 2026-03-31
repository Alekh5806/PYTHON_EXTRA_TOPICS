import socket 

# Create Sockets 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now bind it with the ip and the port we want to use 
server.bind(('0.0.0.0',5000))

# listen for the connections 
server.listen(1)
print("server is waiting for the connections....")

# now accept the connection as it return the client socket  and the client address 
conn , addr = server.accept()
print("connected with ",addr)

#this will be the buffer to store the incoming data until we get a full line with filename and filesize   
buffer = ""
# we will keep receiving data until we get the "END" signal from the client which indicates that all files have been sent

while True:
    while "\n" not in buffer:
        data = conn.recv(1024).decode()
        if not data:
            break
        buffer += data

    if not buffer:
        break

    if "\n" not in buffer:
        continue

    file_info, buffer = buffer.split("\n", 1)

    if file_info.strip() == "END":
        break

    filename, filesize = file_info.split("|")
    filesize = int(filesize)

    print(f"Receiving {filename} of size {filesize} bytes")

    with open("received_" + filename, "wb") as f:
        received = 0
        while received < filesize:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            received += len(data)

    print(f"{filename} received successfully!")

conn.close()
server.close()
