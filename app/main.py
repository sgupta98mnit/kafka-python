import socket  # noqa: F401
import struct


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket, _ = server.accept() # wait for client

    req_data = client_socket.recv(1024)
    message_size = struct.unpack(">i", req_data[0:4])[0]
    req_api_key = struct.unpack(">h", req_data[4:6])[0]
    req_api_version = struct.unpack(">h", req_data[6:8])[0]
    req_correlation_id = struct.unpack(">i", req_data[8:12])[0]


    print(f"Client connected: {_}")

    message_size = struct.pack(">i", 0)
    res_correlation_id = struct.pack(">i", req_correlation_id)
    error_code = struct.pack(">h", 35)

    client_socket.sendall(message_size + res_correlation_id + error_code)

    client_socket.close()


if __name__ == "__main__":
    main()
