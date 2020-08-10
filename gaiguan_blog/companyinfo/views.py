#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render  # 用于页面后台渲染
from django.views.generic import View  # 使用Django自带的视图处理不同类型的请求
from django.http import JsonResponse  # 用于返回json数据

from .models import CompanyInfo, Supers, Aboutus, Services, Customers, Pricing, Employees, Contact


class Index(View):
    """首页"""

    def get(self, request):
        companyinfo = CompanyInfo.objects.all()[0]
        supers = Supers.objects.all()
        aboutus = Aboutus.objects.all()
        services = Services.objects.all()
        customers = Customers.objects.all()
        pricing_stas = Pricing.objects.filter(item='sta')
        pricing_upds = Pricing.objects.filter(item='upd')
        employees = Employees.objects.all()

        content = {
            'companyinfo': companyinfo,
            'supers': supers,
            'aboutus': aboutus,
            'services': services,
            'customers': customers,
            'pricing_stas': pricing_stas,
            'pricing_upds': pricing_upds,
            'employees': employees,
        }
        return render(request, 'companyinfo/index.html/', content)


class ContactView(View):
    """处理用户的留言信息"""

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        msg = request.POST.get('message', '')

        try:
            if name and email and subject and msg:
                Contact(name=name, email=email, subject=subject, msg=msg).save()
                return JsonResponse({"status": "success"})
            return JsonResponse({"status": "failed"})
        except BaseException as e:
            return JsonResponse({"status": "failed"})
