from django.db import models

# Create your models here.
class HairCutting(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Haircuts & Hairdressing'

    def __str__(self):
        return self.name    


class HairColouring(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Colouring & Highlights'

    def __str__(self):
        return self.name 


class Eyebrows(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural= 'Eyebrows & Eyelashes'

    def __str__(self):
        return self.name


class LadiesWaxing(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = "Ladie's Waxing"

    def __str__(self):
        return self.name

    
class WaxPackage(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Ladies Waxing - Packages'

    def __str__(self):
        return self.name


class MensWaxing(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = "Men's Waxing"

    def __str__(self):
        return self.name


class Massage(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Massage'

    def __str__(self):
        return self.name


class NonPurchasable(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Non-Purchasable'

    def __str__(self):
        return self.name


class TeamWorkOne(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length= 200)
    photo = models.ImageField(upload_to='img')

    class Meta:
        verbose_name_plural = 'Team Work One'

    def __str__(self):
        return self.name


class TeamWorkTwo(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length= 200)
    photo = models.ImageField(upload_to='img')

    class Meta:
        verbose_name_plural = 'Team Work Two'

    def __str__(self):
        return self.name


class TeamWorkThree(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length= 200)
    photo = models.ImageField(upload_to='img')

    class Meta:
        verbose_name_plural = 'Team Work Three'

    def __str__(self):
        return self.name
