from django.contrib import admin
from .models import post



# Register your models here.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ""
    list_display = ("titel","author",  "created_date", "published_date")
    list_filter = ( "created_date", "published_date")
    search_fields = ("titel", "created_date")
 




admin.site.register(post, PostAdmin)


