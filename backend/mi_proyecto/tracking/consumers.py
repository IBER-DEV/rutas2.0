import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class BusTrackingConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Query params: ?bus_id=1  OR path-based grouping
        self.bus_id = self.scope['url_route']['kwargs'].get('bus_id')
        if not self.bus_id:
            await self.close()
            return
        self.group_name = f"bus_{self.bus_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        # Optionally: send last known location
        # await self.send_json({"type":"connected","bus_id":self.bus_id})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        # If frontend sends pings or control messages, procesarlos aquí
        pass

    async def bus_location(self, event):
        # evento enviado en perform_create
        payload = {
            "type": "location_update",
            "bus_id": event.get("bus_id"),
            "lat": event.get("lat"),
            "lng": event.get("lng"),
            "speed": event.get("speed"),
            "recorded_at": event.get("recorded_at"),
        }
        await self.send_json(payload)
