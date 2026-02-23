from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models, configs

router = APIRouter()

@router.get("/checkin")
def checkin_check():
    return {"message": "Checkin endpoint is working!"}
