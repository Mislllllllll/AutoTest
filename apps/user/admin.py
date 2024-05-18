from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import UserProfile,EmailVerifyRecord,Banner
from django.contrib.auth.admin import UserAdmin
class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'password', 'gender', 'mobile','image','email']
    search_fields = ['username', 'password', 'gender', 'mobile','image','email']
    list_filter = ['username', 'password', 'gender', 'mobile','image','email']

admin.site.register(UserProfile,UserProfileAdmin)

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display=['code','email','send_type','send_time']
    search_fields = ['code','email','send_type','send_time']
    list_filter = ['code','email','send_type','send_time']

admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index','add_time']
    list_filter = ['title', 'image', 'url', 'index','add_time']

admin.site.register(Banner,BannerAdmin)


