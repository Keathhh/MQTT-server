import socket

host = '127.0.0.1'
port = 11344
buffer_size = 1024

def send_and_receive(msg):
    # Create a new socket and connect for each message
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(msg.encode('ascii'))  # Send the message to the server
    data = client_socket.recv(buffer_size)   # Receive data from the server

    client_socket.close()  # Close the socket after receiving the response
    return data.decode('ascii')

while True:
    message = input("Enter message here: ")  # Get message from user input
    if message.lower() == "exit":  # Allow user to exit the loop
        break
    response = send_and_receive(message)
    print(f"{response}")