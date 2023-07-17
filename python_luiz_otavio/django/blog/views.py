from django.shortcuts import render
from blog.data import posts
# Create your views here.


def blog(request):
    return render(
        request,
        "blog/index.html",
        {
            # 'texto': 'Estamos no blog',
            'posts': posts
        }
    )


def post(request, id):
    print(id)
    return render(
        request,
        "blog/index.html",
        {
            'posts': posts
        }
    )


def exemplo(request):
    return render(
        request,
        "blog/exemplo.html",
        {
            'texto': 'Estamos no exemplo'
        }
    )
