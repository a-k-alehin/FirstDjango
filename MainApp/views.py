from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def view_home(request):
    return render(request, "index.html")


about = {
    "name_f": "Иван",
    "name_s": "Петрович",
    "name_l": "Иванов",
    "phone": "vasya@mail.ru",
    "email": "8-923-600-01-02",
}


def view_about(request):
    text = f'''
<div><b>Имя</b>: {about["name_f"]}</div>
<div><b>Отчество</b>: {about["name_s"]}</div>
<div><b>Фамилия</b>: {about["name_l"]}</div>
<div><b>телефон</b>: {about["phone"]}</div>
<div><b>email</b>: {about["email"]}</div>
'''
    return HttpResponse(text)


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def view_item(request, id):
    item = next((i for i in items if i["id"]==id), None)
    if item is not None:
        context = {"item": item}
        return render(request, "item.html", context)
    else:
        return HttpResponseNotFound(f'Товар с id={id} не найден')


def view_items(request):
    context = {"items": items}
    return render(request, "items.html", context)