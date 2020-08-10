#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import CompanyInfo, Supers, Aboutus, Services, Customers, Pricing, Employees, Contact


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'info1', 'info2', 'phone', 'address', 'web']
    list_filter = ['name']
    search_fields = ['name']


class PricingAdmin(admin.ModelAdmin):
    list_display = ['info', 'item']
    list_filter = ['info', 'item']
    search_fields = ['info', 'item']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Supers)
admin.site.register(Aboutus)
admin.site.register(Services)
admin.site.register(Customers)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Employees)
admin.site.register(Contact)
