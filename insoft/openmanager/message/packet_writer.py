import struct

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.type import _PacketType, _MessageType


class PacketWriter:

	def __init__(self):
		self.b_data = bytearray()
		self.packet_type = _PacketType()
		self.msg_type = _MessageType()

	def write_sig(self, sig):
		self.b_data.extend(sig)

	def write_int(self, value):
		b_int = struct.pack("!i", value)
		self.b_data.extend(b_int)

	def write_str(self, str):
		b_str = bytes(str, "utf-8")
		b_len = len(b_str)

		self.write_int(b_len)
		self.b_data.extend(b_str)

	def write_float(self, value):
		b_float = struct.pack("!f", value)
		self.b_data.extend(b_float)

	def write_long(self, value):
		b_long = struct.pack("!q", value)
		self.b_data.extend(b_long)

	def write_byte(self, value):
		b_len = len(value)
		self.write_int(b_len)
		self.b_data.extend(value)

	def parse_to_bytes(self, msg):
		self.write_msg(msg)
		return self.b_data

	def write_msg(self, msg):

		self.write_sig(self.packet_type.COMPLEX)
		self.write_int(msg.get_field_size())
		self.write_sig(self.packet_type.STRING)
		self.write_str(msg.get_name())

		fields = msg.get_fields()

		for field in fields:
			self.write_sig(self.packet_type.STRING)
			self.write_str(field)

		for field in fields:
			field_type = msg.get_type(field)

			if field_type == self.msg_type.INTEGER:
				self.write_sig(self.packet_type.INTEGER)
				self.write_int(msg.get_int(field))
			elif field_type == self.msg_type.FLOAT:
				self.write_sig(self.packet_type.FLOAT)
				self.write_float(msg.get_float(field))
			elif field_type == self.msg_type.LONG:
				self.write_sig(self.packet_type.LONG)
				self.write_long(msg.get_long(field))
			elif field_type == self.msg_type.STRING:
				self.write_sig(self.packet_type.STRING)
				self.write_str(msg.get_str(field))
			elif field_type == self.msg_type.MESSAGE:
				self.write_msg(msg.get_msg(field))
			elif field_type == self.msg_type.ARRAY:
				self.write_sig(self.packet_type.ARRAY)
				self.write_array(msg.get_array(field))

	def write_msg_value(self, msg):

		fields = msg.get_fields()

		for field in fields:
			field_type = msg.get_type(field)

			if field_type == self.msg_type.INTEGER:
				self.write_sig(self.packet_type.INTEGER)
				self.write_int(msg.get_int(field))
			elif field_type == self.msg_type.FLOAT:
				self.write_sig(self.packet_type.FLOAT)
				self.write_float(msg.get_float(field))
			elif field_type == self.msg_type.LONG:
				self.write_sig(self.packet_type.LONG)
				self.write_long(msg.get_long(field))
			elif field_type == self.msg_type.STRING:
				self.write_sig(self.packet_type.STRING)
				self.write_str(msg.get_str(field))
			elif field_type == self.msg_type.MESSAGE:
				self.write_msg(msg.get_msg(field))
			elif field_type == self.msg_type.ARRAY:
				self.write_sig(self.packet_type.ARRAY)
				self.write_array(msg.get_array(field))


	def write_array(self, array):
		len_array = len(array)
		self.write_int(len_array)

		if len_array > 0:
			arr_value = array[0]
			arr_type = self.packet_type.INTEGER

			if type(arr_value) == int:
				for value in array:
					if value > 0x7fffffff:
						arr_type = self.packet_type.LONG

						if value > 0x7fffffffffffffff:
							raise TypeError("Value is bigger than LONG MAX VALUE - " + str(value))

						break

				self.write_sig(arr_type)

				for value in array:
					if arr_type == self.packet_type.INTEGER:
						self.write_int(value)
					else:
						self.write_long(value)

			elif type(arr_value) == float:
				self.write_sig(self.packet_type.FLOAT)
				for value in array:
					self.write_float(value)
			elif type(arr_value) == str:
				self.write_sig(self.packet_type.STRING)
				for value in array:
					self.write_str(value)
			elif type(arr_value) == Message:

				self.write_sig(self.packet_type.COMPLEX)
				field_size = arr_value.get_field_size()

				if len_array > 1:
					last_msg = array[int(len_array - 1)]
					last_msg_field_size = last_msg.get_field_size()

					if field_size < last_msg_field_size:
						if len_array > 2:
							mid_msg = array[int(len_array / 2)]
							if last_msg_field_size < mid_msg.get_field_size():
								arr_value = mid_msg
								field_size = arr_value.get_field_size()
							else:
								arr_value = last_msg
								field_size = last_msg_field_size
						else:
							arr_value = last_msg
							field_size = last_msg_field_size
					elif last_msg_field_size < field_size and 2 < len_array:
						mid_msg = array[int(len_array / 2)]

						if field_size < mid_msg.get_field_size():
							arr_value = mid_msg
							field_size = arr_value.get_field_size()
						else:
							arr_value = last_msg
							field_size = last_msg_field_size

				self.write_int(field_size)
				self.write_sig(self.packet_type.STRING)
				self.write_str(arr_value.get_name())

				fields = arr_value.get_fields()

				for field in fields:
					self.write_sig(self.packet_type.STRING)
					self.write_str(field)

				for value in array:
					self.write_msg_value(value)

			elif type(arr_value) == array:
				self.write_sig(self.packet_type.ARRAY)
				for value in array:
					self.write_array(value)









