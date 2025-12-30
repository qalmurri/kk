from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPresence(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)
