import sys
from insoft.openmanager.message.message import Message

class WatchGet():

    def readCommand(self, title):
        sys.stdout.write(title + " : ")
        sys.stdout.flush()

        command = sys.stdin.readline()
        command = command.rstrip()

        return command


    def watch_get(self):
        
        objectId = self.readCommand('object id')
        
        msg = Message("WATCH_GET")
        msg.set_str('field_name', 'object_id')
        msg.set_array('field_value', [objectId])
        
        return msg

    def watch_get_all(self):
        
        msg = Message("WATCH_GET")
        msg.set_str('field_name', 'config_child')
        msg.set_array('field_value', ["0"])
        
        return msg

  