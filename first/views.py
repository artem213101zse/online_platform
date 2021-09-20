import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from first.forms import GeoForm
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

                a = f.data['latitude']
                b = f.data['longitude']
                c = f.data['altitude']

                item = GeoHistory(date=datetime.datetime.now() + datetime.timedelta(hours=3, minutes=0), latitude=a, longitude=b, altitude=c, author=main_user)
                item.save()
                context['form'] = f
            else:
                context['form'] = f
        else:
            context['form'] = GeoForm()

    return render(request, 'pages/astr.html', context)


def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)