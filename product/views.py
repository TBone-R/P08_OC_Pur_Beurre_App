from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
)


class HomeView(View):
    # view for home

    pass


class ProductDetailView(DetailView):
    # view for product

    pass


class ResultListView(ListView):
    # view for result

    pass


class SubstituteListView(ListView):
    # view for substitutes

    pass

