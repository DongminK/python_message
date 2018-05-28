import struct

from insoft.openmanager.message.message import Message


class PacketReader:

	def __init__(self, data):
		self.data = data
		self.offset = 0

	def parse_to_msg(self):
		sigs = self.read_signature(self.data, self.offset)
		self.offset = sigs[1]

		return self.read_msg(self.data, self.offset)

	def read_msg(self, data, offset):
		msg_headers = self.read_msg_header(data, offset)

		msg_header = msg_headers[0]
		msg_offset = msg_headers[1]

		msg = Message(msg_header[0])

		for idx, field_name in enumerate(msg_header):

			if idx > 0:
				sigs = self.read_signature(data, msg_offset)
				sig = sigs[0]
				msg_offset = sigs[1]

				if sig == "I":
					rtn_ints = self.read_int(data, msg_offset)
					rtn_int = rtn_ints[0]
					msg_offset = rtn_ints[1]

					msg.set_int(field_name, rtn_int)

				elif sig == "F":
					rtn_floats = self.read_float(data, msg_offset)
					rtn_float = rtn_floats[0]
					msg_offset = rtn_floats[1]

					msg.set_float(field_name, rtn_float)
				elif sig == "L":
					rtn_longs = self.read_long(data, msg_offset)
					rtn_long = rtn_longs[0]
					msg_offset = rtn_longs[1]

					msg.set_long(field_name, rtn_long)
				elif sig == "S":
					rtn_strs = self.read_str(data, msg_offset)
					rtn_str = rtn_strs[0]
					msg_offset = rtn_strs[1]

					msg.set_str(field_name, rtn_str)
				elif sig == "B":
					rtn_bins = self.read_bytes(data, msg_offset)
					rtn_bin = rtn_bins[0]
					msg_offset = rtn_bins[1]

					msg.set_bytes(field_name, rtn_bin)
				elif sig == "C":
					rtn_msgs = self.read_msg(data, msg_offset)
					rtn_msg = rtn_msgs[0]
					msg_offset = rtn_msgs[1]

					msg.set_msg(field_name, rtn_msg)
				elif sig == "V":
					rtn_arrays = self.read_array(data, msg_offset)
					rtn_array = rtn_arrays[0]
					msg_offset = rtn_arrays[1]

					msg.set_array(field_name, rtn_array)

		return msg

	def read_int(self, data, offset):
		rtn_int = (struct.unpack_from("!i", data, offset)[0], offset + 4)
		return rtn_int

	def read_float(self, data, offset):
		rtn_float = (struct.unpack_from("!f", data, offset)[0], offset + 4)
		return rtn_float

	def read_long(self, data, offset):
		rtn_long = (struct.unpack_from("!q", data, offset)[0], offset + 8)
		return rtn_long

	def read_str(self, data, offset):
		str_sizes = self.read_int(data, offset)
		str_size = str_sizes[0]
		str_offset = str_sizes[1]

		rtn_str = (bytes(struct.unpack_from("!" + str(str_size) + "s", data, str_offset)[0]).decode(), str_offset + str_size)
		return rtn_str

	def read_bytes(self, data, offset):
		bin_sizes = self.read_int(data, offset)
		bin_size = bin_sizes[0]
		bin_offset = bin_sizes[1]

		return bytes("")

	def read_array(self, data, offset):
		arr_sizes = self.read_int(data, offset)
		arr_size = arr_sizes[0]
		arr_offset = arr_sizes[1]

		sigs = self.read_signature(data, arr_offset)
		sig = sigs[0]
		arr_offset = sigs[1]

		rtn_value = []

		if sig == 'I':
			for i in range(arr_size):
				int_values = self.read_int(data, arr_offset)
				value = int_values[0]
				arr_offset = int_values[1]

				rtn_value.append(value)
		elif sig == 'F':
			for i in range(arr_size):
				float_values = self.read_float(data, arr_offset)
				value = float_values[0]
				arr_offset = float_values[1]
				rtn_value.append(value)
		elif sig == 'L':
			for i in range(arr_size):
				long_values = self.read_long(data, arr_offset)
				value = long_values[0]
				arr_offset = long_values[1]
				rtn_value.append(value)
		elif sig == 'S':
			for i in range(arr_size):
				str_values = self.read_str(data, arr_offset)
				value = str_values[0]
				arr_offset = str_values[1]
				rtn_value.append(value)
		elif sig == 'C':
			pass
		elif sig == 'V':
			rtn_value.append(self.read_array(data, arr_offset))
			pass

		rtn_array = (rtn_value, arr_offset)
		return rtn_array


	def read_signature(self, data, offset):
		rtn_value = (bytes(struct.unpack_from("!c", data, offset)[0]).decode(), offset + 1)
		return rtn_value


	def read_msg_header(self, data, offset):
		rtn_value = []
		header_sizes = self.read_int(data, offset)

		header_size = header_sizes[0]
		header_offset = header_sizes[1]

		sigs = self.read_signature(data, header_offset)
		header_offset = sigs[1]

		msg_names = self.read_str(data, header_offset)
		msg_name = msg_names[0]
		msg_offset = msg_names[1]

		rtn_value.append(msg_name)

		for i in range(header_size):
			sigs = self.read_signature(data, msg_offset)
			msg_offset = sigs[1]

			field_names = self.read_str(data, msg_offset)
			field_name = field_names[0]
			msg_offset = field_names[1]

			rtn_value.append(field_name)

		rtn_header = (rtn_value, msg_offset)

		return rtn_header

