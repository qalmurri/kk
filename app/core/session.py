import requests
from PySide6.QtCore import QSettings
from core.config import (
    APP_NAME, ORG_NAME, KEY_BACKEND_IP, KEY_ACCESS_TOKEN, KEY_REFRESH_TOKEN, DEFAULT_BACKEND_IP
)

s = QSettings(ORG_NAME, APP_NAME)
print(s.allKeys())

class Session:
    _settings = QSettings(ORG_NAME, APP_NAME)

    @classmethod
    def set_backend_ip(cls, ip: str):
        cls._settings.setValue(KEY_BACKEND_IP, ip)

    @classmethod
    def get_backend_ip(cls) -> str:
        return cls._settings.value(KEY_BACKEND_IP, DEFAULT_BACKEND_IP)
    
    @classmethod
    def set_tokens(cls, access: str, refresh: str):
        cls._settings.setValue(KEY_ACCESS_TOKEN, access)
        cls._settings.setValue(KEY_REFRESH_TOKEN, refresh)

    @classmethod
    def get_access_token(cls) -> str | None:
        return cls._settings.value(KEY_ACCESS_TOKEN)
    
    @classmethod
    def get_refresh_token(cls) -> str | None:
        return cls._settings.value(KEY_REFRESH_TOKEN)
    
    @classmethod
    def clear_tokens(cls):
        cls._settings.remove(KEY_ACCESS_TOKEN)
        cls._settings.remove(KEY_REFRESH_TOKEN)

    @classmethod
    def is_logged_in(cls) -> bool:
        return cls.get_access_token() is not None
    
    @classmethod
    def save_main_window_size(cls, size):
        cls._settings.setValue("main_window/size", size)

    @classmethod
    def load_main_window_size(cls):
        return cls._settings.value("main_window/size")
    
    @classmethod
    def set_scripts_last_tab(cls, index: int):
        cls._settings.setValue("scripts/last_tab", index)

    @classmethod
    def get_scripts_last_tab(cls):
        return cls._settings.value("scripts/last_tab", 0, type=int)

    @classmethod
    def set_table_column_width(cls, tab_name: str, column_id: str, width: int):
        key = f"scripts/tabs/{tab_name}/columns/{column_id}"
        cls._settings.setValue(key, width)

    @classmethod
    def get_table_column_width(cls, tab_name: str, column_id: str) -> int | None:
        key = f"scripts/tabs/{tab_name}/columns/{column_id}"
        return cls._settings.value(key, None, type=int)

    @classmethod
    def get(cls, url, params=None):
        headers = {}

        token = cls.get_access_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        return requests.get(url, params=params, headers=headers)
