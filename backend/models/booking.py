from datetime import datetime, timezone
from typing import Literal
import uuid

from pydantic import BaseModel, Field


BookingStatus = Literal[
    "pending",
    "confirmed",
    "in_progress",
    "quality_check",
    "completed",
    "cancelled",
]

ServiceLocation = Literal["workshop", "home_service"]


class BookingCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    whatsapp: str = Field(min_length=8, max_length=30)

    vehicle_category: str = Field(
        min_length=2,
        max_length=30,
    )

    vehicle_type: str = Field(
        min_length=2,
        max_length=60,
    )

    vehicle_model: str = Field(
        min_length=2,
        max_length=80,
    )

    plate_number: str = Field(
        min_length=2,
        max_length=15,
    )

    service_location: ServiceLocation

    services: list[str] = Field(
        min_length=1,
        max_length=8,
    )

    preferred_date: str = Field(
        pattern=r"^\d{4}-\d{2}-\d{2}$"
    )

    time_slot: str = Field(
        min_length=3,
        max_length=30,
    )

    address: str | None = Field(
        default=None,
        max_length=240,
    )

    notes: str | None = Field(
        default=None,
        max_length=500,
    )

    estimated_total: int = Field(
        ge=0,
    )


class Booking(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4())
    )

    code: str

    customer_name: str
    whatsapp: str

    vehicle_category: str
    vehicle_type: str
    vehicle_model: str
    plate_number: str

    service_location: ServiceLocation

    services: list[str]

    preferred_date: str
    time_slot: str

    address: str | None = None
    notes: str | None = None

    estimated_total: int

    status: BookingStatus = "pending"

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class BookingStatusUpdate(BaseModel):
    status: BookingStatus


class MetaResponse(BaseModel):
    today: str
    workshop_name: str
