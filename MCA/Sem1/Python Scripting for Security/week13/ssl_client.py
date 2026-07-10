import socket
import ssl

def main():
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 4443))

    # SSL context
    context = ssl.create_default_context()
    ssl_sock = context.wrap_socket(sock, server_hostname='localhost')

    print("Connected to SSL server")

    try:
        # Send message
        ssl_sock.send(b"Hello from client!")

        # Receive response
        response = ssl_sock.recv(1024)
        print(f"Response: {response.decode()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssl_sock.close()

if __name__ == "__main__":
    main()
