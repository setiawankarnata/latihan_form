from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('validate', views.validate_index, name="validate"),
    path('cek/<int:ctr>', views.cek_param, name="cek_param"),
]
