from django.shortcuts import render
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'main_page.html')


def shop_page(request):
    fot = 'Футболки'
    dj = 'Джинсы'
    cros = 'Кроссовки'
    cof = 'Кофты'
    context = {
        'fot': fot,
        'dj': dj,
        'cros': cros,
        'cof': cof
    }
    return render(request, 'shop_page.html', context)

def bin_page(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    return render(request, 'bin_page.html', context)
