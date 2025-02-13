from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import update_package_location, get_package_routes
from ..schemas import RouteResponse
from ..models import PackageRoute

router = APIRouter()

@router.put("/{parcel_id}/update-location/")
def update_location(parcel_id: str, latitude: float, longitude: float, db: Session = Depends(get_db)):
    return update_package_location(db, parcel_id, latitude, longitude)

@router.get("/{parcel_id}/route/", response_model=RouteResponse)
def get_route(parcel_id: str, db: Session = Depends(get_db)):
    return {"parcel_id": parcel_id, "route_history": get_package_routes(db, parcel_id)}

@router.websocket("/ws/{parcel_id}")
async def websocket_tracking(websocket: WebSocket, parcel_id: str, db: Session = Depends(get_db)):
    await websocket.accept()
    while True:
        latest_route = db.query(PackageRoute).filter(PackageRoute.parcel_id == parcel_id).order_by(PackageRoute.timestamp.desc()).first()
        if latest_route:
            await websocket.send_json({"latitude": latest_route.latitude, "longitude": latest_route.longitude})
