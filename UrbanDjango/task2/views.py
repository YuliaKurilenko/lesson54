from django.shortcuts import render

# Create your views here.

def class_(request):
    return render(request, 'class_template.html')


def func(request):
    return render(request, 'func_template.html')


