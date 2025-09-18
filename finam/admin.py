from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from threading import Timer


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Record
        # articleObj.user = request.user


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name', 'create_time')


@admin.register(BugName1)
class BugTypeAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name', 'create_time')


@admin.register(AddMap)
class addmapadmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Devicename)
class deviceadmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.
@admin.register(Record)
# class RecordAdmin(admin.ModelAdmin):
# class RecordAdmin(ImportExportModelAdmin):
class RecordAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    fieldsets = (
        ['故障信息', {
            'fields': (
                'type', 'provience', 'city', 'device', 'typename', 'money', 'user_choice', 'solve', 'send', 'img',
                'image_data',
            )
        }],
        ['维护信息', {
            'fields': ('CREATED_TIME', 'UPDATED_BY', 'SOLVED_TIME', 'UPDATED_money', 'img_over', 'image_overdata')
        }]
    )
    list_display = ('id', 'type', 'provience', 'city', 'device', 'typename',
                    'solve', 'send', 'image_data', 'user_choice', 'CREATED_TIME', 'UPDATED_BY', 'SOLVED_TIME',
                    'all_in',
                    'image_overdata')

    list_per_page = 10
    list_filter = ('type', 'provience', 'city', 'device', 'typename',
                   'solve', 'send', 'user_choice', 'CREATED_TIME', 'UPDATED_BY', 'SOLVED_TIME',
                   )

    list_editable = ('solve',)
    list_display_links = ('id', 'all_in')
    date_hierarchy = 'CREATED_TIME'
    readonly_fields = ('UPDATED_BY', 'image_data', 'image_overdata')
    ordering = ('-CREATED_TIME',)

    # 获取登录人员信息，进行填充，需要重写save_model方法,同时记得设定成只读字段
    def save_model(self, request, obj, form, change):
        def task():
            f = open('D:/test.txt')
            xx = f.read()

            # Text消息@所有人
            if xx:
                print('发送提醒')
                print(xx)
                # xiaoding.send_markdown(title='运维提醒', text=xx)

        Timer(1, task, ()).start()

        obj.UPDATED_BY = request.user.username
        obj.save()
