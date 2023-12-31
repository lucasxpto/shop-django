# Generated by Django 4.2.4 on 2023-09-12 22:01

from django.db import migrations
import dynamic_filenames
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_produto_foto_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto_capa',
            field=stdimage.models.StdImageField(default='images/produto_sem_foto.png', force_min_size=False, max_length=255, upload_to=dynamic_filenames.FilePattern(filename_pattern='{model_name:.30}/{uuid:base32}{ext}'), variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto do produto'),
        ),
    ]
