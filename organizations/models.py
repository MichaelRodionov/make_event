from django.db import models


# ----------------------------------------------------------------
# organization model
class Organization(models.Model):
    """
    Model representing event

    Attrs:
        - title: organization title
        - description: organization description
        - address: organization address
        - postcode: organization postcode
    """
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание'
    )
    address = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Адрес'
    )
    postcode = models.CharField(
        max_length=10,
        verbose_name='Почтовый индекс'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: str = 'Организация'
        verbose_name_plural: str = 'Организации'
