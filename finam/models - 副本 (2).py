from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from dingtalkchatbot.chatbot import DingtalkChatbot
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# 'sender'包含了这个动作发生时传入的参数
# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=a24c7fdb0ad801e7cc038ea46ea8e333d58ce87f50143b0e90c17c769c8832ed'
secret = 'SECa15b5a94f259ad9fb4134ac7a9cbd251824845697bef3ee31d02003edc33a6f4'  # 可选：创建机器人勾选“加签”选项时使用
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）


class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='所属项目', help_text='所属项目名字应该唯一', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "所属项目"
        verbose_name_plural = "项目管理"

    def __str__(self):
        return self.name


class BugName1(models.Model):
    name = models.CharField(max_length=128, verbose_name='故障类型', help_text='故障类型名字应该唯一', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "故障类型"
        verbose_name_plural = "故障类型管理"

    def __str__(self):
        return self.name


class Devicename(models.Model):
    name = models.CharField(max_length=128, verbose_name='设备名称', unique=True, db_index=True)

    class Meta:
        verbose_name = "设备名称"
        verbose_name_plural = "设备管理"

    def __str__(self):
        return self.name


# 点位信息


class AddMap(models.Model):
    name = models.CharField(max_length=200, verbose_name='点位名称')

    class Meta:
        verbose_name = "点位"
        verbose_name_plural = "点位管理"

    def __str__(self):
        return self.name


class Record(models.Model):
    type = models.ForeignKey(Department, verbose_name='所属项目', on_delete=models.CASCADE)

    provience = models.CharField(max_length=200, verbose_name='点位名称')
    city = models.CharField(max_length=200, verbose_name='点位桩号')

    device = models.ForeignKey(Devicename, verbose_name='设备名称', on_delete=models.CASCADE)

    typename = models.ForeignKey(BugName1, verbose_name='故障类型', on_delete=models.CASCADE)

    money = models.TextField(verbose_name='故障描述', max_length=500)

    type_choices3 = (
        ('未解决', '未解决'),
        ('已解决', '已解决'),
    )

    solve = models.CharField(verbose_name='是否解决', choices=type_choices3, default=0, max_length=128)

    user_choice = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='上报人')

    img = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='现场照片', null=True, default='null', blank=True)

    # 图片显示，并在admin中加入列表及重构readonly_fields
    def image_data(self):
        if self.img.url != '/img/null':
            return format_html(
                '<a href="{}" target="_blank"> <img src="{}" width="100px"/></a>',
                self.img.url,
                self.img.url,
            )
        else:
            return format_html(
                '无照片上传'
            )

    image_data.short_description = '图片'

    def all_in(self):
        return format_html(
            '<button type="button" class="el-button el-button--primary">详情</button>'
        )

    all_in.short_description = '详情'

    # 自动填充字段 eg:修改某条记录时，自动填充修改人为登录用户
    # 时间字段处理，需要在model中指定，例如自动更新时间需要增加 auto_now属性,django使用的时间函数 timezone.now
    CREATED_TIME = models.DateTimeField('创建时间', default=timezone.now)  # 创建时间
    UPDATED_BY = models.CharField('更新人', max_length=32)  # 更新人
    UPDATED_TIME = models.DateTimeField('解决时间', auto_now_add=False, null=True, blank=True)  # 解决时间
    UPDATED_money = models.TextField(verbose_name='解决过程描述', max_length=500, null=True, blank=True)
    img_over = models.ImageField(upload_to='img_over/%Y/%m/%d', verbose_name='现场解决照片', null=True, default='null',
                                 blank=True)

    # 图片显示，并在admin中加入列表及重构readonly_fields
    def image_overdata(self):
        if self.img_over.url != '/img_over/null':
            return format_html(
                '<a href="{}" target="_blank"> <img src="{}" width="100px"/></a>',
                self.img_over.url,
                self.img_over.url,
            )
        else:
            return format_html(
                '无照片上传'
            )

    image_overdata.short_description = '现场解决照片'

    class Meta:
        verbose_name = "故障"
        verbose_name_plural = "故障信息"

    def __str__(self):
        type_name = str(self.type)
        typename_name = str(self.typename)
        device_name = str(self.device)
        map_name = str(self.provience) + str(self.city)
        money = str(self.money)
        img_url = str(self.img)
        print(img_url)

        if img_url == 'null':
            xx = '无照片'
        else:
            xx = '![现场图片](' + 'http://47.99.242.187' + ':8000/img/' + img_url

        f = open('D:/test.txt', 'w')

        f.write(
            '新增' + type_name + '故障' + "\r\r>"
            + '点位：' + map_name + "\r\r>"
            + '设备名称：' + device_name + "\r\r>"
            + '故障类型:' + typename_name + "\r\r>"
            + '故障描述:' + money + "\r\r>"
            + xx + ')'
        )
        f.close()

        return str(self.provience) + ' ' + str(self.city)


print(ip)
