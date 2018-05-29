import struct

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_reader import PacketReader


class AgentPacket(Packet):

	def __init__(self):
		Packet.__init__(self)
		self.SERVER_ID = 0
		self.FLAG = 0
		self.REQ_ID = 0

	def get_header_size(self):
		# SERVER_ID, FLAG, REQ_ID, HEADER, VER, DATA_LENGTH
		header_size = 1 + 1 + 4 + 4 + 3 + 4
		return header_size

	def get_server_id(self):
		return self.SERVER_ID

	def get_flag(self):
		return self.FLAG

	def get_request_id(self):
		return self.REQ_ID

	def send(self, socket, data):

		try:
			b_send = bytearray()
			b_send.extend(struct.pack("!b", self.SERVER_ID))
			b_send.extend(struct.pack("!b", self.FLAG))
			b_send.extend(struct.pack("!i", self.REQ_ID))
			b_send.extend(bytes(self.HEADER, "utf-8"))
			b_send.extend(bytes(self.VER, "utf-8"))
			b_send.extend(struct.pack("!i", len(data)))
			b_send.extend(data)
			b_send.extend(bytes(self.TAIL, "utf-8"))

			print(b_send)

			socket.send(b_send)
		except Exception as e:
			raise e


	def recv(self, socket):

		header_size = self.get_header_size()
		data_size = self.recv_header(socket)

		if data_size > -1:
			data = socket.recv(data_size + 4)
			tail = bytes(struct.unpack_from("!4s", data, data_size)[0]).decode()

			if tail != self.TAIL:
				raise TypeError("Error packet. invalid tail - %s" % tail)

			return PacketReader().parse_to_msg(data)

		return Message("DEFAULT")

	def recv_header(self, socket):
		header_size = self.get_header_size()
		header_data = socket.recv(header_size)

		try:
			self.SERVER_ID = struct.unpack_from("!b", header_data, 0)[0]
			self.FLAG = struct.unpack_from("!b", header_data, 1)[0]
			self.REQ_ID = struct.unpack_from("!i", header_data, 2)[0]

			header = bytes(struct.unpack_from("!4s", header_data, 6)[0]).decode()

			if header != self.HEADER:
				raise TypeError("Error packet. invalid header - %s" % header)

			self.VER = bytes(struct.unpack_from("!3s", header_data, 10)[0]).decode()
			data_size = struct.unpack_from("!i", header_data, 13)[0]

			return data_size

		except Exception as e:
			raise e

		return -1




