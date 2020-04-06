import copy

import struct

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_reader import PacketReader
from insoft.openmanager.message.packet_writer import PacketWriter


msg = Message("MESSAGE_TEST")

msg.set_int("integer", 1)
msg.set_float("float", 2.0)
msg.set_long("long", 3)
msg.set_str("str", "message_test")
msg.set_bytes("byte", bytes("message", "utf-8"))
msg.set_msg("msg", Message("NEW_MESSAGE"))
msg.set_array("array", ["A","B","C"])

print(msg)
