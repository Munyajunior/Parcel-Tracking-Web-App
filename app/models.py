from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from .database import Base

class Package(Base):
    __tablename__ = "packages"

    parcel_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    sender_name = Column(String, index=True)
    sender_address = Column(String)
    receiver_name = Column(String, index=True)
    receiver_address = Column(String)
    source = Column(String)
    destination = Column(String)
    weight = Column(Float)
    content = Column(String)
    delivery_type = Column(String)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    routes = relationship("PackageRoute", back_populates="package")

class PackageRoute(Base):
    __tablename__ = "package_routes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    parcel_id = Column(String, ForeignKey("packages.parcel_id"))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

    package = relationship("Package", back_populates="routes")
