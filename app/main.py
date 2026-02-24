from fastapi import FastAPI
import uvicorn
from app.routes.v1 import users, checkin, habits
from app.configs.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Daily Tracking Habits API",
    description="An API to help users track their daily habits and routines.",
    version="1.0.0"
)

app.include_router(users.router, prefix="/routes/v1/users", tags=["users"]
                   )
app.include_router(checkin.router, prefix="/routes/v1/checkin", tags=["checkin"])
app.include_router(habits.router, prefix="/routes/v1/habits", tags=["habits"])

# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the Daily Tracking Habits API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)