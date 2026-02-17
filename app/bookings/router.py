from fastapi import APIRouter, Depends

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBookings
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingsDAO.find_all(user_id=user.id)
