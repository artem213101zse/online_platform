import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from first.forms import GeoForm, LoginForm, UserRegistrationForm
from first.models import GeoHistory


def get_menu_context():
    return [
        {'url': '/', 'name': 'Главная'},
        {'url': '/astr/', 'name': 'Астрономия'},
        {'url': '/bal/', 'name': 'Бал'},
        {'url': '/inf/', 'name': 'Информатика'},
    ]


def index_page(request):
    context = {
        'menu': get_menu_context(),
        'pagename': 'Главная'
    }
    return render(request, 'pages/index.html', context)


def astr_page(request):
    main_user = request.user
    context = {
        'menu': get_menu_context(),
        'pagename': 'Астрономия'
    }
    geo_flag = True

    filt_obj = GeoHistory.objects.filter(author=main_user)

    if (filt_obj):
        last_date = GeoHistory.objects.latest("date").date.date()
        last_time = GeoHistory.objects.latest("date").date.time()
        now_date = datetime.datetime.now().date()
        now_time = datetime.datetime.now().time()
        delta_d = now_date - last_date
        if delta_d.days == 0:
            if now_time.hour - last_time.hour == 0:
                if now_time.minute - last_time.minute <= 15:
                    geo_flag = False

    context['geo_flag'] = geo_flag
    if geo_flag:
        if request.method == 'POST':
            f = GeoForm(request.POST)
            if f.is_valid():
                f = GeoForm(request.POST)
                lat = f.data['lat']
                lon = f.data['lon']
                acc = f.data['acc']
                alt = f.data['alt']
                dir = f.data['dir']
                spd = f.data['spd']

                item = GeoHistory(date=datetime.datetime.now() + datetime.timedelta(hours=3, minutes=0), latitude=lat, longitude=lon, accuracy=acc, altitude=alt, direction=dir, speed=spd, author=main_user)
                item.save()
                context['form'] = f
            else:
                context['form'] = f
                print("Form is not valid!")
        else:
            context['form'] = GeoForm()

    return render(request, 'pages/astr.html', context)


def page_not_found_view_404(request, exception):
    return render(request, 'errors/404.html', status=404)


#def page_not_found_view_500(request, exception):
    #return render(request, exception, 'errors/500.html', status=500)


def user_login(request):
    context = {
        'menu': get_menu_context(),
        'pagename': 'Войти в систему'
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Авторизация успешна")
                return redirect(index_page)
            else:
                messages.success(request, "Аккаунт отключен. Обратитесь к администрции")
        else:
            messages.success(request, "Неверный логин или пароль")
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'registration/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect(index_page)

def register(request):
    if request.method=="POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, "Вы успешно зарегистрировались. Теперь Вы можете войти в систему")
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
