# Generated by Django 2.2.12 on 2020-05-17 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200516_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='link',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(default=' ', max_length=256, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]