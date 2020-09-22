from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
)

from product.forms import SearchBarForm
from product.models import Product
from product.queryset import get_substitute


class HomeView(View):
    # view for home
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        form = SearchBarForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
    # view for product
    template_name = "detail.html"

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)


class ResultListView(ListView):
    # view for result
    template_name = "result.html"

    def get_queryset(self):
        form = SearchBarForm(self.request.GET)
        user_input = form.data["name"]
        return Product.objects.filter(name__icontains=user_input)


class SubstituteListView(ListView):
    # view for substitutes
    template_name = "substitute.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origin_id'] = self.kwargs.get("id")
        return context

    def get_queryset(self):
        user = self.request.user
        id_ = self.kwargs.get("id")

        queryset = get_substitute(id_, user)

        return queryset
