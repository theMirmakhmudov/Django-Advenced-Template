from django.shortcuts import render
from calendar import HTMLCalendar
from apps.models import Product


def index(request):
    data = {}
    data['dataset'] = Product.objects.all()
    return render(request, 'index.html', data)


def show_image(request):
    date = {}
    date["data_images"] = Product.objects.all()
    return render(request, "images.html", date)


def test_html(request):
    return render(request, "test.html")


def calendar_page(request):
    month_1 = HTMLCalendar().formatmonth(theyear=2024, themonth=1)
    month_2 = HTMLCalendar().formatmonth(theyear=2024, themonth=2)
    month_3 = HTMLCalendar().formatmonth(theyear=2024, themonth=3)
    month_4 = HTMLCalendar().formatmonth(theyear=2024, themonth=4)
    month_5 = HTMLCalendar().formatmonth(theyear=2024, themonth=5)
    month_6 = HTMLCalendar().formatmonth(theyear=2024, themonth=6)
    month_7 = HTMLCalendar().formatmonth(theyear=2024, themonth=7)
    month_8 = HTMLCalendar().formatmonth(theyear=2024, themonth=8)
    month_9 = HTMLCalendar().formatmonth(theyear=2024, themonth=9)
    month_10 = HTMLCalendar().formatmonth(theyear=2024, themonth=10)
    month_11 = HTMLCalendar().formatmonth(theyear=2024, themonth=10)
    month_12 = HTMLCalendar().formatmonth(theyear=2024, themonth=10)

    calendar = {
        month_1,
        month_2,
        month_3,
        month_4,
        month_5,
        month_6,
        month_7,
        month_8,
        month_9,
        month_10,
        month_11,
        month_12
    }
    return render(request, "calendar.html", context={"calendar": calendar})
