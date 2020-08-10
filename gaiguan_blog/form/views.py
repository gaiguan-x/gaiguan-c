from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo, Field, City


def register(request, keyword):
    """
    这个是动态修改表单的方法，渲染表单html
    :param request:
    :return:
    """
    context = {}
    form = None
    form_fields = Field.objects.all()
    for form_field in form_fields:
        if form_field.id == int(keyword):
            form = form_field
            break
    # 取所有的字段信息
    context['title'] = form.title
    context['name'] = form.name
    context['age'] = form.age
    context['sex'] = form.sex
    context['school'] = form.school
    context['address'] = form.address
    context['hobby'] = form.hobby
    context['strong_point'] = form.strong_point
    context['city'] = form.city
    context['phone'] = form.phone
    context['date'] = form.date
    context['postal_code'] = form.postal_code
    context['mail'] = form.mail
    context['text'] = form.text
    # 获取省份的信息
    provinces = City.objects.values('province').distinct().all()
    context['provinces'] = provinces
    citys = City.objects.values('city').distinct().all()
    context['citys'] = citys
    districts = City.objects.values('district').distinct().all()
    context['districts'] = districts

    return render(request, 'form/register.html', context=context)


@method_decorator(csrf_exempt, name='dispatch')
def add_info(request):
    """
    根据动态的表单添加信息
    :param request:
    :return:
    """
    user_info = UserInfo()
    if request.method == 'POST':
        inform = request.POST
        print(inform)
        user_info.name = inform.get('name', None)
        user_info.age = inform.get('age', None)
        user_info.sex = inform.get('sex', None)
        user_info.school = inform.get('school', None)
        user_info.address = inform.get('address', None)
        user_info.hobby = inform.get('hobby', None)
        user_info.strong_point = inform.get('strong_point', None)
        user_info.date = inform.get('date', None)
        # 城市
        quiz1 = inform.get('quiz1', '')
        quiz2 = inform.get('quiz2', '')
        quiz3 = inform.get('quiz3', '')

        user_info.city = quiz1 + '-' + quiz2 + '-' + quiz3
        user_info.phone = inform.get('phone', None)
        user_info.postal_code = inform.get('postal_code', None)
        user_info.mail = inform.get('mail', None)
        user_info.text = inform.get('text', None)
        user_info.save()
    return render(request, 'form/test.html')


# 以json数据形式返回所有的表单
def get_all_forms(request):
    result = {
        'forms': []
    }

    fields = Field.objects.all()
    for field in fields:
        form = {}
        form["id"] = str(field.id)
        form["title"] = field.title
        form['name'] = field.name
        form['age'] = field.age
        form['sex'] = field.sex
        form['school'] = field.school
        form['address'] = field.address
        form['hobby'] = field.hobby
        form['strong_point'] = field.strong_point
        form['date'] = field.date
        form['city'] = field.city
        form['phone'] = field.phone
        form['postal_code'] = field.postal_code
        form['mail'] = field.mail
        form['text'] = field.text
        result["forms"].append(form)

    return JsonResponse(result)


def display_all_forms(request):
    return render(request, 'form/all_forms.html')


def search_form(request):
    result = {
        'forms': [],
        'info': '没有此表单',
    }
    form_title = request.GET.get('title', '')
    if form_title:
        forms = Field.objects.filter(title__icontains=form_title)
        for form in forms:
            # 创建一个form字典对象
            form_dic = {}
            form_dic["id"] = str(form.id)
            form_dic["title"] = form.title
            form_dic['name'] = form.name
            form_dic['age'] = form.age
            form_dic['sex'] = form.sex
            form_dic['school'] = form.school
            form_dic['address'] = form.address
            form_dic['hobby'] = form.hobby
            form_dic['strong_point'] = form.strong_point
            form_dic['date'] = form.date
            form_dic['city'] = form.city
            form_dic['phone'] = form.phone
            form_dic['postal_code'] = form.postal_code
            form_dic['mail'] = form.mail
            form_dic['text'] = form.text
            result['forms'].append(form_dic)
        result['info'] = '查询成功！'
    return JsonResponse(result)


# # 根据省，获取某省的所有市
# def get_cities(request):
#     result = {
#         "cities": []
#     }
#     province = request.GET.get('province')
#     print(province)
#     # 根据省份查询对应的所有城市的记录
#     if province:
#         all_city_info = City.objects.filter(province=province)
#         for city in all_city_info:
#             city_name = city.city
#             result["cities"].append(city_name)
#
#     return JsonResponse(result)
#
#
# # 根据市，获取某市的所有区
# def get_districts(request):
#     result = {
#         "districts": []
#     }
#     city = request.GET.get('city')
#     # 根据省份查询对应的所有城市的记录
#     if city:
#         all_city_info = City.objects.filter(city=city)
#         for city in all_city_info:
#             city_name = city.city
#             result["districts"].append(city_name)
#
#     return JsonResponse(result)
