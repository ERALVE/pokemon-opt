from django.contrib import admin
from .models import Register
# Register your models here.

#admin.site.register(Register)

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais','edad')
    list_filter = ('edad', 'pais')
    search_fields = ('nombre','pais')
    #fields = ('edad','nombre')
