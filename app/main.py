from datetime import date
from typing import Optional
from fastapi import FastAPI, Depends
from pydantic import BaseModel

from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_bookings)


class HotelsSearchArgs(BaseModel):
    def __init__(
        self, 
        location: str, 
        date_from: date, 
        date_to: date, 
        guests: int, 
        stars: Optional[int] = None
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.guests = guests
        self.stars = stars

@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
):
    return search_args
