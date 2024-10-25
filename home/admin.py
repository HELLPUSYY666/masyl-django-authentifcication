from django.contrib import admin
from .models import Masyli, SupernaturalAbilities
from django.db.models import QuerySet


@admin.register(Masyli)
class MasyliAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'origin', 'age_status', 'opasnosti')
    list_editable = ('age', 'origin', 'opasnosti')
    ordering = ['-age']
    list_per_page = 5
    search_fields = (['name'])

    @admin.display(ordering='-age', description='Возрастной статус')
    def age_status(self, masi):
        if masi.age < 18:
            return 'Совсем карапуз'
        elif masi.age < 30:
            return 'Подросток мась'
        elif masi.age < 45:
            return 'Мась в самом соку'
        else:
            return 'Великий мась'

    @admin.action(description='Установить уровень опасности')
    def set_opasnosti(self, request, qr: QuerySet):
        qr.update(currency=Masyli.OPAS)


@admin.register(SupernaturalAbilities)
class SupernaturalAbilitiesAdmin(admin.ModelAdmin):
    list_display = ('masyli', 'ability_name')
    list_editable = ('ability_name',)
