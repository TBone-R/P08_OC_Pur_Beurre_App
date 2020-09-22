from django.urls import include, path

urlpatterns = [
    path('', include(('product.urls', "product"),
                     namespace='product')),
    path('', include(("user.url", "account"),
                     namespace='account')),
    path('', include('django.contrib.auth.urls')),
]
