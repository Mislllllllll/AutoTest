from django.contrib import admin

# Register your models here.
from django.contrib.admin.models import  LogEntry

from django.utils.html import format_html
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
from django.contrib.admin import  DateFieldListFilter


class CustomDateRangeFilter(DateFieldListFilter):
    title = _('时间范围')

    def __init__(self,*args,**kwargs):
        super(CustomDateRangeFilter,self).__init__(*args,**kwargs)





@admin.register(LogEntry)
class LogOperateAdmin(admin.ModelAdmin):
    list_display = ('action_time','content_type','user','get_edited_object','__str__')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def view_link(self,obj):
        if obj.action_flag!=3 and obj.object_id:
            ct=obj.content_type
            view_url=reverse('admin:%s_%s_change'%(ct.app_label,ct.model),args=[obj.object_id])
            return format_html('<a href="{}">View</a>',view_url)
        return ""

    list_display+=('view_link',)

