from datetime import datetime, timezone
import secrets

from fastapi import APIRouter, HTTPException, Query

from lib.db import db
from lib.dates import today_iso

from models.booking import (
    Booking,
    BookingCreate,
    BookingStatusUpdate,
    MetaResponse,
)


router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
)


def booking_code() -> str:
    return (
        f"HG-{datetime.now(timezone.utc).year}-"
        f"{secrets.token_hex(3).upper()}"
    )


@router.get(
    "",
    response_model=list[Booking],
)
async def list_bookings(
    status: str | None = Query(default=None),
    location: str | None = Query(default=None),
):
    query: dict[str, str] = {}

    if status:
        query["status"] = status

    if location:
        query["service_location"] = location

    documents = (
        await db.bookings
        .find(query)
        .sort("created_at", -1)
        .to_list(200)
    )

    return [
        Booking(**document)
        for document in documents
    ]


@router.post(
    "",
    response_model=Booking,
    status_code=201,
)
async def create_booking(
    input: BookingCreate,
):
    now = datetime.now(timezone.utc)

    booking = Booking(
        **input.model_dump(),
        code=booking_code(),
        created_at=now,
        updated_at=now,
    )

    await db.bookings.insert_one(
        booking.model_dump()
    )

    return booking


@router.get(
    "/track",
    response_model=list[Booking],
)
async def track_bookings(
    q: str = Query(
        min_length=2,
        max_length=100,
    ),
):
    escaped = q.strip()

    documents = (
        await db.bookings
        .find(
            {
                "$or": [
                    {
                        "code": escaped.upper()
                    },
                    {
                        "whatsapp": escaped
                    },
                ]
            }
        )
        .sort("created_at", -1)
        .to_list(20)
    )

    return [
        Booking(**document)
        for document in documents
    ]


@router.get(
    "/meta",
    response_model=MetaResponse,
)
async def get_booking_meta():
    return MetaResponse(
        today=today_iso("Asia/Jakarta"),
        workshop_name="Haryadi Garage",
    )


@router.get(
    "/{booking_id}",
    response_model=Booking,
)
async def get_booking(
    booking_id: str,
):
    document = await db.bookings.find_one(
        {
            "$or": [
                {
                    "id": booking_id
                },
                {
                    "code": booking_id.upper()
                },
            ]
        }
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Booking tidak ditemukan",
        )

    return Booking(**document)


@router.patch(
    "/{booking_id}/status",
    response_model=Booking,
)
async def update_booking_status(
    booking_id: str,
    input: BookingStatusUpdate,
):
    updated_at = datetime.now(timezone.utc)

    result = await db.bookings.update_one(
        {
            "id": booking_id
        },
        {
            "$set": {
                "status": input.status,
                "updated_at": updated_at,
            }
        },
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Booking tidak ditemukan",
        )

    document = await db.bookings.find_one(
        {
            "id": booking_id
        }
    )

    return Booking(**document)
