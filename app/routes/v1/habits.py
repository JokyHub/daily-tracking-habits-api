from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models, configs

router = APIRouter()

@router.get("/habits")
def habits_check():
    return {"message": "Habits endpoint is working!"}