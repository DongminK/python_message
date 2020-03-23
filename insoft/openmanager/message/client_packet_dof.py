import struct

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_reader import PacketReader


class DofClientPacket(Packet):

	def __init__(self):
		Packet.__init__(self)
		self.HEADER = "INOM"
		self.VER = "40"
		self.INDEX = 1
		self.LIMIT = 0
		self.TAIL = "MONI"
		self.SESSION_ID = 0
		self.REQ_ID = 0

	def get_header_size(self):
		# HEAD, VERSION, INDEX, LIMIT, SESSION_ID, REQUEST_ID, DATA_LENGTH
		header_size = 4 + 2 + 1 + 1 + 4 + 4 + 4
		return header_size
	
	def get_head(self):
		return self.HEADER

	def get_version(self):
		return self.VER

	def get_session_id(self):
		return self.SESSION_ID

	def get_request_id(self):
		return self.REQ_ID

	def send(self, socket, data):

		try:
			b_send = bytearray()
			b_send.extend(bytes(self.HEADER, "utf-8"))
			b_send.extend(bytes(self.VER, "utf-8"))
			b_send.extend(struct.pack("!b", self.INDEX))
			b_send.extend(struct.pack("!b", self.LIMIT))
			b_send.extend(struct.pack("!i", self.SESSION_ID))
			b_send.extend(struct.pack("!i", self.REQ_ID))
			b_send.extend(struct.pack("!i", len(data)))
			b_send.extend(data)
			b_send.extend(bytes(self.TAIL, "utf-8"))

			socket.send(b_send)
		except Exception as e:
			raise e


	def recv(self, socket):

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

			header = bytes(struct.unpack_from("!4s", header_data, 0)[0]).decode()
			# bytes(struct.unpack_from("!2s", header_data, 4)[0]).decode() # Version
			self.INDEX = struct.unpack_from("!b", header_data, 6)[0]
			self.LIMIT = struct.unpack_from("!b", header_data, 7)[0]
			self.SESSION_ID = struct.unpack_from("!i", header_data, 8)[0]
			self.REQ_ID = struct.unpack_from("!i", header_data, 12)[0]

			if header != self.HEADER:
				raise TypeError("Error packet. invalid header - %s" % header)

			data_size = struct.unpack_from("!i", header_data, 16)[0]

			return data_size

		except Exception as e:
			raise e

		return -1




