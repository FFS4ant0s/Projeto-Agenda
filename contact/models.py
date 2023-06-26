from django.db import models
from django.utils import timezone

# id (primary key)
# first_name (str), last_name (str), phone (str),
# email (email), created_date (date), description (text)
# category (foreing key), show (boolean), owner (foreing key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'