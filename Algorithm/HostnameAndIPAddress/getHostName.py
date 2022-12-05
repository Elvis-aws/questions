
import ipaddress
import socket




def getHostName():
    hostName = socket.gethostname()
    ipAddre = socket.gethostbyname(hostName)
    print('HostAddress is',ipAddre)

getHostName()