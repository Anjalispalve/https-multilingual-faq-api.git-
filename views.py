from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer



def list(self, request, *args, **kwargs):
    cache_key = f"faqs_{request.query_params.get('lang', 'en')}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return response(cached_data)

    response = super().list(request, *args, **kwargs)
    cache.set(cache_key, response.data, timeout=60 * 60)  # Cache for 1 hour
    return response

