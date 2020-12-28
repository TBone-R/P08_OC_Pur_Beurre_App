from django.urls import path

from user.views import (
    RegisterCreateView,
    SavedListView,
    SaveCreateView,
    AccountUpdateView,
    LegalView,
)

app_name = "account"
urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name="register"),
    path('save/', SaveCreateView.as_view(), name="save"),
    path('myproduct/', SavedListView.as_view(), name="myproduct"),
    path('myaccount/', AccountUpdateView.as_view(), name="myaccount"),
    path('legal/', LegalView.as_view(), name="legal"),
]
