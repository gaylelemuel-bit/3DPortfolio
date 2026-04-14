from django.contrib import admin
from .models import Project, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'is_featured')
    list_editable = ('is_featured',)
    list_filter = ('is_featured', 'year')
    filter_horizontal = ('skills',)


admin.site.register(Skill)