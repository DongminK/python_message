from insoft.openmanager.message.message import Message

msg = Message()

msg.set_string("key", "value")
msg.set_integer("key", 2)

print(msg.get_integer("key", 1))


