import socket

def handle_request(client_socket):
    # Receive the request data
    request_data = client_socket.recv(1024).decode('utf-8')
    
    # Extract the first line of the request
    first_line = request_data.split('\n')[0]
    
    # Extract the URL path from the first line
    url_path = first_line.split()[1]
    
    # Prepare the response
    response_body = f"Hello! You requested: {url_path}"
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/plain\r\n"
    response += f"Content-Length: {len(response_body)}\r\n"
    response += "\r\n"
    response += response_body
    
    # Send the response
    client_socket.sendall(response.encode('utf-8'))
    
    # Close the client socket
    client_socket.close()

def start_server(host='localhost', port=8080):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Wait for a client connection
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        
        # Handle the client request
        handle_request(client_socket)

if __name__ == "__main__":
    start_server()