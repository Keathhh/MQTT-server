import socket

host = '127.0.0.1'
port = 11344
buffer_size = 1024

# Use SOCK_STREAM for TCP
server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_soc.bind((host, port))
server_soc.listen(5)  # Listen for up to 5 pending connection requests



def process_message(data):
    if data.startswith("TNE20003:"):
        print("Message received from:", client_address)
        return f"A:{data}"
    elif data == "":
        return "TNE20003:E: No messages received"
    else:
        return "TNE20003:E: Invalid header information"

print("TCP server is waiting for connections...")


while True:
    client_socket, client_address = server_soc.accept()  # Accept a client connection
    data = client_socket.recv(buffer_size)  # Receive data from the connected client
    data_decoded = data.decode('ascii')
    response = process_message(data_decoded)
    client_socket.send(response.encode('ascii'))  # Send the response to the connected client
    client_socket.close()  # Close the client socket after sending the response