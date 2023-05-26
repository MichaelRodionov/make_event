from django.urls import path

from core.views import UserRegView, UserAuthView

# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('create/', UserRegView.as_view()),
    path('auth/', UserAuthView.as_view()),
]
