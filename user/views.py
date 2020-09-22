from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from user.form import UserForm
from user.models import SavedSubstitute
from product.models import Product
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)



class RegisterCreateView(CreateView):
    template_name = "register/register.html"
    form_class = UserCreationForm
    success_url = reverse("account:myaccount")


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "myaccount.html"
    form_class = UserForm

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user


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
