from insoft.openmanager.message.message import Message

from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.agent_packet import AgentPacket
from insoft.openmanager.message.packet_reader import PacketReader
from insoft.openmanager.message.packet_writer import PacketWriter

class AgentHandler():

    def write(self, agent_packet, sock, msgResponse):
        
        packet_writer = PacketWriter()
        b_msg = packet_writer.parse_to_bytes(msgResponse)

        agent_packet.send(sock, b_msg)

        print('[RSP]', msgResponse)
    
    