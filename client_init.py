import copy
import socket
import struct
import time

from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_reader import PacketReader
from insoft.openmanager.message.packet_writer import PacketWriter
from insoft.openmanager.message.client_packet_dof import DofClientPacket

msg = Message("LOGIN")
msg.set_str('user_id','root')
msg.set_str('user_pw','changeit')
msg.set_int('client_type', 6)

print(msg)

addr = ('192.168.9.62', 9100)
s = socket.socket()
s.connect(addr)

packet_writer = PacketWriter()
b_msg = packet_writer.parse_to_bytes(msg)


client_packet = DofClientPacket()
client_packet.send(s, b_msg)

print("send message...")

time.sleep(3)

r_msg = client_packet.recv(s)
print(r_msg)


time.sleep(3)
