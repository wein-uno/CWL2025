from django.contrib import admin

from .models import Comics

class ComicsAdmin(admin.ModelAdmin)
    list_display = ('title', 'number','grade', 'price')

admin.site.register(Comics, ComicsAdmin)
