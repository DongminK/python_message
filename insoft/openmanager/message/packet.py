import socket
import struct

class Packet:

	def __init__(self):
		self.SERVER_ID = 0
		self.FLAG = 0
		self.REQ_ID = 0
		self.HEADER = "INOM"
		self.VER = "100"
		self.TAIL = "MONI"

	def send(self, data):
		pass

	def recv(self, data, sock:socket):
		print(sock.recv(10000))

		self.SERVER_ID = struct.unpack_from("!B", data, 0)[0]
		self.FLAG = struct.unpack_from("!B", data, 1)[0]
		self.REQ_ID = struct.unpack_from("!I", data, 2)[0]

		print(self.SERVER_ID)
		print(self.FLAG)
		print(self.REQ_ID)
		try:
			header = bytes(struct.unpack_from("!4s", data, 6)[0]).decode()

			if header != self.HEADER:
				pass

			self.VER = bytes(struct.unpack_from("!3s", data, 10)[0]).decode()
			self.DATA_LENGTH = struct.unpack_from("!I", data, 13)[0]
		except:
			pass
		finally:
			pass


	pass
