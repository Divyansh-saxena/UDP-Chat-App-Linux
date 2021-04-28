import socket
import os 
import threading
import time


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

print(''' **********************************************************
 ****************** Start Messaging ************************
 ***********************************************************''')

def datasender():
    send = True
    while (send is not False):
        os.system('tput setaf 6')
        data = input("Enter the Message to be Send...>>> ")
        s.sendto( data.encode(), (rip,rport))
        if data == 'exit':
            send = False
            exit()
        time.sleep(1)

def datareceiver():
    send = True
    while (send is not False):
        x = s.recvfrom(1024)
        os.system('tput setaf 5')
        print('\n\t\t\t'+x[1][0]+' : '+x[0].decode())
        if 'exit' ==  x[0].decode():
            send = False
            exit()
        time.sleep(1)
            
thr1 = threading.Thread(target=datasender)
thr2 = threading.Thread(target=datareceiver)

thr1.start()
thr2.start()

os.system('tput setaf 7')
