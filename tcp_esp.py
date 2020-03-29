# import socket
# import sys
import netifaces as ni
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

ni.ifaddresses('wlp6s0')
ip = ni.ifaddresses('wlp6s0')[ni.AF_INET][0]['addr']
print (ip)  # should print "192.168.100.37"
print (type(ip))  # should print "192.168.100.37"
# # Bind the socket to the port
# server_address = (ip, 8090)
# print (sys.stderr, 'starting up on %s port %s' % server_address)
# sock.bind(server_address)


# # Listen for incoming connections
# sock.listen(1)

# while True:
# 	# Wait for a connection
# 	print(sys.stderr, 'waiting for a connection')
# 	connection, client_address = sock.accept()
# 	try:
# 		print (sys.stderr, 'connection from', client_address)

# 		# Receive the data in small chunks and retransmit it
# 		while True:
# 			data = connection.recv(1024)
# 			print(sys.stderr, 'received "%s"' % data)
# 			if not data:
# 				break
# 			# if data:
# 			# 	print (sys.stderr, 'sending data back to the client')
# 			# 	connection.sendall(data)
# 			# else:
# 			# 	print (sys.stderr, 'no more data from', client_address)
# 			# 	break
# 	finally:
# 		connection.close()

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("{} wrote:".format(self.client_address[0]))
        print (self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = ip, 8090
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()