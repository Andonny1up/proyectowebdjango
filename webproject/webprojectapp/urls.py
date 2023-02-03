from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('servicio/',views.service, name="service"),
    path('tienda/',views.shop, name="shop"),
    path('blog/',views.blog, name="blog"),
    path('contacto/',views.contact, name="contact"),
]
