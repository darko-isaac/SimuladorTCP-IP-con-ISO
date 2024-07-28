import socket


def create_iso_message():
    # Crear un mensaje ISO 8583 simplificado
    mti = "0200".ljust(4, ' ')
    pan = "1234567890123456".ljust(16, ' ')
    processing_code = "000000".ljust(6, ' ')
    amount = "000000000001".ljust(12, ' ')
    date_time = "2407241230".ljust(10, ' ')

    return mti.encode('ascii') + pan.encode('ascii') + processing_code.encode('ascii') + amount.encode(
        'ascii') + date_time.encode('ascii')


def send_message(host='127.0.0.1', port=65432):
    message = create_iso_message()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message)


if __name__ == "__main__":
    send_message()
