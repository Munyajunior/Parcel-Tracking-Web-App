from sqlalchemy.orm import Session
from .models import Package, PackageRoute
from .schemas import PackageCreate
from datetime import datetime

def create_package(db: Session, package_data: PackageCreate):
    new_package = Package(**package_data.model_dump())
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return new_package

def update_package_location(db: Session, parcel_id: str, latitude: float, longitude: float):
    route = PackageRoute(parcel_id=parcel_id, latitude=latitude, longitude=longitude)
    db.add(route)
    db.commit()
    return route

def get_package(db: Session, parcel_id: str):
    return db.query(Package).filter(Package.parcel_id == parcel_id).first()

def get_package_routes(db: Session, parcel_id: str):
    return db.query(PackageRoute).filter(PackageRoute.parcel_id == parcel_id).all()
