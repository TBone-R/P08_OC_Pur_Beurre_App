from django.urls import path

from product.views import (
    HomeView,
    ProductDetailView,
    ResultListView,
    SubstituteListView,
)

app_name = "product"
urlpatterns = [
    path('', HomeView.as_view(),
         name="home"),

    path('<int:id>/', ProductDetailView.as_view(),
         name="product"),

    path('result/', ResultListView.as_view(),
         name="result"),

    path('<int:id>/substitute', SubstituteListView.as_view(),
         name="substitutes"),
]
