"""django_pig_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app.login.views import LoginCheck
from app.station.views import Station, SystemCheck
from app.pig_base.views import PigBaseCheck
from app.fit.views import GetPoint,GetCoefficient
from app.food_quantity.views import SetIntake
from app.fit.views import LineFit

urlpatterns = [
    path('login/', LoginCheck.as_view()),
    path('system/', SystemCheck.as_view()),
    path('station/', Station.as_view()),
    path('pigbase/', PigBaseCheck.as_view()),
    path('setintake/', SetIntake.as_view()),
    path('linefit/',LineFit.as_view()),
    path('getpoint/', GetPoint),
    path('getcoefficient/', GetCoefficient)
]
