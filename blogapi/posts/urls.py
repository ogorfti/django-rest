from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

# 2nd method
# router = SimpleRouter()
# router.register('', views.PostViewSet, basename='posts')
# router.register('users', views.UserViewSet, basename='users')

# urlpatterns = router.urls



# midleware, get_user_model