from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import posttest, Category


# @admin.register(post)
class PosttestAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("titel", "created_date", "published_date")
    list_filter = ("created_date", "published_date")
    search_fields = ("titel", "created_date")


admin.site.register(Category)
admin.site.register(posttest, PosttestAdmin)
