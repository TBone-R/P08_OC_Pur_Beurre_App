from django.urls import include, path

urlpatterns = [
    path('', include(('product.urls', "product"),
                     namespace='product')),
    path('', include(("user.urls", "account"),
                     namespace='account')),
    path('', include('django.contrib.auth.urls')),
]
