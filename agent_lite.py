import sys
# System Path를 설정하여 root부터 데이터를 가져오도록 설정할수 있다.
sys.path.append('D:/workspace/Python/python_message')

from insoft.openmanager.agent.agent_listener import AgentListener

if __name__ == "__main__":
    # 파라미터로 host port를 받아서 처리한다.
    if(len(sys.argv) < 2) :
        print ('[AGENT_LITE] Usage : python agent_lite.py port')
        sys.exit()
    
    port = int(sys.argv[1])

    agentListener = AgentListener(port)
    sys.exit(agentListener.listen())