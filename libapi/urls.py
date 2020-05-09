from django.contrib import admin
from django.urls import path
from libapi.views import PublicationView, PublicationRetrieveUpdateDestroyView, LoginView

# /api/lib/

urlpatterns = [
    path('publication-houses/', PublicationView.as_view()),
    path('publication-houses/<int:pk>', PublicationRetrieveUpdateDestroyView.as_view()),
    path('login/', LoginView.as_view())
]
