from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "users/index.html"

async def websocket_view(socket):
    await socket.accept()
    await socket.send_text('hello')
    await socket.close()