from django.db import models
from datetime import date


# Create your models here.
class Breakfast(models.Model):
    """Definición del modelo desayuno"""

    day = models.DateField("Dia", default=date.today(), unique=True)
    bread = models.CharField("Pan", max_length=50, blank=True)
    drinks = models.CharField("Refresco", max_length=50, blank=True)
    other = models.CharField("Otros", max_length=50, blank=True)

    class Meta:
        verbose_name = "Desayuno"
        verbose_name_plural = "Desayunos"
        db_table = "desayuno"

    def __str__(self):
        return (
            "Desayuno del dia "
            + str(self.day.day)
            + " del mes "
            + str(self.day.month)
            + " del "
            + str(self.day.year)
        )


class Lunch(models.Model):
    """Definición del modelo almuerzo"""

    day = models.DateField("Dia", default=date.today(), unique=True)
    rice = models.CharField("Arroz", max_length=50, blank=True)
    broth = models.CharField("Caldo", max_length=50, blank=True)
    bread = models.CharField("Pan", max_length=50, blank=True)
    main_dish = models.CharField("Plato principal", max_length=50, blank=True)
    drink = models.CharField("Refresco", max_length=50, blank=True)
    other = models.CharField("Otros", max_length=50, blank=True)
    dessert = models.CharField("Postre", max_length=50, blank=True)

    class Meta:
        verbose_name = "Almuerzo"
        verbose_name_plural = "Almuerzos"
        db_table = "almuerzo"

    def __str__(self):
        return (
            "Almuerzo del dia "
            + str(self.day.day)
            + " del mes "
            + str(self.day.month)
            + " del "
            + str(self.day.year)
        )


class Dinner(models.Model):
    """Definición del modelo comida"""

    day = models.DateField("Dia", default=date.today(), unique=True)
    rice = models.CharField("Arroz", max_length=50, blank=True)
    broth = models.CharField("Caldo", max_length=50, blank=True)
    bread = models.CharField("Pan", max_length=50, blank=True)
    main_dish = models.CharField("Plato principal", max_length=50, blank=True)
    drink = models.CharField("Refresco", max_length=50, blank=True)
    other = models.CharField("Otros", max_length=50, blank=True)
    dessert = models.CharField("Postre", max_length=50, blank=True)

    class Meta:
        verbose_name = "Comida"
        verbose_name_plural = "Comidas"
        db_table = "comida"

    def __str__(self):
        return (
            "Comida del dia "
            + str(self.day.day)
            + " del mes "
            + str(self.day.month)
            + " del "
            + str(self.day.year)
        )
