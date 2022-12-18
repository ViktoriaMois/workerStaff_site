from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordContextMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView
from django.utils.translation import gettext_lazy as _

from .forms import AskForm

import workerStuff.models as mod


def test_link(request):
    return render(request, 'test.html')


@csrf_exempt
def signUp_link(request):
    if request.method == "GET":
        return render(request, 'signUp.html')
    elif request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["pass"]
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        request.method = "GET"
        return redirect('signIn')


@csrf_exempt
def signIn_link(request):
    if request.method == "GET":
        return render(request, "signIn.html", {"sucess": 1})
    if request.method == "POST":
        username = request.POST["your_name"]
        password = request.POST["your_pass"]
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "signUp.html", {"sucess": 0})
        else:
            login(request, user)
            return redirect('/')


def contact(request):
    return render(request, 'contact.html')


def index(request, string="all"):
    workers_list = mod.Workers.objects.all()
    print(string)
    name = "Сотрудники"
    if string == "index":
        name = string
    elif string == "Бухгалтер":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    elif string == "Директор":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    elif string == "Инженер":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    elif string == "Системный администратор":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    elif string == "Менеджер":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    elif string == "Разработчик":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    elif string == "Секретарь":
        workers_list = mod.Workers.objects.filter(position=string)
        name = string
    return render(request, 'index.html', {"nameHead": name,  "w_l": workers_list})


def askQuestion(request):
    form = AskForm()
    return render(request, 'askForm.html', {"form": form})


@login_required
def makeRequest(request):
    if request.method == 'POST':
        form = AskForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = User.objects.get(username=request.user.username)
            obj.email = User.objects.get(email=request.user.email)
            obj.worker = mod.Workers.objects.get(fio=form.cleaned_data["fio"])
            form.save()
            return redirect('/')
    return render(request, "askForm.html", {'form': form})


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'passwordChange.html'
    title = _('Password change')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = 'passwordChange.html'
    title = _('Password change successful')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def logoutUser(request):
    logout(request)
    return redirect('/')


# def index(request):
#     workers_list = mod.Workers.objects.all()
#     duty_list = mod.Duties.objects.all()
#     return render(request, 'index.html', {"w_l": workers_list, "d_l": duty_list})


def checkusername(request):
    result = {'code': 1, "content": ""}
    username = request.GET.get("username")
    user = User.objects.filter(username=username).first()
    if user:
        result = {'code': -1, "content": "Имя пользователя занято"}
    else:
        result = {'code': 1, "content": "Имя пользователя свободно"}
    return JsonResponse(result)


def checkmail(request):
    result = {'code': 1, "content": ""}
    email = request.GET.get("email")
    print(email)
    user = User.objects.filter(email__exact=email).first()
    if user:
        result = {'code': -1, "content": "Пользователь с такой почтой существует"}
    else:
        result = {'code': 1, "content": "Почтовый адрес свободен"}
    return JsonResponse(result)
