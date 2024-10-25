from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Masyli, SupernaturalAbilities
from django.db.models import F
from django.views.generic import ListView, View, UpdateView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import MasyliForm, RegisterForm, SupernaturalForm
from django.core.cache import cache


def main_page(request):
    return render(request, 'home/index.html')


def about_page(request):
    return render(request, 'home/information_about_us.html')


def levels_confirm(request):
    return render(request, 'home/levels_confirm.html')


class AddMasyliView(View):
    def get(self, request):
        form = MasyliForm()
        return render(request, 'home/add_masyli.html', {'form': form})

    def post(self, request):
        form = MasyliForm(request.POST, request.FILES)
        if form.is_valid():
            masyli = form.save()
            return redirect('add-masyly-details', masyli_id=masyli.id)
        else:
            print(form.errors)
        return render(request, 'home/add_masyli.html', {'form': form})


class AddMasylyDetailsView(View):
    def get(self, request, masyli_id):
        try:
            masyli_instance = Masyli.objects.get(id=masyli_id)
        except Masyli.DoesNotExist:
            return redirect('error_page')

        form = SupernaturalForm()
        return render(request, 'home/add_more_details.html', {'form': form, 'masyli': masyli_instance})

    def post(self, request, masyli_id):
        try:
            masyli_instance = Masyli.objects.get(id=masyli_id)
        except Masyli.DoesNotExist:
            return redirect('error_page')

        form = SupernaturalForm(request.POST, request.FILES)
        if form.is_valid():
            supernatural_instance = form.save(commit=False)
            supernatural_instance.masyli = masyli_instance
            return redirect('success')
        else:
            print(form.errors)

        return render(request, 'home/add_more_details.html', {'form': form, 'masyli': masyli_instance})


class MasylyDetailsView(ListView):
    model = Masyli
    template_name = 'home/masyli_list.html'
    context_object_name = 'masyli'

    def get_queryset(self):
        queryset = cache.get('masyli_list')
        if queryset is None:
            queryset = super().get_queryset().values()
            cache.set('masyli_list', list(queryset), 3600)
        return queryset


class MasyliUpdateView(UpdateView):
    model = Masyli
    form_class = MasyliForm
    template_name = 'home/update_post.html'
    success_url = '/success'


class SupernaturalListView(ListView):
    model = SupernaturalAbilities
    template_name = 'home/supernatural_list.html'
    context_object_name = 'supernatural_list'


def success_view(request):
    return render(request, 'home/success.html')


@login_required
def profile_view(request):
    return render(request, 'web/profile.html')


def login_view(request):
    return render(request, 'registration/login.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
