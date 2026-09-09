# siteprogram
program/
│
├── README.md
├── SPEC.md
├── design_guidelines.json
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   │
│   └── src/
│       ├── main.tsx
│       ├── App.tsx
│       ├── index.css
│       │
│       ├── components/
│       │   └── ui/
│       │       ├── badge.tsx
│       │       ├── button.tsx
│       │       ├── dialog.tsx
│       │       ├── input.tsx
│       │       ├── label.tsx
│       │       └── sonner.tsx
│       │
│       ├── lib/
│       │   ├── api.ts
│       │   ├── queryClient.ts
│       │   ├── types.ts
│       │   └── utils.ts
│       │
│       └── pages/
│           ├── Home.tsx
│           └── Admin.tsx
│
├── backend/
│   ├── server.py
│   ├── seed.py
│   ├── requirements.txt
│   │
│   ├── models/
│   │   └── booking.py
│   │
│   ├── routers/
│   │   └── bookings.py
│   │
│   └── lib/
│       ├── db.py
│       └── dates.py
│
└── memory/
    ├── SPEC.md
    └── test_credentials.md
