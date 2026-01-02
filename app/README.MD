pyside_app/
│
├── app.py                     # Entry point aplikasi
│
├── core/
│   ├── __init__.py
│   ├── config.py              # Global config (API, timeout, env)
│   ├── session.py             # Menyimpan user, token, ip
│   ├── exceptions.py          # Custom exception
│
├── network/
│   ├── __init__.py
│   ├── api_client.py          # HTTP client (requests / httpx)
│   ├── auth_service.py        # Login / logout
│   ├── data_service.py        # Fetch data utama
│
├── models/
│   ├── __init__.py
│   ├── table/
│   │   ├── __init__.py
│   │   └── item_table_model.py   # QAbstractTableModel
│   │
│   └── domain/
│       ├── __init__.py
│       └── user.py            # (opsional) domain object
│
├── views/
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── login_window.py    # Window login (IP + user + pass)
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── main_window.py     # Window utama (table, menu)
│   │
│   └── widgets/
│       ├── __init__.py
│       ├── loading.py
│       └── message_box.py
│
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py     # Logic login
│   └── main_controller.py     # Logic data load
│
├── utils/
│   ├── __init__.py
│   ├── datetime.py
│   ├── formatter.py
│   └── validators.py
│
├── resources/
│   ├── icons/
│   └── styles/
│       └── app.qss
│
└── requirements.txt