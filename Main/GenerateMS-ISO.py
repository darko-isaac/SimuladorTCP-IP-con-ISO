import socket


def parse_iso_message(data):
    # Suponiendo que el mensaje tiene una estructura fija
    mti = data[0:4].decode('ascii')
    pan = data[4:20].decode('ascii').strip()
    processing_code = data[20:26].decode('ascii').strip()
    amount = data[26:38].decode('ascii').strip()
    date_time = data[38:48].decode('ascii').strip()

    return {
        "MTI": mti,
        "PAN": pan,
        "Processing Code": processing_code,
        "Amount": amount,
        "Date and Time": date_time
    }


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
                    data = conn.recv(48)  # Tamaño del buffer basado en el tamaño del mensaje esperado
                    if not data:
                        break
                    iso_message = parse_iso_message(data)
                    print(f"Mensaje recibido: {iso_message}")


if __name__ == "__main__":
    start_server()
