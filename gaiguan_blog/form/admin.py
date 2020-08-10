from django.contrib import admin
from .models import UserInfo, Field, City


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'school', 'address', 'hobby', 'strong_point', 'date', 'city')
    ordering = ('id',)


class FieldAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'name', 'age', 'sex', 'school', 'address', 'hobby', 'strong_point', 'date', 'city', 'is_used')
    list_editable = (
        'is_used',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('province', 'city', 'district')


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(City, CityAdmin)
