from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)



class RegisterCreateView(CreateView):
    # view for register

    pass


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    # view for myaccount

    pass


class SavedListView(LoginRequiredMixin, ListView):
    # view for myproduct

    pass


class SaveCreateView(LoginRequiredMixin, CreateView):
    # view for save

    pass
