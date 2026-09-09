from pydantic import BaseModel

from routers.bookings import router as bookings_router


class RootResponse(BaseModel):
    message: str


@api_router.get(
    "/",
    response_model=RootResponse,
)
async def root():
    return RootResponse(
        message="Haryadi Garage API siap digunakan"
    )


api_router.include_router(
    bookings_router
)
