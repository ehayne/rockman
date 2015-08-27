FROM python:2.7.9

RUN mkdir -p /src /out /data /media

RUN pip install dj-database-url==0.3.0
RUN pip install django==1.8.2
RUN pip install django-app-namespace-template-loader==0.3
RUN pip install django-admin-bootstrapped==2.5.0
RUN pip install django-blog-zinnia==0.15.2
RUN pip install django-bootstrap3==5.4.0
RUN pip install django-braces==1.8.0
RUN pip install django-debug-toolbar==1.3
RUN pip install django-jinja==1.4.1
RUN pip install django-photologue==3.2
RUN pip install flake8==2.4.0
RUN pip install gevent==1.0.2
RUN pip install gunicorn==19.3.0
RUN pip install jinja2==2.7.3
RUN pip install logan==0.7.1
RUN pip install markupsafe==0.23
RUN pip install mots-vides>=2015.2.6
RUN pip install pbr==1.1.1
RUN pip install psycopg2==2.6.1
RUN pip install pytest==2.7.2
RUN pip install pytest-cov==1.8.1
RUN pip install pytest-capturelog==0.7
RUN pip install pytest-django==2.8.0
RUN pip install pytest-mock==0.5.0
RUN pip install python-social-auth==0.2.11
RUN pip install pytz==2015.4
RUN pip install zinnia-theme-bootstrap==0.4

WORKDIR /src
COPY ./src/ /src

# This is to make pbr work
RUN git init
RUN python setup.py develop
RUN app migrate

EXPOSE 8000
CMD ["app", "start"]
