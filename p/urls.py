from django.urls import path
from chat.views import chat_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ... your other URL patterns
     path('', chat_view, name='chat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




