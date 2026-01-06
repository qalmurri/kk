pyside_app/
│
├── app.py
│
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── session.py           
│   ├── exceptions.py
│
├── network/
│   ├── __init__.py
│   ├── api_client.py
│   ├── auth_service.py
│   ├── data_service.py
│
├── models/
│   ├── __init__.py
│   ├── table/
│   │   ├── __init__.py
│   │   └── item_table_model.py
│   │
│   └── domain/
│       ├── __init__.py
│       └── user.py
│
├── views/
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── login_window.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── main_window.py
│   │
│   └── widgets/
│       ├── __init__.py
│       ├── loading.py
│       └── message_box.py
│
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py
│   └── main_controller.py
│
├── utils/
│   ├── __init__.py
│   ├── datetime.py
│   ├── formatter.py
│   └── validators.py
│
├── workers/
│   └── __init__.py
│
├── resources/
│   ├── icons/
│   └── styles/
│       └── app.qss
│
└── requirements.txt