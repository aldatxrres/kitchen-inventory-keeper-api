from django.contrib import admin
from django.urls import path, include
from api.swagger import swagger_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path(
        "swagger/",
        swagger_schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        swagger_schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]