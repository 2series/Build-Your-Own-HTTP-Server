import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Create a server socket
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        
        # Receive the client's request (we're not using it in this stage)
        client_socket.recv(1024)
        
        # Prepare the HTTP response
        response = "HTTP/1.1 200 OK\r\n\r\n"
        
        # Send the response to the client
        client_socket.sendall(response.encode())
        
        # Close the client socket
        client_socket.close()


if __name__ == "__main__":
    main()
