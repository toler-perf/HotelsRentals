from fastapi import APIRouter

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBookings

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings() -> list[SBookings]:
    return await BookingsDAO.find_all()
