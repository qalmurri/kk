from urllib.parse import parse_qs
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async

User = get_user_model()

@database_sync_to_async
def get_user(token):
    try:
        access_token = AccessToken(token)
        return User.objects.get(id=access_token["user_id"])
    except Exception:
        return None

class JwtAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query = parse_qs(scope["query_string"].decode())
        token = query.get("token")

        if token:
            scope["user"] = await get_user(token[0])
        else:
            scope["user"] = None

        return await super().__call__(scope, receive, send)
