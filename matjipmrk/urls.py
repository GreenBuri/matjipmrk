from django.urls import path
from . import views

app_name = 'matjipmrk'

urlpatterns = [
    path('',views.home, name='home'), #config/urls -> matjipmrk/urls -> matjipmrk/views.py 실행!
    # path('restaruantCreate/create', views.Create_category, name=)
    path('rst/detail/<int:rst_id>/', views.rst_detail, name='rst_detail'), # path_conver를 통해 url 쪼개줌.
    path('rst/create/', views.rst_create, name='rst_create'),
    path('rst/detail/<int:rst_id>/delete/', views.rst_delete, name='rst_delete'),
    path('rst/detail/<int:rst_id>/comment/', views.cmnt_create, name='cmnt_create'),
    path('rst/detail/<int:rst_id>/comment/<int:cmnt_id>/delete/', views.cmnt_delete, name='cmnt_delete'),
    path('rst/search/', views.rst_search, name='rst_search'),
    ]

