from django.urls import path
from . import views
urlpatterns = [
    path('',views.api_response,name="api_response"),
]
