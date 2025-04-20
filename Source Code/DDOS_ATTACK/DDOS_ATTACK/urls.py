"""DDOS_ATTACK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from data_admins import views as admins
from django.urls import re_path  # Corrected import for re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),  # Admin URL

    re_path(r'^$', admins.index, name="index"),  # Index page
    re_path(r'user/register', admins.register, name="register"),  # Register page
    re_path(r'user/add_data', admins.add_data, name="add_data"),  # Add data page
    re_path(r'user/userpage', admins.userpage, name="userpage"),  # User page
    re_path(r'user/labeled_data', admins.labeled_data, name="labeled_data"),  # Labeled data page
    re_path(r'user/unlabeled_data', admins.unlabeled_data, name="unlabeled_data"),  # Unlabeled data page
    re_path(r'user/ddos_analysis', admins.ddos_analysis, name="ddos_analysis"),  # DDoS analysis page
    re_path(r'user/chart_page/(?P<chart_type>\w+)', admins.chart_page, name="chart_page"),  # Chart page with regex for chart_type
]
