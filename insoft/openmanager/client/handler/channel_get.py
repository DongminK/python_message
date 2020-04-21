import sys
from insoft.openmanager.message.message import Message

class ChannelGet():

    def readCommand(self, title):
        sys.stdout.write(title + " : ")
        sys.stdout.flush()

        command = sys.stdin.readline()
        command = command.rstrip()

        return command


    def channel_get(self):
        
        objectId = self.readCommand('object id')
        
        msg = Message("CHANNEL_GET")
        msg.set_str('field_name', 'object_id')
        msg.set_array('field_value', [objectId])
        
        return msg

    def channel_get_all(self):
        
        msg = Message("CHANNEL_GET")
        msg.set_str('base_config_id', '0')
        msg.set_str('channel_type', '*')
        msg.set_str('field_name', 'list')
        msg.set_str('object_id', '*')
        msg.set_str('os', '*')
        msg.set_str('watch_type', '*')
        msg.set_array('field_value', [])
        
        return msg


  