from django.db import models

from organizations.models import Organization


# ----------------------------------------------------------------
# event model
class Event(models.Model):
    """
    Model representing event

    Attrs:
        - title: Event title
        - description: event description
        - organizations: defines list with related organizations
        - image: event image logo
        - date: define datetime of event
    """
    title = models.CharField(
        max_length=50,
        verbose_name='Мероприятие'
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание'
    )
    organizations = models.ManyToManyField(
        Organization,
        related_name='events',
        verbose_name='Организации'
    )
    image = models.ImageField(
        upload_to='logos/',
        verbose_name='Логотип',
        null=True
    )
    date = models.DateTimeField(
        verbose_name='Дата проведения',
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: str = 'Мероприятие'
        verbose_name_plural: str = 'Мероприятия'
