from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('home', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('shoes/', views.shoe_index, name='shoe_index'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoe_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe_delete'),
    path('accessories/create/', views.AccessoriesCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/', views.AccessoriesDetail.as_view(), name='accessories-detail'),
    path('accessories/', views.AccessoriesList.as_view(), name='accessories-index')


]
