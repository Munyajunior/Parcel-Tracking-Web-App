from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import create_package, get_package
from ..schemas import PackageCreate, PackageResponse

router = APIRouter()

@router.post("/", response_model=PackageResponse)
def create_package_endpoint(package: PackageCreate, db: Session = Depends(get_db)):
    return create_package(db, package)

@router.get("/{parcel_id}/", response_model=PackageResponse)
def get_package_endpoint(parcel_id: str, db: Session = Depends(get_db)):
    return get_package(db, parcel_id)
