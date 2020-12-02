import random, time 

from django.shortcuts import render
from django.views.generic.base import TemplateView


socket_list = {}

class IndexView(TemplateView):
    template_name = "users/index.html"

async def websocket_view(socket):
    await socket.accept()
    print(type(socket.headers))
    key = socket.headers['sec-websocket-key']
    socket.scope["room"] = "test"
    socket_list[key] = socket
    await socket.send_text("socket start")
    await socket.send_text(str(socket.scope))
    # while sum < 20:
    #     await socket.receive_text()
    #     sum += random.randint(0,10)
    #     await socket.send_text(str(sum))
    # await socket.send_text(str(socket.headers))
    # await socket.send_text("socket closed")
    # await socket.close()

    while True:
        message = await socket.receive_text()
        for s in socket_list.values():
            if s.scope["room"] == "test":
                await s.send_text(message)
        # await socket.send_text(message)
    # await socket.send_text(str(socket.headers))
    # await socket.send_text('hello')
    # await socket.close()