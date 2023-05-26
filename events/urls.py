from django.urls import path

from events.views import EventCreateView, EventRetrieveView, EventListView

# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('<int:pk>/', EventRetrieveView.as_view()),
    path('list/', EventListView.as_view()),
]
