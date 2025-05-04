from django.contrib import admin
from .models import Artiles
from .models import Comment


admin.site.register(Artiles)


class ArtilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_filter = ('category',)


admin.site.register(Comment)