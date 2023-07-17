from blog import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("post/<int:post_id>/", views.post, name="post"),
    path("", views.blog, name="home"),
    path("exemplo", views.exemplo, name="exemplo"),
]
