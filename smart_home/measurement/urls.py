from django.urls import path
from .views import ViewListCreate, ViewRetrieveUpdate

urlpatterns = [
    path('views/', ViewListCreate.as_view(), name='view-list-create'),
    path('views/<int:pk>/', ViewRetrieveUpdate.as_view(), name='view-retrieve-update'),
]