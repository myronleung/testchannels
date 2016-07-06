from channels import Group
from channels.sessions import channel_session
from ctest.models import *

# Connected to websocket.receive
@channel_session
def ws_connect(message):
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)
    print('--- connect ---')
    print('room: '+room)

# Connected to websocket.receive
@channel_session
def ws_message(message):
    u = UserProfile.objects.get(id=1)
    r = Room.objects.get(id=1)
    if message['text'] != '':
        m = Message(author = u, room = r, message=message['text'])
        m.save()
    print('message: '+message['text'])
    try:
        Group("chat").send({
            "text": "[user] %s" % message.content['text'],
        })
        print('sent')
    except:
        print('failed')


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
    print('dc')
