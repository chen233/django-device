from django.db import models
from django import forms
# Create your models here.
from django.utils.html import format_html


class table_view(models.Model):
    # time_map=models.DateTimeField(verbose_name='勘察时间')

    type_map = models.CharField(verbose_name='地点', max_length=128)
    name_map = models.CharField(verbose_name='工程名称', max_length=128)

    type_choices1 = (
        (0, '鄞州公路段'),
        (1, '海曙公路段'),
        (2, '江北公路段'),
        (3, '镇海公路段'),
    )
    type_map_choices = models.IntegerField(verbose_name='所属项目', choices=type_choices1)

    id_map = models.CharField(verbose_name='点位编号', max_length=128)
    install_map = models.CharField(verbose_name='安装方式', max_length=128)
    install_map_1 = models.CharField(verbose_name='安装位置', max_length=128)
    # install_map_xy=models.CharField(verbose_name='安装位置',max_length=128)
    type_choices_map = (
        (0, '高清球机'),
        (1, '高清枪机'),
        (2, '传感器'),
    )
    type = models.IntegerField(verbose_name='设备类型', choices=type_choices_map)

    Pixel_map = (
        (0, '200万'),
        (1, '300万'),
        (2, '900万'),
    )
    night_map = (
        (0, '红外'),
        (1, '无'),
    )
    if type_choices_map != 2:
        Pixel = models.IntegerField(verbose_name='像素', choices=Pixel_map, null=True, default='null', blank=True)
        night = models.IntegerField(verbose_name='夜视', choices=night_map, null=True, default='null', blank=True)

    Electrical_type_choices = (
        (0, '民电'),
        (1, '市政'),
        (2, '单位'),
        (3, '供电所'),
        (4, '太阳能'),
        (5, '村里用电')
    )
    Electrical_type = models.IntegerField(verbose_name='接电类型', choices=Electrical_type_choices)
    phone_number_map = models.CharField(max_length=12, verbose_name='联系方式')
    electrical_map = models.CharField(max_length=128, verbose_name='接电位置')
    electrical_max = models.CharField(max_length=128, verbose_name='电源长度')
    net_max = models.CharField(max_length=128, verbose_name='网线长度')
    Carrier_map = models.CharField(max_length=128, verbose_name='运营商链路')

    img = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='安装环境简易图', null=True, default='null', blank=True)
    img1 = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='安装环境照片', null=True, default='null', blank=True)

    # 图片显示，并在admin中加入列表及重构readonly_fields
    def image_map(self):
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

    image_map.short_description = '安装环境简易图'

    def image_map1(self):
        if self.img1.url != '/img/null':
            return format_html(
                '<a href="{}" target="_blank"> <img src="{}" width="100px"/></a>',
                self.img1.url,
                self.img1.url,
            )
        else:
            return format_html(
                '无照片上传'
            )

    image_map1.short_description = '安装环境照片'

    def all_in_map(self):
        return format_html(
            '<button type="button" class="el-button el-button--primary">详情</button>'
        )

    all_in_map.short_description = '详情'

    class Meta:
        verbose_name = "勘察表"
        verbose_name_plural = "现场勘察信息"
