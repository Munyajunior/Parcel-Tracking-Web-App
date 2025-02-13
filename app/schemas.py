from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class PackageCreate(BaseModel):
    sender_name: str
    sender_address: str
    receiver_name: str
    receiver_address: str
    source: str
    destination: str
    weight: float
    content: str
    delivery_type: str

class PackageResponse(PackageCreate):
    parcel_id: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PackageRouteResponse(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime

    class Config:
        orm_mode = True

class RouteResponse(BaseModel):
    parcel_id: str
    route_history: List[PackageRouteResponse]
