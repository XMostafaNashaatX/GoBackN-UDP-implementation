import socket
import random
host = "127.0.0.1"
port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
server.bind(server_address)
ack = 0
win, address = server.recvfrom(5000)
window = int.from_bytes(win, 'big')
with open('received image.jpeg', 'wb') as img:
    packet_loss_probability = 0.0
    while True:
        data, address = server.recvfrom(5000)
        if data:
            if int.from_bytes(data,'big') == 9999:
                print(int.from_bytes(data, 'big'))
                break
            if random.random() < packet_loss_probability:
                print(f"Packet with sequence number {int.from_bytes(data[:4], 'big')} dropped!")
                continue
            seq_n = int.from_bytes(data[:4], 'big')
            if seq_n == window-1:
                print(f"recived {window} packets")
                ack = ack+int.from_bytes(win, 'big')
                sent = server.sendto(ack.to_bytes(4, 'big'), address)
                print(f"sent {sent} bytes back to {address}")
                print(f"received packet with sequence number:{seq_n}")
                window = window+int.from_bytes(win, 'big')
            img.write(data[4:])