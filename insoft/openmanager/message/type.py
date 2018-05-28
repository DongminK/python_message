class _MessageType:

	INTEGER = 2
	FLOAT = 3
	LONG = 4
	STRING = 5
	BYTES = 7
	MESSAGE = 8
	ARRAY = 10

	def __setattr__(self, key, value):
		pass


class _PacketType:

	INTEGER = bytes("I", "utf-8")
	FLOAT = bytes("F", "utf-8")
	LONG = bytes("L", "utf-8")
	STRING = bytes("S", "utf-8")
	BYTES = bytes("B", "utf-8")
	COMPLEX = bytes("C", "utf-8")
	ARRAY = bytes("V", "utf-8")

	def __setattr__(self, key, value):
		pass



