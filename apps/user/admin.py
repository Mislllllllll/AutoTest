from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import UserProfile,EmailVerifyRecord,Banner
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'gender', 'mobile','image']
    search_fields = ['username', 'password', 'gender', 'mobile','image']
    list_filter = ['username', 'password', 'gender', 'mobile','image']

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


