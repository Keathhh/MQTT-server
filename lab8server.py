import socket

# Define the server address (host and port)
server_address = ('localhost', 12345)  # Change this to your desired host and port

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind(server_address)

# Protocol function to parse the incoming packet and construct a response
def parse_and_construct_response(data):
    data = data.decode('utf-8')
    if data.startswith("TNE20003:"):
        header, message = data.split(":", 1)
        if message:
            response = f"TNE20003:{message}"
        else:
            response = "TNE20003:E: Invalid message. Must have at least one character"
    else:
        response = "TNE20003:E:Invalid message format. Must have TNE20003: at the beginning"
    
    return response

while True:
    print("Waiting for incoming packets...")
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received packet from {client_address}: {data.decode('utf-8')}")

    # Parse the incoming packet and construct a response
    response = parse_and_construct_response(data)

    # Send the response back to the client
    server_socket.sendto(response.encode('utf-8'), client_address)
    print(f"Sent response to {client_address}: {response}")

server_socket.close()
