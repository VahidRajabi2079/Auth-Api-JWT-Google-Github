from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="🔐 Authentication API",
      default_version='complete',
      description="مستندات API برای احراز هویت با استفاده از Django، Djoser، JWT و Social Login",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="you@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path("admin/", admin.site.urls),
   path("auth/", include("djoser.urls")),
   path("auth/", include("djoser.urls.jwt")),
   path("auth/", include("djoser.social.urls")),
   path("auth/o/", include("social_django.urls", namespace="social")),
   
   
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
