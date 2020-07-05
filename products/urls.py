from django.contrib import admin
from django.urls import path
from products import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home, name='home'),
    path('create', views.create,name='create'),
    path('<int:product_id>', views.detail, name= 'detail'),
    path('<int:product_id>/upvote', views.upvote, name= 'upvote'),
]