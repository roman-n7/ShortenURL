from django.urls import path
from .views import URLShortenView, URLRedirectView

urlpatterns = [
    path('shorten/', URLShortenView.as_view(), name='url-shorten'),
    path('redirect/<str:short_url>/', URLRedirectView.as_view(), name='url-redirect'),
]