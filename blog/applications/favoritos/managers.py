from django.db import models

class FavoritesManagers(models.Manager):

    def entradas_user(self, usuario):
        return self.filter(
            entry__public = True,
            user = usuario
        ).order_by('-created')