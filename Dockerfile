 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /blog
 WORKDIR /blog
 ADD . /blog/
 RUN pip install -r requirements.txt
 RUN python manage.py makemigrations blog
 RUN python manage.py migrate blog
 ADD . /blog/