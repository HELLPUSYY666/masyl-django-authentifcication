from django.db import models


class Masyli(models.Model):
    KOLO = 'KOLO'
    OPAS = 'OPAS'
    NEIZ = 'NEIZ'
    NEIT = 'NEIT'
    BEZO = 'BEZO'
    class_masi = [
        (KOLO, 'kolosalni'),
        (OPAS, 'opasni'),
        (NEIZ, 'neizvestni'),
        (NEIT, 'neitral'),
        (BEZO, 'bezopasni')
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    color = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    opasnosti = models.CharField(max_length=4, choices=class_masi, default=OPAS)
    photo = models.ImageField(upload_to='masyli_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class SupernaturalAbilities(models.Model):
    masyli = models.ForeignKey(Masyli, on_delete=models.CASCADE, null=True)
    ability_name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='supernatural_photos/', blank=True, null=True)

    def __str__(self):
        return self.ability_name
