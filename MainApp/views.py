from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def view_home(request):
    author = 'Шиховцов'
    text = f'''<h1>"Изучаем django"</h1>
           <strong>Автор</strong>: <i>{author}</i>'''
    return HttpResponse(text)


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
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]


def view_item(request, id):
    name = ''
    for i in items:
        if i["id"] == id:
            name = i["name"]
    if name:
        return HttpResponse(name)
    else:
        return HttpResponseNotFound(f'Товар с id={id} не найден')


def view_items(request):
    names = []
    for i in items:
        names.append(f'<li>{i["id"]}: {i["name"]}</li>')
    return HttpResponse('<ul>'+''.join(names)+'</ul>')