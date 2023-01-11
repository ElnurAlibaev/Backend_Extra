from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.ProductView.as_view({'get':'list'})),
    path('products/<int:pk>/', views.ProductView.as_view({'get':'retrieve'})),

    path('categories/', views.CategoryView.as_view({'get':'list'})),
    path('categories/<int:pk>/', views.CategoryView.as_view({'get':'retrieve'})),
    path('categories/<int:pk>/products/', views.CategoryProduct.as_view({'get':'retrieve'})),

]
