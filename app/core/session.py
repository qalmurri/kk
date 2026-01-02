class Session:
    user = None
    token = None
    server_ip = None

    @classmethod
    def set_user(cls, data, ip):
        cls.user = data.get("user")
        cls.token = data.get("token")
        cls.server_ip = ip
