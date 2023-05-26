# Generated by Django 3.2 on 2023-05-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Мероприятие')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(null=True, upload_to='logos/', verbose_name='Логотип')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата проведения')),
                ('organizations', models.ManyToManyField(related_name='events', to='organizations.Organization', verbose_name='Организации')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]