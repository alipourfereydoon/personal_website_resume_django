from django.contrib import admin
from . models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','father_name','nationalcode')
