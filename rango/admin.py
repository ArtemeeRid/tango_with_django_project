from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

admin.site.register(Category)
admin.site.register(Page, PageAdmin)

# Finally, register the PageAdmin class with Django’s admin interface.
# Youshouldmodifythelineadmin.site.register(Page). Changeit to
# admin.site.register(Page, PageAdmin) in Rango’s admin.py file.
# Licenced to University of Glasgow