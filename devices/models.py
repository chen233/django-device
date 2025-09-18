from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html


class test():
    id = 0


class Device(models.Model):
    name = models.CharField(max_length=128, verbose_name='设备名称', db_index=True)
    user_choice = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='上报人')
    buy_time = models.DateTimeField('购买时间', default=timezone.now)
    deadline = models.DateTimeField('到期时间', default=timezone.now)
    qr_code = models.ImageField(upload_to='qr_code', verbose_name='二维码', null=True)

    def qr_code_data(self):
        if self.qr_code == '':
            return format_html(
                '无照片上传'
            )
        elif self.qr_code.url != '/qr_code/null':
            return format_html(
                '<a href="{}" target="_blank"> <img src="{}" width="100px"/></a>',
                self.qr_code.url,
                self.qr_code.url,
            )
        else:
            return format_html(
                '无图片上传'
            )

    qr_code_data.short_description = '二维码照片'

    class Meta:
        verbose_name = "设备名称"
        verbose_name_plural = "设备管理"

    def __str__(self):
        print('调用__str__')
        test.id = str(self.id)
        print(self.id)
        print(test.id)
        return self.name
