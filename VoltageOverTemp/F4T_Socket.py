import socket

# the public network interface
HOST = "172.16.52.26"
PORT = 5025
# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send(b'*iDN?')
print(s.recv(1024))
