from insoft.openmanager.agent.handler.agent_handler import AgentHandler
from insoft.openmanager.message.message import Message

from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.agent_packet import AgentPacket
from insoft.openmanager.message.packet_reader import PacketReader
from insoft.openmanager.message.packet_writer import PacketWriter

class Os(AgentHandler):

    def setParam(self, sock, agentPacket, msgRequest):
        self.sock = sock
        self.agent_packet = agentPacket
        self.r_msg = msgRequest

    def execute(self):
        msgResponse = Message(self.r_msg.get_name())
        msgResponse.set_int("return_code", 1)
        
        msgResponse.set_int("current_nfiles", 2656)
        msgResponse.set_int("current_queue", 1)
        msgResponse.set_int("idle", 94)
        msgResponse.set_int("max_nfile", 381681)
        msgResponse.set_int("mem_buffer", 0)
        msgResponse.set_int("mem_cached", 2138)
        msgResponse.set_int("mem_free", 312)
        msgResponse.set_int("mem_used", 3478)
        msgResponse.set_int("real_free", 2588)
        msgResponse.set_int("real_total", 3790)
        msgResponse.set_int("swap_free", 3036)
        msgResponse.set_int("swap_total", 3072)
        msgResponse.set_int("system", 4)
        msgResponse.set_int("user", 2)
        msgResponse.set_int("wait", 0)

        self.write(self.agent_packet, self.sock, msgResponse)
 