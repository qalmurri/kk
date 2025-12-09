from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    """
    python manage.py shell
    from scripts.models import User
    User.objects.create_user(username="andi", password="12345")
    """
    first_name = None
    last_name = None
    last_login = None
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )