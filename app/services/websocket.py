from fastapi import WebSocket
from sqlalchemy.orm import Session
from ..models import PackageRoute
import asyncio

class WebSocketManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, parcel_id: str):
        await websocket.accept()
        if parcel_id not in self.active_connections:
            self.active_connections[parcel_id] = []
        self.active_connections[parcel_id].append(websocket)

    def disconnect(self, websocket: WebSocket, parcel_id: str):
        if parcel_id in self.active_connections:
            self.active_connections[parcel_id].remove(websocket)
            if not self.active_connections[parcel_id]:  
                del self.active_connections[parcel_id]

    async def broadcast_location(self, parcel_id: str, db: Session):
        while True:
            if parcel_id not in self.active_connections:
                break  # Stop broadcasting if no active connections

            latest_route = (
                db.query(PackageRoute)
                .filter(PackageRoute.parcel_id == parcel_id)
                .order_by(PackageRoute.timestamp.desc())
                .first()
            )

            if latest_route:
                location_data = {"latitude": latest_route.latitude, "longitude": latest_route.longitude}
                for connection in self.active_connections.get(parcel_id, []):
                    await connection.send_json(location_data)

            await asyncio.sleep(5)  # Poll database every 5 seconds

websocket_manager = WebSocketManager()
