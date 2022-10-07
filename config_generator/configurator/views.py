from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from config_generator.configurator.models import WhiteLabel, WhiteLabelConfig
from config_generator.configurator.forms import WhiteLabelForm, WhiteLabelConfigForm
from django.http import Http404


def sign_up_view(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect("/")

    signup_error = u""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if password != password_repeat:
            signup_error = u'Введенные пароли не совпадают.'
        else:
            try:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                return HttpResponseRedirect("/")
            except:
                signup_error = u'Пользователь с таким именем уже существует'

    return render(request, "configurator/signup.html", {"signup_error": signup_error, })


def sign_in_view(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect("/")

    auth_error = u""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            auth_error = u"Неправильный логин или пароль."
        else:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                auth_error = u"Пользователь %s заблокирован" % username
    return render(request, "configurator/signin.html", {"auth_error": auth_error,})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/signin/")


def site_view(request):

    if not request.user.is_authenticated:
            return HttpResponseRedirect("/signin/")

    user = request.user

    context = {
        'apps': WhiteLabel.objects.filter(user=user),
    }
    return render(request, "configurator/frontpage.html", context)


def create_app(request):

    form = WhiteLabelForm(request.POST, request.FILES, instance=WhiteLabel(user=request.user))
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {
        'form': form,
        'success': form.is_valid(),
    }

    return render(request, 'configurator/create_app.html', context)


def create_config(request):

    form = WhiteLabelConfigForm(request.POST, request.FILES)
    if form.is_valid():
        config = form.save()
        if 'app' in request.POST:
            app = WhiteLabel.objects.filter(id=request.POST.get('app')).first()
            if app:
                app.config = config
                app.save()

    context = {
        'form': form,
    }
    return HttpResponseRedirect("/")


def get_config(request):

    if 'project' in request.GET:
        try:
            return WhiteLabel.objects.get(title=request.GET.get('project')).get_config()
        except WhiteLabel.DoesNotExist:
            raise Http404("WhiteLabel does not exist")
    else:
        raise Http404


def get_resources(request):

    if 'project' in request.GET:
        try:
            return WhiteLabel.objects.get(title=request.GET.get('project')).get_resources()
        except WhiteLabel.DoesNotExist:
            raise Http404("WhiteLabel does not exist")
    else:
        raise Http404
