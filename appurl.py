from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_list, name='mood_list'),
    path('<int:mood_id>/', views.mood_detail, name='mood_detail'),
    path('predict/', views.predict_mood, name='predict_mood'),
]
