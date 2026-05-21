FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt manage.py /app/
RUN pip install --no-cache-dir -r requirements.txt \
    python manage.py migrate

COPY data  /app/
RUN python manage.py loaddata ./data/MainApp.json

COPY FirstDjango static  /app/

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]