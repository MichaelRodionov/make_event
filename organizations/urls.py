from django.urls import path

from organizations.views import OrgCreateView

# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('create/', OrgCreateView.as_view()),
]
