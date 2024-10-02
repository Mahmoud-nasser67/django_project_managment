from django.contrib import admin
from django.db.models import Count

from .models import Progect,category,task
# Register your models here.
admin.site.register(category)

@admin.register(Progect)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','statues','create_at','updata_at','category','user','tasks_count']
    list_per_page = 4
    list_editable = ['statues','category']
    list_select_related = ['user','category']
    def tasks_count(self,obj):
        return obj.tasks_count

    #بيجيب عدد التاسك لكل مشروع ب استعلام واحد فقط
    def get_queryset(self, request):
        query=super().get_queryset(request)
        query=query.annotate(tasks_count=Count('task'))
        return query

@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display = ['id','description','is_complete','project']
    list_per_page = 2
    list_editable = ['is_complete']
