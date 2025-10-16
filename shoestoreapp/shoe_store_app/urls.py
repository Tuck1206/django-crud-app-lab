from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.about, name ='about'),
    path('shoes/', views.shoe_index, name='shoe_index'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoe_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe_delete'),
    path('accessory/create/', views.AccessoryCreate.as_view(), name='accessory_create'),
    path('accessory/<int:pk>/', views.AccessoryDetail.as_view(), name='accessory_detail'),
    path('accessory/', views.AccessoryList.as_view(), name='accessory_index'),
    path('accessory/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessory_update'),
    path('accessory/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessory_delete'),
    path('shoes/<int:shoe_id>/associate-accessory/<int:accessory_id>/', views.associate_accessory, name='associate-accessory'),
    path('shoes/<int:shoe_id>/remove-toy/<int:accessory_id>/', views.remove_accessory, name='remove-accessory'),
    path('accounts/signup/', views.signup, name='signup')
]
