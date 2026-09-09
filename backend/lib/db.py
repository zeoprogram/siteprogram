INDEXES: dict[str, list[IndexModel]] = {
    "status_checks": [
        IndexModel(
            [("timestamp", DESCENDING)],
            name="timestamp_desc",
        )
    ],

    "bookings": [
        IndexModel(
            [("id", ASCENDING)],
            name="booking_id",
            unique=True,
        ),

        IndexModel(
            [("code", ASCENDING)],
            name="booking_code",
            unique=True,
        ),

        IndexModel(
            [("created_at", DESCENDING)],
            name="booking_created_desc",
        ),

        IndexModel(
            [
                ("status", ASCENDING),
                ("preferred_date", ASCENDING),
            ],
            name="booking_queue",
        ),
    ],
}
