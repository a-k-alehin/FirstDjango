from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

def view_home(request):
    return render(request, "index.html")


def view_about(request):
    about = {
        "name_f": "Иван",
        "name_s": "Петрович",
        "name_l": "Иванов",
        "phone": "vasya@mail.ru",
        "email": "8-923-600-01-02",
    }
    text = f'''
<div><b>Имя</b>: {about["name_f"]}</div>
<div><b>Отчество</b>: {about["name_s"]}</div>
<div><b>Фамилия</b>: {about["name_l"]}</div>
<div><b>телефон</b>: {about["phone"]}</div>
<div><b>email</b>: {about["email"]}</div>
'''
    return HttpResponse(text)


def view_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар с id={id} не найден')
    context = {"item": item}
    return render(request, "item.html", context)    


def view_items(request):
    context = {"items": Item.objects.all()}
    return render(request, "items.html", context)