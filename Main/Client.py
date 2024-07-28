import socket
import iso8583


def create_iso_message():
    # Crear un mensaje ISO 8583
    msg = iso8583.ISO8583()

    # Configurar el MTI y los campos
    msg.setMTI("0200")
    msg.set(2, "1234567890123456")  # PAN
    msg.set(3, "000000")  # Processing Code
    msg.set(4, "000000000001")  # Amount
    msg.set(7, "2407241230")  # Date and Time

    # Empaquetar el mensaje para enviar
    return msg.pack()


def send_message(host='127.0.0.1', port=65432):
    message = create_iso_message()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message)


if __name__ == "__main__":
    send_message()
