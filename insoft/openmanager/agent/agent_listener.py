import sys
import socket
import select

from insoft.openmanager.agent.agent_executor import AgentExecutor

class AgentListener:
    
    def __init__(self, port):
        self.PORT = port

    def listen(self):

        # 소켓 객체를 생성합니다. 
        # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
        agent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 포트 사용중이라 연결할 수 없다는 
        # WinError 10048 에러 해결를 위해 필요합니다. 
        agent_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
        # HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
        # 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다. 
        # PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.
        agent_socket.bind(('', self.PORT))

        # 서버가 클라이언트의 접속을 허용하도록 합니다. 
        agent_socket.listen()
        socketList = [agent_socket]
    
        print ("[AGENT_LITE] Listener started on port " + str(self.PORT))
    
        while 1:
            try :
                read_socket, write_socket, error_socket = select.select(socketList, [], [], 1)

                for sock in read_socket :
                    if sock == agent_socket :
                        # 서버로부터 접속된 소켓을 처리한다.
                        dof_server_socket, addr = agent_socket.accept()
                        print ("[AGENT_LITE] Socket (%s, %s) connected" % addr)
                        AgentExecutor(dof_server_socket)

            except KeyboardInterrupt :
                break
            

        agent_socket.close()
