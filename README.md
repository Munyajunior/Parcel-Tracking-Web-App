# Parcel Tracking Web App
 FastAPI-based parcel tracking system:

```
parcel_tracking/
│── app/
│   ├── __init__.py
│   ├── main.py              # Entry point for the FastAPI application
│   ├── models.py            # Database models (SQLAlchemy)
│   ├── schemas.py           # Pydantic schemas for data validation
│   ├── database.py          # Database connection and session handling
│   ├── crud.py              # CRUD operations for packages and routes
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── package.py       # Package-related API endpoints
│   │   ├── tracking.py      # Tracking and WebSocket endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── websocket.py     # WebSocket service for real-time updates
│── .env                     # Environment variables (DB credentials, API keys)
│── requirements.txt          # Required Python packages
│── alembic/                  # Alembic for database migrations
│── README.md                 # Project documentation

```