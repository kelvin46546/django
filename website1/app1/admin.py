from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

    search_fields = ['title','length']

list_filter = ['release_year','length','title']


admin.site.register(models.Customer)

search_fields = ['first_name','last_name']

admin.site.register(models.Movie,MovieAdmin)
