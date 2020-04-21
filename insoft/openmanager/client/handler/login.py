import sys
from insoft.openmanager.message.message import Message

class Login():

    def login(self):
        
        msg = Message("LOGIN")
        msg.set_str('user_id', 'root')
        msg.set_str('user_pw', 'changeit')
        msg.set_int('client_type', 6)

        return msg

  