# Simple Python HTTP Server

This project is a basic HTTP server implemented in Python. It's designed as a learning exercise to understand the fundamentals of TCP servers, the HTTP protocol, HTTP headers, HTTP verbs, and handling multiple concurrent connections.

## Project Overview

The goal of this project is to build a simple HTTP server capable of:

1. Handling basic GET/POST requests
2. Serving files
3. Managing multiple concurrent connections

## Features

- [x] Bind to a port
- [x] Respond with 200 status code
- [x] Extract URL path
- [x] Respond with body
- [ ] Read headers
- [ ] Handle concurrent connections
- [ ] Return files
- [ ] Read request body
- [ ] HTTP Compression
- [ ] Compression headers
- [ ] Multiple compression schemes
- [ ] Gzip compression

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/2series/build-http-server.git
   cd build-http-server
   ```

### Running the Server

1. Run the server:
   ```
   python http_server.py
   ```

2. The server will start and listen on `localhost:8080` by default.

3. Open a web browser and visit `http://localhost:8080/some/path` to see the server in action.

## Current Functionality

The server currently:
- Binds to a specified port (default: 8080)
- Listens for incoming connections
- Extracts the requested URL path
- Responds with a 200 OK status and a simple text message

## Roadmap

See the [open issues](https://github.com/2series/build-http-server/issues) for a list of proposed features (and known issues).

## Contributing

We welcome contributions to Build Your Own HTTP Server! Here's how you can help:

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

This is a learning project, and we appreciate any contributions, suggestions, and feedback. Please feel free to open an issue or submit a pull request if you'd like to contribute.

## License

This project is open source and available under the [MIT License](LICENSE).