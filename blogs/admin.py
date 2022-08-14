from django.contrib import admin
from blogs.models import *
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog,BlogAdmin)
admin.site.register(comment)

class catergoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categorie',)}
admin.site.register(category,catergoryAdmin)