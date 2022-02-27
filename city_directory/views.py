from django.shortcuts import render


def main(req):
    l = ["Москва", "Нью-Йорк", "Сингапур"]
    path = req.path.replace('/', '')
    if path == '':
        path = "index"
    return render(req, f"{path}.html", {
        "cities": l
    })
# Create your views here.
