from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from inspect import currentframe as frame

from starlette.responses import Response

from app.database.connect import db

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
