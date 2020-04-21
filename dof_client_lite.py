# chat_client.py

import traceback
import sys
import socket
import threading
import time
import select

from insoft.openmanager.client.handler.login import Login
from insoft.openmanager.client.handler.config_get import ConfigGet
from insoft.openmanager.client.handler.channel_get import ChannelGet
from insoft.openmanager.client.handler.watch_get import WatchGet
from insoft.openmanager.client.handler.fault_get_current import FaultGetCurrent


from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_reader import PacketReader
from insoft.openmanager.message.packet_writer import PacketWriter
from insoft.openmanager.message.client_packet_dof import DofClientPacket

def dof_client():
    
    # 파라미터로 hostname port를 받아서 처리한다.
    if(len(sys.argv) < 3) :
        print ('Usage : python dof_client_lite.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    
    # 소켓을 연결한다 (IPv4, TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2000)
    
    try :
        sock.connect((host, port))
    except :
        print ('Unable to connect')
        sys.exit()
     
    print ('Connected to remote host. You can start sending messages')
    
    handlers = {}
    loadHandler(handlers)

    # 데이터를 요청할 스레드 생성
    sender = threading.Thread(target=sendThread, args=(sock,handlers, )) 
    sender.start()

def loadHandler(handlers):
    handlers['login'] = Login().login
    handlers['config_get'] = ConfigGet().config_get
    handlers['config_get_all'] = ConfigGet().config_get_all
    handlers['channel_get'] = ChannelGet().channel_get
    handlers['channel_get_all'] = ChannelGet().channel_get_all
    handlers['watch_get'] = WatchGet().watch_get
    handlers['watch_get_all'] = WatchGet().watch_get_all
    handlers['fault_get_current'] = FaultGetCurrent().fault_get_current
    
def login(sock, sessionId, requestId, handlers):

    r_msg = handlers['login']()
    print("[REQ]", r_msg)

    packet_writer = PacketWriter()
    b_msg = packet_writer.parse_to_bytes(r_msg)

    client_packet = DofClientPacket()
    client_packet.set_session_id(sessionId)
    client_packet.set_request_id(requestId)
    client_packet.send(sock, b_msg)

    r_msg = recvData(sock, sessionId, requestId)

    return r_msg.get_int("session_id")

# 전송 스레드    
def sendThread(sock, handlers):

    print('\n[CLIENT] Start')
    print('\n help: command list')
    print('\n exit: process quit')
    
    requestId = 0
    sessionId = 0

    sessionId = login(sock, sessionId, requestId, handlers)

    while True:

        sys.stdout.write('>> ')
        sys.stdout.flush()

        msgName = sys.stdin.readline()
        try:
            
            msgName = msgName.rstrip()

            if msgName == '':
                continue

            if msgName == 'exit':
                break
            
            if msgName == 'help':
                print('## command list ##')
                print('exit')
                print('help')
                for key in handlers:
                    print(key)
                continue

            try:
                handler = handlers[msgName]
            except Exception:
                print('\n[CLIENT] Not support handler - ' + msgName)
                continue
            
            r_msg = handler()#.request()

            requestId += 1
            print("[REQ]", r_msg)

            packet_writer = PacketWriter()
            b_msg = packet_writer.parse_to_bytes(r_msg)

            client_packet = DofClientPacket()
            client_packet.set_session_id(sessionId)
            client_packet.set_request_id(requestId)
            client_packet.send(sock, b_msg)

            r_msg = recvData(sock, sessionId, requestId)

            if r_msg.get_name() == 'LOGIN':
                sessionId = r_msg.get_int("session_id")

        except Exception:
             traceback.print_exc(file=sys.stdout)
             break

    sock.close() 


# 수신 데이터
def recvData(sock, sessionId, requestId): 
    try:
        # 수신받은 데이터를 읽어들인다.
        client_packet = DofClientPacket()
        client_packet.set_session_id(sessionId)
        client_packet.set_request_id(requestId)
        r_msg = client_packet.recv(sock)
        
        msg = r_msg[0]
        print("[RSP]", msg)

        return msg

    except Exception as e:
        raise e

if __name__ == "__main__":
    sys.exit(dof_client())