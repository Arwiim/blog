from applications.home.models import Home

# procesor para recuperar telefono y correo del registro home

def home_contact(request):#funcion para escribir un proceso
    home = Home.objects.latest('created')
    return{
        'phone' : home.phone,
        'email' : home.conctact_email
    }