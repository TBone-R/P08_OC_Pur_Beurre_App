from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import SavedSubstitute
from user.form import CustomUserCreationForm, CustomUserChangeForm
from product.models import Product
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)


class RegisterCreateView(CreateView):
    template_name = "register/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account:myaccount")


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "register/register.html"
    login_url = '/login/'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("product:home")

    def get_object(self, queryset=None):
        return self.request.user


class SavedListView(LoginRequiredMixin, ListView):
    template_name = "myproduct.html"

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        user = self.request.user
        queryset = SavedSubstitute.objects.filter(user=user)
        return queryset


class SaveCreateView(LoginRequiredMixin, CreateView):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id_substitute", None)
        origin_id = request.POST.get("origin_id", None)
        user = request.user

        substitute = SavedSubstitute(
            user=user,
            substitute=Product.objects.get(id=id),
            original_product=Product.objects.get(id=origin_id),
        )

        substitute.save()

        return redirect(reverse("account:myproduct"))


class LegalView(View):
    template_name = "legal.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
