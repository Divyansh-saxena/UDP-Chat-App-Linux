import socket
protocol = socket.SOCK_DGRAM
addressFam = socket.AF_INET
print("Waiting for the msg")
s = socket.socket(addressFam,protocol)
s.bind(("192.168.0.11",5005))
msg = s.recvfrom(1024)
print(msg)

#input and then 
# s.sendto( b"data" , ( ip , port ))
