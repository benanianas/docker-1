FROM ubuntu

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 && apt-get install -y python3-pip
RUN pip3 install Django
WORKDIR /var/www
RUN django-admin startproject django_app
WORKDIR /var/www/django_app
COPY ./views.py /var/www/django_app/django_app
COPY ./urls.py /var/www/django_app/django_app
RUN python3 manage.py migrate
RUN echo "ALLOWED_HOSTS = ['10.12.6.15']" >> django_app/settings.py
CMD  python3 manage.py runserver 0.0.0.0:8000

#docker build -t django
#docker run -it -p 8000:8000 django
