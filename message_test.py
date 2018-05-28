import copy

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_reader import PacketReader
'''
msg = Message("TEST")

print("Integer")

msg.set_int("int", 324)
print(msg.get_int_def("int", 100))
#msg.set_str("int", "SER")
print(msg.get_int_def("int", 100))
print(msg.get_int("int"))

print("\nFloat")

msg.set_float("float", 314.234)
print(msg.get_float_def("float", 1.1))
#msg.set_str("float", "SER")
print(msg.get_float_def("float", 1.1))
print(msg.get_float("float"))


print("\nLong")

msg.set_long("long", 31412093490123480234)
print(msg.get_long_def("long", 11))
#msg.set_str("long", "SER")
print(msg.get_long_def("long", 11))
print(msg.get_long("long"))


print("\nString")

msg.set_str("str", "test")
print(msg.get_str_def("str", "DEF"))
#msg.set_int("str", 11)
print(msg.get_str_def("str", "DEF"))
print("[" + msg.get_str("str") + "]")

print("\nMessage")
submsg = Message("SUB")
submsg.set_int("test", 123123)

submsg1 = Message("SUB1")
submsg1.set_int("test", 123)

msg.set_msg("msg", submsg)

print(msg.get_msg_def("msg", submsg1).get_int("test"))
#msg.set_int("msg", 11)
print(msg.get_msg_def("msg", submsg1).get_int("test"))
print(msg.get_msg("msg").get_int("test"))


print("\nBytes")

msg.set_bytes("byte", bytes("TEST", "utf-8"))

print(msg.get_bytes_def("byte", bytes("kim", "utf-8")))
#msg.set_int("byte", 11)
print(msg.get_bytes_def("byte", bytes("kim", "utf-8")))
print(msg.get_bytes("byte"))


print("\nArray")

msg.set_array("array", [1,2,3,4,5])
print(msg.get_array_def("array", [2]))
#msg.set_int("array", 1)
print(msg.get_array_def("array", [2]))
print(msg.get_array("array"))

msg.set_array("str_array", ["1","2","3","4","5"])
msg.set_array("float_array", [1.1,2.2,3.3,4.4,5.5])

msg1 = Message("TEST1")
msg1.set_str("test", "test1")
msg1.set_array("str_array", ["1","2","3","4","5"])
msg1.set_array("float_array", [1.1,2.2,3.3,4.4,5.5])

msg2 = Message("TEST2")
msg2.set_str("test", "test2")
msg2.set_array("str_array", ["1","2","3","4","5"])
msg2.set_array("float_array", [1.1,2.2,3.3,4.4,5.5])

msg3 = Message("TEST3")
msg3.set_str("test", "test3")

arr_mag = [msg1, msg2, msg3]
msg.set_array("msg_arr", arr_mag)

msg_copy = copy.deepcopy(msg)
print(msg)
msg_copy.set_str("copy", "copy")
msg_copy.remove("msg_arr")
print(msg_copy)

'''

data = b'C\x00\x00\x00\x06S\x00\x00\x00\nAGENT_INITS\x00\x00\x00\x04dateS\x00\x00\x00\nip_addressS\x00\x00\x00\x04portS\x00\x00\x00\x16versionmanager_addressS\x00\x00\x00\x13versionmanager_portS\x00\x00\x00\x0fversionmanagersS\x00\x00\x00\x0e20180524154906S\x00\x00\x00\x0f192.168.255.146I\xff\xff\xff\xffS\x00\x00\x00\r123.212.42.13I\x00\x00\x1f@V\x00\x00\x00\x01C\x00\x00\x00\x03S\x00\x00\x00\x0eVERSIONMANAGERS\x00\x00\x00\x02ipS\x00\x00\x00\x04nameS\x00\x00\x00\x04portS\x00\x00\x00\r123.212.42.13S\x00\x00\x00\x03OMCI\x00\x00\x1f@'

packet = Packet()
packet_reader = PacketReader(data)
msg = packet_reader.parse_to_msg()

print(msg)