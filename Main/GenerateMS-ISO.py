import socket
import iso8583


def parse_iso_message(data):
    # Decodificar el mensaje usando la biblioteca iso8583
    msg = iso8583.ISO8583()
    msg.unpack(data)
    return msg


def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Servidor escuchando en {host}:{port}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(1024)  # Tamaño del buffer para recibir datos
                    if not data:
                        break
                    iso_message = parse_iso_message(data)
                    print(f"Mensaje recibido: {iso_message}")


if __name__ == "__main__":
    start_server()
