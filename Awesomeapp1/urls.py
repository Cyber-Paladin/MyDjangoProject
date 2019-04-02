"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('product', views.product),
    path('product/2019', views.poroduct2019),
    path('folder', views.folder),
    path('folder/Product1', views.ReFolder),
    re_path('^folder/Product(?P<numberPage>[\d]+)$', views.folderProductN, name = 'folderProductN'),
    re_path('^product/(?P<year>[\d]{4})$', views.productFour, name = 'productFour'),
    re_path('^product/(?P<year>[\d]{4})/(?P<month>[0-9]{1,2})$', views.productFourYM, name = 'productFourYM'),
    re_path('^product/(?P<year>[\d]{4})/(?P<month>[0-9]{1,2})/(?P<day>[\d]{1,2})$', views.productFourYMD, name = 'productFourYMD'),
    re_path('^product/(?P<word>[\w]+)$', views.productText, name = 'productText'),
    # path('product/2020/20', views.poroduct2020),

]