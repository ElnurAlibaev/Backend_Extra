from django.urls import path, include
from blogs import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'get3', views.BlogViewSet)


urlpatterns = [
    path('', views.get_blogs),
    path('<int:id>/', views.get_blog),

    path('get/', views.BlogView.as_view()),

    path('get1/', views.BlogView2.as_view({'get':'list'})),
    path('get1/<int:pk>/', views.BlogView2.as_view({'get':'retrieve'})),

    path('get2/', views.BlogListCreateAPIView.as_view()),

    path('', include(router.urls))
]
