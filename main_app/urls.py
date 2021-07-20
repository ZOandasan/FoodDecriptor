from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('foods/', views.foods_index, name="foods_index"),
    path('foods/<int:food_id>/', views.foods_detail, name='detail'),
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    path('foods/<int:food_id>/add_review/', views.add_review, name='add_review'),
    path('foods/<int:food_id>/assoc_side/<int:side_id>/', views.assoc_side, name='assoc_side'),
    path('foods/<int:food_id>/unassoc_side/<int:side_id>/', views.unassoc_side, name='unassoc_side'),
]