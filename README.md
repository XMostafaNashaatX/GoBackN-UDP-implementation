# Implementation of Go-Back-N Protocol
This project involves the implementation of the Go-Back-N protocol in Python using the socket
programming library. The Go-Back-N protocol is a sliding window protocol that uses a window of
size ‘N’ to send multiple packets at once without waiting for individual acknowledgments.
# Server Side
The server is set up using the socket library. It binds to a specific host and port and waits for
incoming connections from the client.
The server receives the window size from the client and then enters a loop where it continuously
receives data packets from the client. Each packet contains a sequence number and the actual data.
The sequence number is extracted from the first 4 bytes of the packet.
The server also simulates packet loss. It generates a random number and if this number is less than
the packet loss probability, it drops the packet and continues to the next iteration of the loop.
If the packet is not dropped, the server increments the acknowledgment number and checks if the
sequence number is equal to the window size minus one. If it is, the server sends an
acknowledgment back to the client and increases the window size.
The server writes the received data (excluding the sequence number) to a file. This process
continues until a special packet with a sequence number of 9999 is received, indicating the end of
the transmission.
# Client Side
The client also uses the socket library to set up a UDP socket. It sends the window size to the
server and then enters a loop where it reads data from a file and sends it to the server.
The client maintains a sequence number for each packet it sends. Each packet consists of the
sequence number followed by the actual data. The sequence number is incremented for each
packet.
The client uses a try/except block to handle timeouts. It sends a packet to the server and waits for
an acknowledgment. If an acknowledgment is not received within a certain timeout period, it prints a
message and resends the packet.
The client also checks if the acknowledgment number is equal to the window size minus one. If it is,
it prints a message indicating that all packets in the window have been sent.
This process continues until all data has been read from the file and sent to the server. The client
then sends a special packet with a sequence number of 9999 to indicate the end of the
transmission.
# Error Handling
Errors are handled using the try/except block in the client code. If a packet is not acknowledged
within the timeout period, a socket. Timeout exception is raised. The client catches this exception
and resends the packet.

On the server side, packet loss is simulated using a random number generator. If a packet is
dropped, the server simply continues to the next iteration of the loop without sending an
acknowledgment. This causes the client to timeout and resend the packet.
# Implementation of Go-Back-N
The Go-Back-N protocol is implemented using a sliding window mechanism. The client sends
multiple packets at once without waiting for individual acknowledgments. The server acknowledges
the receipt of all packets up to a certain sequence number, which effectively acknowledges all
preceding packets as well.
If a packet is lost or an error occurs, the client resends all packets starting from the last
unacknowledged packet. This is the “go back” part of the Go-Back-N protocol. The size of the
window ‘N’ determines how many packets can be sent at once and how far the client can “go back”
in case of an error.
In conclusion, this project successfully implements the Go-Back-N protocol using Python’s socket
programming library. It demonstrates the use of UDP sockets, error handling, and the sliding window
mechanism for reliable data transmission over an unreliable network.
