## PACKET
'''
SERVER_ID, 1
FLAG, 1
REQUEST_ID, 4

HEADER, 4, INOM
VER, 3, 100
DATA_LENGTH, 4

DATA, DATA_LENGTH
	C, 1
	FIELD_SIZE, 4
	S, 1
	MESSAGE_NAME, S


TAIL, 4, MONI
'''

import struct

from insoft.openmanager.message.packet import Packet

data = b'\x01\x00\x00\x04\x93\xe1INOM100\x00\x00\x01\x14C\x00\x00\x00\x06S\x00\x00\x00\nAGENT_INITS\x00\x00\x00\x04dateS\x00\x00\x00\nip_addressS\x00\x00\x00\x04portS\x00\x00\x00\x16versionmanager_addressS\x00\x00\x00\x13versionmanager_portS\x00\x00\x00\x0fversionmanagersS\x00\x00\x00\x0e20180524154906S\x00\x00\x00\x0f192.168.255.146I\xff\xff\xff\xffS\x00\x00\x00\r123.212.42.13I\x00\x00\x1f@V\x00\x00\x00\x01C\x00\x00\x00\x03S\x00\x00\x00\x0eVERSIONMANAGERS\x00\x00\x00\x02ipS\x00\x00\x00\x04nameS\x00\x00\x00\x04portS\x00\x00\x00\r123.212.42.13S\x00\x00\x00\x03OMCI\x00\x00\x1f@MONI'


SERVER_ID = struct.unpack_from("!B", data, 0)[0]
FLAG = struct.unpack_from("!B", data, 1)[0]
REQ_ID = struct.unpack_from("!I", data, 2)[0]
HEADER = bytes(struct.unpack_from("!4s", data, 6)[0]).decode()
VER = bytes(struct.unpack_from("!3s", data, 10)[0]).decode()
DATA_LENGTH = struct.unpack_from("!I", data, 13)[0]

print(SERVER_ID, FLAG, REQ_ID, HEADER, VER, DATA_LENGTH)
len = 17

SIG = bytes(struct.unpack_from("!s", data, len)[0]).decode()
print(SIG)
len += 1

FIELD_SIZE = struct.unpack_from("!I", data, len)[0]
print(FIELD_SIZE)
len += 4

SIG = bytes(struct.unpack_from("!s", data, len)[0]).decode()
print(SIG)
len += 1

DATA_SIZE = struct.unpack_from("!I", data, len)[0]
print(DATA_SIZE)
len += 4

fmt = "!" + str(DATA_SIZE) + "s"
DATA = bytes(struct.unpack_from(fmt, data, len)[0]).decode()
print(DATA)
len += DATA_SIZE

packet = Packet()
packet.recv(data, )