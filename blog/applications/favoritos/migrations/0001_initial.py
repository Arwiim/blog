# Generated by Django 3.0.3 on 2020-04-12 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_favorites', to='entrada.Entry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entrada Favorita',
                'verbose_name_plural': 'Entradas Favoritas',
                'unique_together': {('user', 'entry')},
            },
        ),
    ]
