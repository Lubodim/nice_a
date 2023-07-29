from django.contrib import admin

from nice_a.pets.models import Pet


# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
