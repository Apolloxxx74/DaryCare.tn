from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("services/",views.services,name='services'),
    path("espace_infirmier/",views.espace_infirmier,name='espace_infirmier'),
    path("infirmier0/",views.infirmier0,name='infirmier0'),
    path("espace_patient/",views.espace_patient,name='espace_patient'),
    path("patient0/",views.patient0,name='patient0'),
    path("quiz/",views.quiz,name='quiz'),
    path("quiz0/",views.quiz0,name='quiz0'),


]
