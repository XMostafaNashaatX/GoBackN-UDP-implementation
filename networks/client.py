
import socket
host = "127.0.0.1"
port = 8080
addr = (host, port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
seq_n = 0
tail = 9999
window = 7
win = 7
client.sendto(win.to_bytes(4, 'big'), addr)
with open("medium file.jpeg", 'rb') as img:

  while True:
      if seq_n < window:
        chunk = img.read(4096)
        if not chunk:
            data = tail.to_bytes(4, 'big')
            client.sendto(data, addr)
            break
        data = seq_n.to_bytes(4, 'big')+chunk
        try:
            client.sendto(data, addr)
            client.settimeout(5)
            if seq_n == window - 1:
                print(f"{window} packets where sent")

            if seq_n == window - 1:
                window = window + win
                ack, server = client.recvfrom(4096)
                ack_n= int.from_bytes(ack, 'big')
                print(f"received ACK:{ack_n} from {server}")
            seq_n = seq_n + 1
            continue
        except socket.timeout:
            print("ack not received resending packet")

      if ack_n != seq_n + 1:
          window = window - win
          continue
