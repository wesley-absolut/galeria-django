from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Imagem, Categoria

ORDENACOES = {
    'recentes': '-criado_em',
    'antigas': 'criado_em',
    'titulo': 'titulo',
}


class ImagemListView(ListView):
    model = Imagem
    template_name = 'galeria/imagem_list.html'
    context_object_name = 'imagens'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        ordem = self.request.GET.get('ordem')
        queryset = queryset.order_by(ORDENACOES.get(ordem, '-criado_em'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class ImagemDetailView(DetailView):
    model = Imagem
    template_name = 'galeria/imagem_detail.html'
    context_object_name = 'imagem'


class ImagemCreateView(CreateView):
    model = Imagem
    fields = ['titulo', 'arquivo', 'categoria']
    template_name = 'galeria/imagem_form.html'
    success_url = reverse_lazy('imagem_list')


class ImagemUpdateView(UpdateView):
    model = Imagem
    fields = ['titulo', 'arquivo', 'categoria']
    template_name = 'galeria/imagem_form.html'
    success_url = reverse_lazy('imagem_list')


class ImagemDeleteView(DeleteView):
    model = Imagem
    template_name = 'galeria/imagem_confirm_delete.html'
    success_url = reverse_lazy('imagem_list')
