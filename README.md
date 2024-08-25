# Simple Lightweight Math Server (STMS) - README

## Overview

The Simple Lightweight Math Server (STMS) is a basic server application designed to perform mathematical operations using the `bc` command-line calculator. The server listens for incoming client connections, evaluates mathematical expressions received from clients, and sends back the results.

## Features

- **Mathematical Operations:** Supports basic arithmetic operations (`+`, `-`, `*`, `/`), comparisons (`==`), and exponentiation (`^`).
- **Multi-threading:** Utilizes threading to handle input and output simultaneously for each client connection.
- **Validation:** Checks incoming data against a regular expression to ensure it conforms to valid mathematical expressions or commands.
- **Client Management:** Maintains a list of connected clients and prevents multiple connections from the same IP address.

## Requirements

- Python 3.x
- `bc` command-line calculator (usually available on Unix-like systems)

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the `bc` utility if it's not already installed:
   - On Debian-based systems: `sudo apt-get install bc`
   - On Red Hat-based systems: `sudo yum install bc`

## Usage

1. Save the provided Python code into a file named `stms_server.py`.

2. Run the server script using Python:
   ```bash
   python stms_server.py
   ```

3. The server will start and listen on port `8989`. You can connect to it using a client that can send text over TCP, such as `telnet` or `netcat`.

4. Once connected, you can enter mathematical expressions or commands, and the server will process them using `bc`.

## Code Explanation

### Key Components

- **Math_thread_stdout:** A thread that continuously reads the output of the `bc` process and sends it to the client.
- **Math_thread_stdin:** A thread that handles input from the client, validates it, and writes it to the `bc` process.
- **Main Server Loop:** Listens for incoming client connections and manages multiple clients using the threading model.

### Regular Expressions

The server uses the following regular expression to validate incoming data:
```python
pattern = r"([0-9]{1,4}\s*==\s*[0-9]{1,4})|([0-9]{1,4}\s*[\+\-\*\<\>\^\=/]\s*[0-9]{1,4})|([a-z]+\s*[\+\-\*\<\>\^\=/]\s*[0-9]{1,4})|([a-z]+\s*[\+\-\*\<\>\^\=/]\s*[a-z]+)|([a-z]+\s*==\s*[a-z]+)"
```
This pattern checks for valid arithmetic expressions, comparisons, and simple variable manipulations.

### Error Handling

- **Invalid Syntax:** The server responds with a message if the received data does not match the expected pattern.
- **Connection Issues:** Handles broken connections and sends appropriate error messages.

## Known Issues

- **Connection Management:** The current implementation only allows one connection per IP address. Improvements can be made to handle multiple connections more gracefully.

## Future Improvements

- Support for more complex mathematical functions and expressions.
- Improved error handling and logging.
- Enhanced client management to support multiple connections from the same IP address.


## Author

Sridharanitharan.B

Feel free to modify and enhance this server according to your needs!
