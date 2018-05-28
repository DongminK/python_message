import copy
import sys

from insoft.openmanager.message.type import _MessageType


class Message:

	def __init__(self, name):
		self.NAME = name
		self.TYPE = _MessageType()
		self.map_value = {}
		self.map_type = {}
		self.INDENT = "    "
		self.DEPTHS = 1

	def set_name(self, name):
		self.NAME = name

	def get_name(self):
		return self.NAME

	def get_field_size(self):
		return len(self.map_value.keys())

	def get_fields(self):
		return self.map_value.keys()

	def get_type(self, field):
		return self.map_type.get(field)

	def set_int(self, key, value):

		if type(value) == int:
			self.map_value[key] = value
			self.map_type[key] = self.TYPE.INTEGER
		else:
			raise TypeError("Not integer type value : " + str(value))

	def get_int(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.INTEGER:
			return -sys.maxsize - 1

		key_value = self.map_value.get(key)

		if key_value == None:
			return -sys.maxsize - 1

		return key_value

	def get_int_def(self, key, defValue):

		if type(defValue) != int:
			raise TypeError("Not integer type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.INTEGER:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value


	def set_float(self, key, value):

		if type(value) == float:
			self.map_value[key] = value
			self.map_type[key] = self.TYPE.FLOAT
		else:
			raise TypeError("Not float type value : " + str(value))

	def get_float(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.FLOAT:
			return -sys.float_info.max -1

		key_value = self.map_value.get(key)

		if key_value == None:
			return -sys.float_info.max - 1

		return key_value

	def get_float_def(self, key, defValue):

		if type(defValue) != float:
			raise TypeError("Not float type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.FLOAT:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value


	def set_long(self, key, value):

		if type(value) == int:
			self.map_value[key] = value
			self.map_type[key] = self.TYPE.LONG
		else:
			raise TypeError("Not long type value : " + str(value))

	def get_long(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.LONG:
			return -sys.maxsize - 1

		key_value = self.map_value.get(key)

		if key_value == None:
			return -sys.maxsize - 1

		return key_value

	def get_long_def(self, key, defValue):

		if type(defValue) != int:
			raise TypeError("Not long type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.LONG:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value


	def set_str(self, key, value):

		if type(value) == str:
			self.map_value[key] = value
			self.map_type[key] = self.TYPE.STRING
		else:
			raise TypeError("Not string type value : " + str(value))

	def get_str(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.STRING:
			return ""

		key_value = self.map_value.get(key)

		if key_value == None:
			return ""

		return key_value

	def get_str_def(self, key, defValue):

		if type(defValue) != str:
			raise TypeError("Not string type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.STRING:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value


	def set_msg(self, key, value):

		if type(value) == Message:
			self.map_value[key] = value
			self.map_type[key] = self.TYPE.MESSAGE
		else:
			raise TypeError("Not message type value : " + str(value))

	def get_msg(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.MESSAGE:
			return Message("DEFAULT")

		key_value = self.map_value.get(key)

		if key_value == None:
			return Message("DEFAULT")

		return key_value

	def get_msg_def(self, key, defValue):

		if type(defValue) != Message:
			raise TypeError("Not message type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.MESSAGE:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value


	def set_array(self, key, value):

		if type(value) == list:

			if len(value) > 0:
				value_type = type(value[0])

				for val in value:
					if type(val) != value_type:
						raise TypeError("Not different array type value : " + str(value))

			self.map_value[key] = value
			self.map_type[key] = self.TYPE.ARRAY
		else:
			raise TypeError("Not array type value : " + str(value))

	def get_array(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.ARRAY:
			return []

		key_value = self.map_value.get(key)

		if key_value == None:
			return []

		return key_value

	def get_array_def(self, key, defValue):

		if type(defValue) != list:
			raise TypeError("Not array type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.ARRAY:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value


	def set_bytes(self, key, value):

		if type(value) == bytes:
			self.map_value[key] = value
			self.map_type[key] = self.TYPE.BYTES
		else:
			raise TypeError("Not bytes type value : " + str(value))

	def get_bytes(self, key):

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.BYTES:
			return bytes(0)

		key_value = self.map_value.get(key)

		if key_value == None:
			return bytes(0)

		return key_value

	def get_bytes_def(self, key, defValue):

		if type(defValue) != bytes:
			raise TypeError("Not bytes type value : " + str(defValue))

		key_type = self.map_type.get(key)

		if key_type == None or key_type != self.TYPE.BYTES:
			return defValue

		key_value = self.map_value.get(key)

		if key_value == None:
			return defValue

		return key_value

	def remove(self, key):
		key_value = self.map_value.get(key)

		if key_value != None:
			del self.map_value[key]
			del self.map_type[key]

	def to_string(self, depth):
		self.DEPTHS = depth
		return self.__repr__()

	def __repr__(self):

		msg_fmt = self.NAME + " {\n"

		keys = list(self.map_value.keys())
		keys.sort()

		for key in keys:

			for depth in range(0, self.DEPTHS):
				msg_fmt += self.INDENT

			key_type = self.map_type.get(key)

			if key_type == self.TYPE.INTEGER:
				msg_fmt += "I) " + key + " = " + str(self.map_value.get(key))
			elif key_type == self.TYPE.FLOAT:
				msg_fmt += "F) " + key + " = " + str(self.map_value.get(key))
			elif key_type == self.TYPE.LONG:
				msg_fmt += "L) " + key + " = " + str(self.map_value.get(key))
			elif key_type == self.TYPE.STRING:
				msg_fmt += "S) " + key + " = " + self.map_value.get(key)
			elif key_type == self.TYPE.BYTES:
				msg_fmt += "B) " + key + " = " + str(self.map_value.get(key))
			elif key_type == self.TYPE.MESSAGE:
				msg_fmt += "M) " + key + " = " + self.map_value.get(key).to_string(self.DEPTHS + 1)
			elif key_type == self.TYPE.ARRAY:

				len_array = len(self.map_value.get(key))

				if len_array == 0:
					msg_fmt += "A) " + key + " = ?:0) [ ]"
				else:
					arr = self.map_value.get(key)
					if type(arr[0]) == int:
						msg_fmt += "A) " + key + " = I:" + str(len_array) + ") " + str(arr)
					elif type(arr[0]) == float:
						msg_fmt += "A) " + key + " = F:" + str(len_array) + ") " + str(arr)
					elif type(arr[0]) == str:
						msg_fmt += "A) " + key + " = S:" + str(len_array) + ") " + str(arr)
					elif type(arr[0]) == bytes:
						msg_fmt += "A) " + key + " = B:" + str(len_array) + ") " + str(arr)
					elif type(arr[0]) == Message:
						msg_fmt += "A) " + key + " = M:" + str(len_array) + ") [\n"
						for idx, msg_arr in enumerate(arr):

							for depth in range(0, self.DEPTHS + 1):
								msg_fmt += self.INDENT

							if idx > 0:
								msg_fmt += ", "

							msg_fmt += msg_arr.to_string(self.DEPTHS + 2)

						for depth in range(0, self.DEPTHS):
							msg_fmt += self.INDENT

						msg_fmt += "]"

			if key_type != self.TYPE.MESSAGE:
				msg_fmt += "\n"

		for depth in range(0, self.DEPTHS - 1):
			msg_fmt += self.INDENT

		msg_fmt += "}\n"

		return msg_fmt