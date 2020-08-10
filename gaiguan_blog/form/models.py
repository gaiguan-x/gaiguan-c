from django.db import models


# 存储用户信息表
class UserInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名", null=True)
    age = models.IntegerField(verbose_name="年龄", null=True)
    sex = models.CharField(max_length=5, verbose_name="性别", null=True)
    school = models.CharField(max_length=50, verbose_name="学校", null=True)
    address = models.CharField(max_length=100, verbose_name="地址", null=True)
    hobby = models.CharField(max_length=500, verbose_name="爱好", null=True)
    # 特长
    strong_point = models.CharField(max_length=500, verbose_name="特长", null=True)
    date = models.DateField(verbose_name="日期", null=True)
    city = models.CharField(max_length=20, verbose_name="城市", null=True)
    phone = models.CharField(max_length=20, verbose_name="电话", null=True)
    # 邮编
    postal_code = models.IntegerField(verbose_name="邮编", null=True)
    mail = models.CharField(max_length=50, verbose_name="邮箱", null=True)
    text = models.TextField(verbose_name="普通文本", null=True)

    class Meta:
        verbose_name_plural = '表单对应的用户信息'


# 制作表单的表
class Field(models.Model):
    """
    字段被选择或者不被选择
    """
    title = models.CharField(max_length=50, verbose_name="标题")
    name = models.BooleanField(default=False, verbose_name="姓名")
    age = models.BooleanField(default=False, verbose_name="年龄")
    sex = models.BooleanField(default=False, verbose_name="性别")
    school = models.BooleanField(default=False, verbose_name="学校")
    address = models.BooleanField(default=False, verbose_name="地址")
    hobby = models.BooleanField(default=False, verbose_name="爱好")
    # 特长
    strong_point = models.BooleanField(default=False, verbose_name="特长")
    date = models.BooleanField(default=False, verbose_name="日期")
    city = models.BooleanField(default=False, verbose_name="城市")
    phone = models.BooleanField(default=False, verbose_name="手机")
    # 邮编
    postal_code = models.BooleanField(default=False, verbose_name="邮编")
    mail = models.BooleanField(default=False, verbose_name="邮箱")
    text = models.BooleanField(default=False, verbose_name="普通文本")
    # 是否在使用
    is_used = models.BooleanField(default=True, verbose_name="是否启用本表单")

    class Meta:
        verbose_name_plural = '动态修改表单'


# 城市表
class City(models.Model):
    province = models.CharField(max_length=50, verbose_name="省份")
    city = models.CharField(max_length=50, verbose_name="城市")
    district = models.CharField(max_length=50, verbose_name="区域")

    class Meta:
        verbose_name_plural = "城市数据表"
