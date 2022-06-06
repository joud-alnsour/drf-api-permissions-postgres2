from django.urls import path
from ducks.api.viewsets import (
    DuckListView,
    DuckDetailView,
)

urlpatterns = [
    path('ducks-list', DuckListView.as_view(), name='duck_list'),
    path('duck-detail/<int:pk>', DuckDetailView.as_view(), name='duck_detail'),
]