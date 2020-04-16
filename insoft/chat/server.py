import sys
import socket
import select

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9900

def chat_server():

    # 소켓 객체를 생성합니다. 
    # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 포트 사용중이라 연결할 수 없다는 
    # WinError 10048 에러 해결를 위해 필요합니다. 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
    # HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
    # 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다. 
    # PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.
    server_socket.bind((HOST, PORT))

    # 서버가 클라이언트의 접속을 허용하도록 합니다. 
    server_socket.listen()
 
    # SELECTOR를 사용하기 위해 서버소켓을 배열에 추가
    SOCKET_LIST.append(server_socket)
 
    print ("Chat server started on port " + str(PORT))
 
    while 1:

        # SELECTOR를 이용하여 소켓들의 상태를 파악하여 대기함
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST, [], [], 0)
      
        # 데이터가 준비된 소켓에서 데이터를 읽어들인다.
        for sock in ready_to_read:
            
            # 서버소켓일경우 클라이언트 접속 처리
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()

                # 접속된 클라이언트 소켓은 소켓배열에 추가한다.
                SOCKET_LIST.append(sockfd)
                print ("Client (%s, %s) connected" % addr)
                 
                # 클라이언트가 추가된 사항을 접속된 전체 클라이언트에게 전달한다
                broadcast(server_socket, sockfd, '[%s:%s] entered our chatting room\n' % addr)
             
            # 클라이언트로 부터 전달받은 경우
            else:
                
                try:
                    # 수신받은 데이터를 읽어들인다.
                    data = sock.recv(RECV_BUFFER)

                    if data:
                        # 수신데이터 (bytes)를 변환 (str) 한다.
                        decodeData = data.decode()
                        print("\r" + '[' + str(sock.getpeername()) + '] ' + decodeData)

                        # 수신된 데이터를 접속된 전체 클라이언트에게 전달한다
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + decodeData)  
                    else:
                        # 데이터가 아닐경우 해당 소켓을 제외한다. 
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # 제외된 클라이언트 정보를 전체 클라이언트에게 전달한다.
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                print(message)

                # 전달할 데이터(str)를 변환(bytes) 한다.
                socket.send(message.encode())
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(chat_server())   