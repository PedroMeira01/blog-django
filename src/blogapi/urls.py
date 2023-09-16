# blogapi/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importe as views de autenticação do Django
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Rotas JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Rota de administração do Django
    path('admin/', admin.site.urls),

    # Rota principal para suas APIs (substitua 'blog' pelo nome do seu aplicativo)
    path('api/', include('blog.urls')),

]
