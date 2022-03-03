
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from firm.views import *
urlpatterns = [
    path('', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', CreateUserView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('company/', include('firm.urls')),
    # path('api/auth/', include('rest_framework.urls')),
    # path('api/rest-auth/', include('rest_auth.urls')),
    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.contrib import admin
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
