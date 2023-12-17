from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.forms import FormWithCaptcha


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = FormWithCaptcha(request.POST)

        if form.is_valid():
            pass
    else:
        form = FormWithCaptcha()

    context = {
        'form': form,
    }

    return render(request, "core/index.html", context)
