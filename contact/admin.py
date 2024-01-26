from django.contrib import admin
from .models import Contact, Category
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display        =  'id', 'first_name','last_name', 'create_date','email',
    ordering            =   'id',
    list_filter         =   'create_date',
    list_per_page       =   1
    list_max_show_all   =   10
    list_editable       =   'email',
    list_display_links  =   'id',



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display        =  'name',
    ordering            =   'id',
