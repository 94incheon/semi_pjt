from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # CRUD
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),

    # 로그인/로그아웃
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
