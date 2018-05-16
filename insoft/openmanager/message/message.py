from insoft.openmanager.message.type import _MessageType


class Message:

	TYPE = _MessageType()
	map_value = {}
	map_type = {}

	def set_integer(self, key, value):
		self.map_value[key] = value
		self.map_type[key] = self.TYPE.INTEGER

	def get_integer(self, key, defValue):
		if self.map_type[key] != self.TYPE.INTEGER:
			return defValue

		return self.map_value[key]

	def set_float(self, key, value):
		self.map_value[key] = value
		self.map_type[key] = self.TYPE.FLOAT

	def get_float(self, key, defValue):
		if self.map_type[key] != self.TYPE.FLOAT:
			return defValue

		return self.map_value[key]

	def set_string(self, key, value):
		self.map_value[key] = value
		self.map_type[key] = self.TYPE.STRING

	def get_string(self, key, defValue):
		if self.map_type[key] != self.TYPE.STRING:
			return defValue

		return self.map_value[key]







