from typing import Any

from blog.data import posts
from django.http import Http404, HttpRequest
from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(
        request,
        "blog/index.html",
        {
            # 'texto': 'Estamos no blog',
            "posts": posts
        },
    )


def post(request: HttpRequest, post_id: int):

    found_post: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404("Post não existe")

    context = {
        "posts": [found_post],
        "title": found_post["title"] + " - ",
    }
    print(post_id)
    return render(request, "blog/index.html", context)


def exemplo(request):
    return render(request, "blog/exemplo.html",
                  {"texto": "Estamos no exemplo"})
