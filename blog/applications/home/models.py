from django.db import models

# app terceros

from model_utils.models import TimeStampedModel

#######Modelo para pagina principal###########

class Home(TimeStampedModel): #ya trae los atributos fecha de modificaion y de creacion
    title = models.CharField('Nombre', max_length=50)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    conctact_email = models.EmailField('Email contacto', blank=True, null=True , max_length=50)
    phone = models.CharField('Telefono Contacto', max_length=30)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
    
    def __str__(self):
        return self.title

###########Modelo Subscripcion***********

class Suscribers(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriptor'
        verbose_name_plural = 'Subscriptores'
    
    def __str__(self):
        return self.email

###########Modelo Contacto***********

class Contact(TimeStampedModel):

    full_name = models.CharField('Nombres',max_length=40)
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        verbose_name = 'Conctacto'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.full_name