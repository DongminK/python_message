import sys
from insoft.openmanager.message.message import Message

class FaultGetCurrent():

    def fault_get_current(self):
        msg = Message("FAULT_GET_CURRENT")
        msg.set_str('field_name', 'config_id')
        msg.set_array('field_value', [])
        
        return msg

