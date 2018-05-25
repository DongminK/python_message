from insoft.openmanager.message.message import Message

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

print(msg)