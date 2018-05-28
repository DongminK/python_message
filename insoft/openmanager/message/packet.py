import socket
import struct

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet_reader import PacketReader


class Packet:

	def __init__(self):
		self.SERVER_ID = 0
		self.FLAG = 0
		self.REQ_ID = 0
		self.HEADER = "INOM"
		self.VER = "100"
		self.TAIL = "MONI"

	def get_header_size(self):
		# SERVER_ID, FLAG, REQ_ID, HEADER, VER, DATA_LENGTH
		header_size = 1 + 1 + 4 + 4 + 3 + 4
		return header_size

	def send(self, data):
		pass

	def recv_header(self, socket):
		header_size = self.get_header_size()
		header_data = socket.recv(header_size)

		try:
			self.SERVER_ID = struct.unpack_from("!B", header_data, 0)[0]
			self.FLAG = struct.unpack_from("!B", header_data, 1)[0]
			self.REQ_ID = struct.unpack_from("!I", header_data, 2)[0]

			header = bytes(struct.unpack_from("!4s", header_data, 6)[0]).decode()

			if header != self.HEADER:
				raise TypeError("Error packet")

			self.VER = bytes(struct.unpack_from("!3s", header_data, 10)[0]).decode()
			data_size = struct.unpack_from("!I", header_data, 13)[0]

			return data_size

		except:
			pass
		finally:
			pass

		return -1

	def recv(self, socket):
		data_size = self.recv_header(socket)

		if data_size > -1:
			data = socket.recv(data_size)
			return PacketReader(data).parse_to_msg()

		return Message("DEFAULT")


