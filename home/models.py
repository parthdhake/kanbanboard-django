from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    # board_id = models.AutoField(primary_key=True, default=uui)
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


PRIORITY_CHOICES = (
    ('high', 'HIGH'),
    ('medium', 'MEDIUM'),
    ('low', 'LOW'),
)

COLOR_CHOICES = {
    ('green', 'GREEN'),
    ('white', 'WHITE'),
    ('red', 'RED'),
}

STATUS_CHOICES = (
    ('to do', 'TO DO'),
    ('in progress', 'IN PROGRESS'),
    ('completed', 'COMPLETED'),
    ('done', 'DONE'),
)


class Card(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    priority = models.CharField(max_length=6,
                                choices=PRIORITY_CHOICES,
                                default='medium')
    status = models.CharField(max_length=11,
                              choices=STATUS_CHOICES,
                              default='to do')
    color = models.CharField(max_length=6,
                             choices=COLOR_CHOICES,
                             default='white')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)