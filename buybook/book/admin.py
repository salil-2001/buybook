from django.contrib import admin

# from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import User,Book,Author


class UserAdmin(ModelAdmin):
        list_display = ('id', 'email', 'username', 'first_name', 'last_name' ,'account_status','profile_img')
        list_filter = ('is_superuser',)
        fieldsets = [
                (None, {'fields': ('email', 'password',)}),
                ('Personal info', {'fields': ('first_name', 'last_name', 'username','account_status','profile_img',)}),
                ('Permissions', {'fields': ('is_superuser',)}),
        ]

        add_fieldsets = (
                (None, {
                        'classes': ('wide',),
                        'fields': ( 'is_student','account_status','profile_img'),
                }),
        )
        search_fields = ('username',)
        ordering = ('id',)
        filter_horizontal = ()


admin.site.register(User, UserAdmin)
# admin.site.register(ModelAdmin)

      
@admin.register(Book)
class Books(admin.ModelAdmin):
        list_display=['id',"book_name","book_price","book_language","book_type","publish_date","book_image","author"]

@admin.register(Author)
class Authors(admin.ModelAdmin):
        list_display=['id',"name","age","birth_place","birth_date","death_date","country"]