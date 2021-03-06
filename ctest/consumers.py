from channels import Group
from channels.sessions import channel_session
from ctest.models import *
import json

# Connected to websocket.receive
@channel_session
def ws_connect(message):
    Group("chat").add(message.reply_channel)
    print('--- connect ---')

# Connected to websocket.receive
@channel_session
def ws_message(message):
    u = UserProfile.objects.get(id=1)
    r = Room.objects.get(id=1)
    if message['text'] != '':
        m = Message(author = u, room = r, message=message['text'])
        m.save()
    print('message: '+message.content['text'])
    data = json.loads(message.content['text'])
    print('data:')
    print(data)
    print('---------')
    # try:
    Group("chat").send({'text':m.message})
    print('sent')
    # except:
    #     print('failed')


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
    print('dc')
