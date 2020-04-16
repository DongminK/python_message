# chat_client.py

import sys
import socket
import threading
 
def chat_client():
    
    # 파라미터로 hostname port를 받아서 처리한다.
    if(len(sys.argv) < 3) :
        print ('Usage : python client.py hostname port')
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
    
    # 데이터를 수신할 스레드 생성
    receiver = threading.Thread(target=recvThread, args=(sock,)) 
    receiver.start()

    # 데이터를 전송할 스레드 생성
    sender = threading.Thread(target=sendThread, args=(sock,)) 
    sender.start()
    
# 전송 스레드    
def sendThread(sock):

    print('\n[SENDER] Thread start')

    while True:

        try:
            sys.stdout.write('[Me] '); sys.stdout.flush()    

            # 데이터 입력을 받는다
            msg = sys.stdin.readline()

            if msg == 'quit\n':
                break

            # 받은 데이터(str)를 byte로 변환하여 데이터 전송
            sock.send(msg.encode())
        except Exception as e:
             print('\n[SENDER] Unable to connect ', e)
             break

    sock.close() 



# 수신 스레드
def recvThread(sock): 
    print('\n[RECEIVER] Thread start')
    
    while True: 

        try:

            # 서버로 부터 전달된 데이터 를 받는다
            data = sock.recv(4096)
                        
            if not data: 
                # 데이터가 아닐경우 연결종료
                print('\n[RECEIVER] Disconnected from chat server')
                sys.exit()
            else :
                # 수신된 데이터(byte)를 변환(str)한다.
                decodeData = data.decode()

                # 변환된 데이터 출력
                sys.stdout.write(decodeData)
                sys.stdout.write('[Me] '); sys.stdout.flush()    
            
        except Exception as e:
            print('\n[RECEIVER] Disconnected from chat server ', e)
            break

    sock.close() 

if __name__ == "__main__":
    sys.exit(chat_client())