'''

2 layers of network service 
1.  At a low level, you can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.

2. libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP, and so on.

3 . Socket
What is Sockets?
Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.

Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest.

3.1 type 
The type of communications between the two endpoints, typically SOCK_STREAM for connection-oriented protocols tcp and SOCK_DGRAM for connectionless protocols udp 

3.2 hostname
The identifier of a network interface − A string, which can be a host name, a dotted-quad address, or an IPV6 address in colon (and possibly dot) notation

3.3 port
Each server listens for clients calling on one or more ports. A port may be a Fixnum port number, a string containing a port number, or the name of a service.

3.4 create a socket 
use the socket.socket() function available in socket module, which has the general syntax
Once you have socket object, then you can use required functions to create your client or server program.

- s.bind()
 binds address (hostname, port number pair) to socket.
- s.listen()
 sets up and start TCP listener.
- accept()
  accept TCP client connection, waiting until connection arrives (blocking).

3.5  clinet socket
s.connect()

This method actively initiates TCP server connection.

3.6 other methods
s.recv()

This method receives TCP message

s.send()

This method transmits TCP message

s.recvfrom()

This method receives UDP message

s.sendto()

This method transmits UDP message

s.close()

This method closes socket

socket.gethostname()
'''

####A Simple Server
## socket object -----<Create> ---> socket server ---<bind a host and port > --> put socket server on a host
##<accpet> -- to wait a client connection --< return a conn> -- set up a conn b/w server and client 

import socket               # Import socket module
import glob




#if __name__=='__main__':
def server():
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1'#socket.gethostname() # Get local machine name
    port = 12359
    s.bind((host, port))        # Bind to the port
    #hostname = (s.getsockname()[0]) # get the socket host name
    #portnumber = s.getsockname()[1]
    s.listen(5)                 # Now wait for client connection.
    glob.Client.num =10
    while True:

        glob.setClientNum()
        if glob.getClientNum()>= 15:
            break
        con, addr = s.accept()     # Establish connection with client.
        #Accept a connection. The socket must be bound to an address and listening for connections.
        #The return value of socket.accept() is a pair (conn, address) where conn is a new socket object usable to send and receive 
        #data on the connection, and address is the address bound to the socket on the other end of the connection.
        print ('Got connection from', addr)
        con.send(b'Thank you for connecting')
        print('this is the ', glob.getClientNum(), ' conn')
        con.close()                # Close the connection

        

if __name__ =='__main__':
    server()
