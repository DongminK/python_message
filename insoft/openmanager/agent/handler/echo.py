from insoft.openmanager.agent.handler.agent_handler import AgentHandler
from insoft.openmanager.message.message import Message

from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.agent_packet import AgentPacket
from insoft.openmanager.message.packet_reader import PacketReader
from insoft.openmanager.message.packet_writer import PacketWriter

class Echo(AgentHandler):

    def setParam(self, sock, agentPacket, msgRequest):
        self.sock = sock
        self.agent_packet = agentPacket
        self.r_msg = msgRequest

    def execute(self):
        msgResponse = Message(self.r_msg.get_name())
        msgResponse.set_int("return_code", 1)

        self.write(self.agent_packet, self.sock, msgResponse)
 