from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "users/index.html"

async def websocket_view(socket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        message = 'add_' + message
        await socket.send_text(message)
    # await socket.send_text(str(socket.headers))
    # await socket.send_text('hello')
    # await socket.close()