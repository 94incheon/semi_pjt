from django.urls import path
from . import views

# /community
urlpatterns = [
    path('', views.index), 
    path('new_review/', views.new_review), # create [생성]
    path('create_review/', views.create_review), # 사용자 제출 리뷰 데이터 저장
    path('review_detail/<int:review_pk>/', views.review_detail), # read [조회]
    path('review_delete/<int:review_pk>/', views.review_delete), # delete [삭제]
    path('review_update/<int:review_pk>/', views.review_update), # update [삭제]
]