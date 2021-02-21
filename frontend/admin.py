from django.contrib import admin
from .models import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','img_url','what_i_do','about_me')

admin.site.register(Person,PersonAdmin)

class ExprienceAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Exprience,ExprienceAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title' , 'description')

admin.site.register(Project,ProjectAdmin)