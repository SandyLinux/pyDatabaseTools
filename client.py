#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import glob

#if __name__=='__main__':
def client():
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1'#socket.gethostname() # Get local machine name
    port = 12359    # Reserve a port for your service.

    s.connect((host, port))
    print (s.recv(1024).decode('ascii'))
    print(glob.getClientNum())

    s.close()                     # Close the socket when done

if __name__ =='__main__':

    client()
