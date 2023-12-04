from django.urls import path, include

urlpatterns = [
    path('', include('back.routers'), name='api_router'),
]