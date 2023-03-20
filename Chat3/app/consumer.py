import json
from channels.generic.websocket import SyncConsumer
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from app.models import Chat,Group


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Connection Established', event, type(event))
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print('Message from client is', event, event['text'], type(event))
        data = json.dumps(event['text'])
        d2 = json.loads(event['text'])
        group = Group.objects.get(name=self.group_name)
        chat = Chat.objects.create(content = d2['message'],group=group)
        print('D22222222222',d2,type(d2))
        print(data, type(data))
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat.message",
                "message": event['text']
            }
        )

    def chat_message(self, event):
        self.send({
            "type": "websocket.send",
            "text": event['message']
        })

    def websocket_disconnect(self, event):
        print('Connection Disconnected', event, type(event))
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()

    

class MyASyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Connection Established',event,type(event))
        # groupname = self.scope['url_route']['*kwargs']['groupname']
        self.send({
            "type":"websocket.accept"
        })
    def websocket_receive(self,event):
        print('Message from server is',event,event['text'],type(event))
        
        self.send({
            "type":"websocket.send",
            "text":"message recieved"
        })
    def websocket_disconnect(self,event):
        print('Connection Established',event,type(event))
        raise StopConsumer()