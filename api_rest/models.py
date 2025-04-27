from django.db import models

class User(models.Model):

    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    senha_numerica = models.IntegerField()

    def __str__(self):
        return f'Nickname: {self.user_nickname}'