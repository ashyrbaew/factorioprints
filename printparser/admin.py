from django.contrib import admin
from .models import Prints


@admin.register(Prints)
class PrintsAdmin(admin.ModelAdmin):
    list_display = [
        'author', 'short_details', 'short_blueprint', 'image',
        'created_at', 'updated_at', 'favorites'
    ]
