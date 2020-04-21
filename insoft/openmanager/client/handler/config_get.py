import sys
from insoft.openmanager.message.message import Message

class ConfigGet():

    def readCommand(self, title):
        sys.stdout.write(title + " : ")
        sys.stdout.flush()

        command = sys.stdin.readline()
        command = command.rstrip()

        return command


    def config_get(self):
        
        objectId = self.readCommand('object id')
        
        msg = Message("CONFIG_GET")
        msg.set_str('field_name', 'object_id')
        msg.set_array('field_value', [objectId])
        
        return msg

    def config_get_all(self):
        msg = Message("CONFIG_GET")
        msg.set_str('field_name', 'user_configs')
        msg.set_array('field_value', ['0'])
        
        return msg