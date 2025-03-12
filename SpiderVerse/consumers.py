#Spiderverse/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Carrera

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("carreras_group", self.channel_name)
        await self.accept()
        await self.enviar_carreras()  # Enviar carreras al conectar

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("carreras_group", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            nombre = data.get("nombre")
            descripcion = data.get("descripcion")

            if nombre and descripcion:
                carrera = await self.guardarCarrera(nombre, descripcion)

                # Enviar notificación a todos los clientes conectados
                await self.channel_layer.group_send(
                    "carreras_group",
                    {
                        "type": "enviar_carreras",
                    }
                )

    @database_sync_to_async
    def guardarCarrera(self, nombre, descripcion):
        return Carrera.objects.create(nombre=nombre, descripcion=descripcion)

    @database_sync_to_async
    def getCarreras(self):
        return list(Carrera.objects.all().order_by('nombre'))

    async def enviar_carreras(self, event=None):
        carreras = await self.getCarreras()
        data = [{'nombre': c.nombre, 'descripcion': c.descripcion} for c in carreras]

        await self.send(text_data=json.dumps({"message": data}))