# 记得引入include
from django.conf.urls.static import static
import notifications.urls
from article.views import article_list

from companyinfo.views import Index, ContactView

from django.conf import settings
from django.views.static import serve  # 处理静态文件
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url,include
# 存放了映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),
    # home
    path('', article_list, name='home'),
    # 重置密码app
    path('password-reset/', include('password_reset.urls')),
    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
    # djang-notifications
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # notice
    path('notice/', include('notice.urls', namespace='notice')),
    # django-allauth
    path('accounts/', include('allauth.urls')),

    path('form/', include('form.urls')),

    path('jet/', include('jet.urls', 'jet')),  # django-jet 路由
    path('com', Index.as_view(), name='/companyinfo/index'),   # 首页
    path('contactus/', ContactView.as_view(), name='contactus'),  # 接收用户留言
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    #  配置静态文件访问处理
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}))

