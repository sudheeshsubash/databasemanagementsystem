
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenBlacklistView



schema_view = get_schema_view(
    openapi.Info(
        title="DATABASE MANAGEMENT CRUD SYSTEM",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path("api/databasemanagement/",include("api.urls")),
    path('',include('users.urls')),
    
]
