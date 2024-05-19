from django.contrib import admin
from jakis.models import Profil, Choices
# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    fields = ["name", "surname", "age"]
    readonly_fields = ["name", "age"]
    list_filter = ["age"]
admin.site.register(Profil)
admin.site.register(Choices)