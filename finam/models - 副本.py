from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils.html import format_html


class Record(models.Model):
    type_choices1 = (
        (0, '鄞州公路段'),
        (1, '海曙公路段'),
        (2, '江北公路段'),
        (3, '镇海公路段'),
    )
    type = models.IntegerField(verbose_name='所属项目', choices=type_choices1)

    create_date = models.DateTimeField(verbose_name='时间', auto_now=True)

    type_choices2 = (
        (0, '死机'),
        (1, '断电'),
        (2, '无法ping通'),
        (3, '无法判断，需要现场查看'),
    )

    typename = models.SmallIntegerField(verbose_name='故障类型', choices=type_choices2)

    name = models.CharField(verbose_name='地点', max_length=128)
    money = models.TextField(verbose_name='故障描述', max_length=128)
    type_choices3 = (
        (0, '未解决'),
        (1, '已解决'),
    )

    # type_choices3.boolean = True
    solve = models.SmallIntegerField(verbose_name='是否解决', choices=type_choices3, default=0)

    user_choice = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='上报人')
    img = models.ImageField(upload_to='img/%Y/%m/%d',verbose_name='现场照片')

    # 图片显示，并在admin中加入列表及重构readonly_fields
    def image_data(self):
        return format_html(
            '<a href="{}" target="_blank"> <img src="{}" width="100px"/></a>',
            self.img.url,
            self.img.url,
        )
    image_data.short_description = '图片'

    def all_in(self):
        return format_html(
            '<button type="button" class="el-button el-button--primary">详情</button>'
        )
    all_in.short_description = '详情'

    class Meta:
        verbose_name = "故障"
        verbose_name_plural = "故障信息"

    def __str__(self):
        return self.name
