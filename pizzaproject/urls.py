"""pizzaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from pizzashop import views, apis
from django.contrib.auth import views as auth_views


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),

    re_path(r'^pizzashop/sign-in', auth_views.LoginView.as_view(template_name='pizzashop/sign_in.html'),
            name='sign-in'),
    re_path(r'^pizzashop/sign-out', auth_views.LogoutView.as_view(next_page='/'),
                name='sign-out'),
    re_path(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),
    re_path(r'^pizzashop/sign-up', views.pizzashop_sign_up, name='pizzashop_sign_up'),
    re_path(r'^pizzashop/account/$', views.pizzashop_account, name='pizzashop-account'),
    re_path(r'^pizzashop/pizza/$', views.pizzashop_pizza, name='pizzashop-pizza'),
    re_path(r'^pizzashop/pizza/add/$', views.pizzashop_add_pizza, name='pizzashop-add-pizza'),
    re_path(r'^pizzashop/pizza/edit/(?P<pizza_id>\d+)/$', views.pizzashop_edit_pizza, name='pizzashop-edit-pizza'),
    #API
    re_path(r'api/client/pizzashops/$', apis.client_get_pizzashops ),
    re_path(r'^api/client/pizzas/(?P<pizzashop_id>\d+)/$', apis.client_get_pizzas)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
