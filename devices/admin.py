from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from threading import Timer
import os


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    fieldsets = (
        ['设备信息', {
            'fields': (
                'name', 'user_choice', 'buy_time', 'deadline', 'qr_code_data'
            )
        }],
    )
    list_display = ('id', 'name', 'user_choice', 'buy_time', 'deadline', 'qr_code_data')
    readonly_fields = ('qr_code_data', 'qr_code')
    ordering = ('deadline',)

    def save_model(self, request, obj, form, change):

        def task():
            id = str(test.id)
            print(id)
            os.system(
                'myqr http://47.99.242.187:8000/devices/device/' + id + '/change/ ' + '-n newdevice' + id + '.png -d upload/qr_code/')
            # os.system('myqr http://localhost:8000/devices/device/' + id + '/change/ ' + '-n 新设备' + id + '.png')
            print(
                'myqr http://47.99.242.187:8000/devices/device/' + id + '/change/ ' + '-n newdevice' + id + '.png -d upload/qr_code/')
            print('已生成二维码')
            device = Device.objects.get(id=id)
            print(device)
            device.qr_code = 'qr_code/newdevice' + str(test.id) + '.png'
            device.save()
            print('路径更新')

            # obj.qr_code = '/img/qr_code/新设备' + str(test.id) + '.png'
        Timer(1, task, ()).start()
        obj.save()
        print('保存')

