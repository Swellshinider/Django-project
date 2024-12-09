from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = reverse_lazy('login')
    raise_exception = False  # Não lançar exceção 403

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Se estiver autenticado mas não for superuser, volta pro login
        return redirect(self.login_url)


class ProdutoListView(SuperUserRequiredMixin, ListView):
    model = Produto
    template_name = 'product/produto_list.html'
    context_object_name = 'produtos'


class ProdutoDetailView(SuperUserRequiredMixin, DetailView):
    model = Produto
    template_name = 'product/produto_detail.html'
    context_object_name = 'produto'


class ProdutoCreateView(SuperUserRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco']
    template_name = 'product/produto_form.html'
    success_url = reverse_lazy('produto-list')


class ProdutoUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco']
    template_name = 'product/produto_form.html'
    success_url = reverse_lazy('produto-list')


class ProdutoDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Produto
    template_name = 'product/produto_confirm_delete.html'
    success_url = reverse_lazy('produto-list')


class CustomLoginView(LoginView):
    template_name = 'product/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('produto-list')
    
    def get_success_url(self):
        return self.success_url