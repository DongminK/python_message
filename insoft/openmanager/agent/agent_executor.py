import sys
import threading
import traceback

from insoft.openmanager.agent.handler.echo import Echo
from insoft.openmanager.agent.handler.agent_init import AgentInit
from insoft.openmanager.agent.handler.auto_start import AutoStart
from insoft.openmanager.agent.handler.system_resource import SystemResrouce
from insoft.openmanager.message.agent_packet import AgentPacket

class AgentExecutor:

    def __init__(self, sock):
        self.handlers = {}
        self.sock = sock
        self.loadHandlers()
        
        # 데이터 응답받을 스레드 생성
        executor = threading.Thread(target=self.dataExecutor, args=(sock, )) 
        executor.daemon = True
        executor.start()


    def loadHandlers(self):
        self.handlers['ECHO'] = Echo()
        self.handlers['AGENT_INIT'] = AgentInit()
        self.handlers['SYSTEM_RESOURCE'] = SystemResrouce()
        self.handlers['AUTOSTART'] = AutoStart()

    # 수신 데이터
    def dataExecutor(self, sock): 

        while 1:
            try:
                # 수신받은 데이터를 읽어들인다.
                agentPacket = AgentPacket()
                r_msg = agentPacket.recv(sock)
                
                msgRequest = r_msg[0]
                print("[REQ]", msgRequest)

                try:
                    handler = self.handlers[msgRequest.get_name()]
                    handler.setParam(sock, agentPacket, msgRequest)
                    handler.execute()
                except Exception as e:
                    print("[AGENT_LITE] Not found handler - ", msgRequest.get_name())
                    traceback.print_exc(file=sys.stdout)

            except Exception as e:
                raise e
        
        sock.close()

    
