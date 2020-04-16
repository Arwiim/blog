from django.db import models

class EntryManager(models.Manager):
    #Procedimientos para entrada

    def entrada_en_portada(self):
        return self.filter(
            public = True,
            portada = True,    
        ).order_by('-created').first() #Ordenar por fecha de mificacion y traer el ultimo
    
    def entradas_en_home(self):
        #devuelve las ultimas 4 entradas en home
        return self.filter(
            public = True,
            in_home = True,
        ).order_by('-created')[:4]

    def entradas_recientes(self):
        #entradas recientes 5
        return self.filter(
            public = True,
        ).order_by('-created')[:6]
    
    def buscar_entrada(self,kword,categoria):
        #procedimiento para buscar entradas por categoria o palabra clave
        if len(categoria) > 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')