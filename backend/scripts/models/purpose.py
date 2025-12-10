from django.db import models

class Purpose(models.Model): #MigrateDone
    code = models.IntegerField(db_index=True)
    sum = models.IntegerField()
    purpose = models.CharField(
        max_length=255
    )
    class Meta:
        unique_together = (
            'code',
            'sum',
            'purpose'
        )