from django.urls import path
from .views import PostsList, NewsDetail

urlpatterns = [

   path('', PostsList.as_view()),
   path('<int:id>', NewsDetail.as_view()),
]
