# P3_20231202

https://django.fun/docs/django/4.2/topics/http/urls/#example

https://django.fun/docs/django/4.2/topics/db/queries/

https://django.fun/docs/django/4.2/topics/templates/


https://stackoverflow.com/questions/54639428/v-s-code-v1-31-emmet-intellisense-not-working-with-python-django-extensions



    python manage.py dumpdata --indent 4 MainApp >data/MainApp.json




    python manage.py shell_plus --bpython
    c_red = Color(1,'red')
    c_red.save()
    i = Item.objects.get(id=1)
    i.colors.add(c_red)
    i.save()
    i.colors.all() #показать цвета
    # отфильтровать
    i = Item.objects.filter(colors__name='green')
    

