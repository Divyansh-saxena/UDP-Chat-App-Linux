import socket

print(''' **********************************************************
 ************* Panshi: The New Era !!***********************
 ***********************************************************''')

protocol = socket.SOCK_DGRAM
addFam = socket.AF_INET
s = socket.socket( addFam, protocol)

rip = input("Enter REVCEIVER IP...>>> ")
rport = int(input("Enter REVCEVER revceving port...>>> "))
s.bind(('192.168.0.35',1321))
send = 0 
data1 = ''

def datasender():
    data = input("Enter the Message to be Send...>>> ")
    s.sendto( data.encode(), (rip,rport))
    return data

def datareceiver():
    x = s.recvfrom(1024)
    print(x[0].decode()+' : '+x[1][0])
    if 'exit' ==  data1:
        print (send)
        return 1

while (send != 1):
    data1 = datasender()
    send = datareceiver()
