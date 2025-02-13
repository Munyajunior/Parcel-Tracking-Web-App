from fastapi import FastAPI
from .routes import package, tracking
from .database import Base, engine

# Initialize DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include Routers
app.include_router(package.router, prefix="/package", tags=["Packages"])
app.include_router(tracking.router, prefix="/tracking", tags=["Tracking"])
