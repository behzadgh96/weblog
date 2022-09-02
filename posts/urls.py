from django.urls import path
from .views import post_list_view,post_detail_view

urlpatterns = [
    path('',post_list_view.as_view()),
    path('<int:pk>/',post_detail_view.as_view()),
]