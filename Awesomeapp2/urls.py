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
from django.urls import path, re_path, include

from . import views

redirectpatterns = [
    path('redirect', views.redirect),
]

newpatterns = [
    path('comments', views.comments),
    re_path('^comments/(?P<number>[\d]+)', views.comments_number, name = 'number'),
]

actionpatterns = [
    re_path('^page-(?P<page>[1-9]|[1-9][0-9]+)/(?P<action>edit|delete|answer)/$',
            views.reviewAction, name='reviewAction'),
]

urlpatterns = [
    # first part
    path('review', views.review),
    re_path('^review/page-(?P<Page>[1-9])$', views.reviewPage, name='reviewPage'),
    re_path(r'review/(?:page-(?P<Page>[1-9][0-9]+)/)$', views.reviewPage, name = 'reviewPage'),
    path('newpatterns/', include(newpatterns)),
    path('product/review/', include(actionpatterns)),
    path('', views.application3),
    # another part
    path('redirect', views.redirect),
    path('redirected', views.redirected),
    path('render-html', views.renderHtml),
    path('render-template', views.htmlFormTemplate),
    path('render-template/form-handler', views.formHandler),

]
