from django.contrib import admin
from .models import *
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

# admin.site.register(Genre, MPTTModelAdmin)

admin.site.register(
    Genre,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Article)
