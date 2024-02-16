from django.urls import path, include
from blog import views

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('comment', views.CommentsviewSet, basename='comment')







urlpatterns = [
    
    # auth
    path('register/', views.RegisterUser.as_view()),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
    
    # blog
    path('blog/', views.BlogCreateList.as_view() ),
    path('blog/<uuid:pk>', views.BlogDestroyUpdateRetrive.as_view() ),
    
    # comments
    path('', include(router.urls)),
   
    
]
