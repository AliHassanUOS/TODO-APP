from django.urls.conf import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),
    path("del/<int:id>",views.delete, name="del")
   
]
