from django.urls import path
from .views import (
    ImagemListView, ImagemDetailView,
    ImagemCreateView, ImagemUpdateView, ImagemDeleteView
)

urlpatterns = [
    path('', ImagemListView.as_view(), name='imagem_list'),
    path('imagem/<int:pk>/', ImagemDetailView.as_view(), name='imagem_detail'),
    path('imagem/novo/', ImagemCreateView.as_view(), name='imagem_create'),
    path('imagem/<int:pk>/editar/', ImagemUpdateView.as_view(), name='imagem_update'),
    path('imagem/<int:pk>/deletar/', ImagemDeleteView.as_view(), name='imagem_delete'),
]