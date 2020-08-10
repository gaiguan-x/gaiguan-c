#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 常规模块的引入分为三部分，依次为：
# Python内置模块（如json、datetime）、第三方模块（如Django）、自己写的模块

from django.db import models  # 创建Django模型


class CompanyInfo(models.Model):
    """公司基本信息"""
    name = models.CharField(verbose_name='盖冠政务', max_length=50)  # 在生成数据表时，会创建名为name的字段，字符串类型，长度为50
    info1 = models.CharField(verbose_name='简介1', max_length=200)
    info2 = models.CharField(verbose_name='简介2', max_length=200)
    img = models.ImageField(verbose_name='背景图', upload_to='imgs')  # 图片格式，在后台上传图片时，会验证文件类型
    phone = models.CharField(verbose_name='联系电话', max_length=100)
    address = models.CharField(verbose_name='联系地址', max_length=200)
    web = models.CharField(verbose_name='政务官网', max_length=200)

    class Meta:  # 元类，可定义该模块的基本信息
        verbose_name = '盖冠政务'    # 名称
        verbose_name_plural = verbose_name   # 复数名称

    def __str__(self):    # 当print输出实例对象，或str() 实例对象时，调用这个方法
        return self.name


class Supers(models.Model):
    """盖冠政务优势"""
    info = models.CharField(verbose_name='优势', max_length=30)
    content = models.CharField(verbose_name='内容', max_length=50)

    class Meta:
        verbose_name = '盖冠政务优势'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.info


class Aboutus(models.Model):
    """关于盖冠政务"""
    title = models.CharField(verbose_name='服务项目', max_length=50)

    class Meta:
        verbose_name = '关于盖冠政务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Services(models.Model):
    """主要服务"""
    title = models.CharField(verbose_name='服务项目', max_length=10)
    info = models.CharField(verbose_name='简介', max_length=50)

    class Meta:
        verbose_name = '主要服务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Customers(models.Model):
    """客户"""
    name = models.CharField(verbose_name='服务群体', max_length=10)
    img = models.ImageField(verbose_name='图片', upload_to='imgs')
    info = models.CharField(verbose_name='服务内容', max_length=50)
    url = models.URLField(verbose_name='链接', max_length=200)

    class Meta:
        verbose_name = '服务群体'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Pricing(models.Model):
    """服务收费"""
    info = models.CharField(verbose_name='服务内容', max_length=50)
    item = models.CharField(verbose_name='所属分类', choices=(('sta', '标准套餐'), ('upd', '升级套餐')), default='sta',
                            max_length=5)

    class Meta:
        verbose_name = '服务收费'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.info


class Employees(models.Model):
    """员工展示"""
    name = models.CharField(verbose_name='姓名', max_length=50)
    img = models.ImageField(verbose_name='头像', upload_to='imgs')
    info = models.CharField(verbose_name='简介', max_length=50)
    post = models.CharField(verbose_name='职位', max_length=50)

    class Meta:
        verbose_name = '员工展示'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Contact(models.Model):
    """客户联系"""
    name = models.CharField(verbose_name='姓名', max_length=50)
    email = models.EmailField(verbose_name='邮箱')
    subject = models.CharField(verbose_name='主题', max_length=100)
    msg = models.TextField(verbose_name='信息内容')

    class Meta:
        verbose_name = '客户联系'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
