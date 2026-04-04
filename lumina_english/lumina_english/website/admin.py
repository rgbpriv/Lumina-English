from django.contrib import admin
from .models import SimpleText, CourseCard


@admin.register(SimpleText)
class SimpleTextAdmin(admin.ModelAdmin):
	list_display = ('title', 'pk')


@admin.register(CourseCard)
class CourseCardAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'highlight')
