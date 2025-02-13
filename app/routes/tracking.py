from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import update_package_location, get_package_routes
from ..schemas import RouteResponse
from ..services.websocket import websocket_manager

router = APIRouter()

@router.put("/{parcel_id}/update-location/")
def update_location(parcel_id: str, latitude: float, longitude: float, db: Session = Depends(get_db)):
    return update_package_location(db, parcel_id, latitude, longitude)

@router.get("/{parcel_id}/route/", response_model=RouteResponse)
def get_route(parcel_id: str, db: Session = Depends(get_db)):
    return {"parcel_id": parcel_id, "route_history": get_package_routes(db, parcel_id)}

@router.websocket("/ws/{parcel_id}")
async def websocket_tracking(websocket: WebSocket, parcel_id: str, db: Session = Depends(get_db)):
    await websocket_manager.connect(websocket, parcel_id)
    try:
        await websocket_manager.broadcast_location(parcel_id, db)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        websocket_manager.disconnect(websocket, parcel_id)
