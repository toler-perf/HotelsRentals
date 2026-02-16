from datetime import date
from typing import Optional
from fastapi import FastAPI, Depends
from pydantic import BaseModel

from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_bookings)

