import socket
import threading
import os

# Constants for HTTP status codes
HTTP_OK = 200
HTTP_NOT_FOUND = 404

# Constants for content types
CONTENT_TYPE_HTML = 'text/html'
CONTENT_TYPE_PLAIN = 'text/plain'

# Directory to serve files from
SERVE_DIRECTORY = 'public'

def handle_request(client_socket):
    # Receive the client's request
    request = client_socket.recv(1024).decode('utf-8')
    
    # Extract the HTTP method and path
    request_lines = request.split('\n')
    first_line = request_lines[0].split()
    method = first_line[0]
    path = first_line[1]
    
    # Extract headers
    headers = {}
    for line in request_lines[1:]:
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    
    # Handle GET requests
    if method == 'GET':
        file_path = os.path.join(SERVE_DIRECTORY, path.lstrip('/'))
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                content = file.read()
            status_code = HTTP_OK
            content_type = CONTENT_TYPE_HTML if file_path.endswith('.html') else CONTENT_TYPE_PLAIN
        else:
            content = b'404 Not Found'
            status_code = HTTP_NOT_FOUND
            content_type = CONTENT_TYPE_PLAIN
    else:
        content = b'Method Not Supported'
        status_code = 405
        content_type = CONTENT_TYPE_PLAIN
    
    # Prepare the HTTP response
    response = f"HTTP/1.1 {status_code}\r\n"
    response += f"Content-Type: {content_type}\r\n"
    response += f"Content-Length: {len(content)}\r\n"
    response += "\r\n"
    
    # Send the response headers
    client_socket.sendall(response.encode())
    
    # Send the content
    client_socket.sendall(content)
    
    # Close the client socket
    client_socket.close()

def main():
    # Create a server socket
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server is running on http://localhost:4221")
    
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        
        # Handle the client request in a new thread
        client_thread = threading.Thread(target=handle_request, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
