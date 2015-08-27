FROM python:2.7.9

RUN mkdir -p /src /out /data /media

RUN pip install dj-database-url==0.3.0 \
                django==1.8.2 \
                django-app-namespace-template-loader==0.3 \
                django-admin-bootstrapped==2.5.0 \
                django-blog-zinnia==0.15.2 \
                django-bootstrap3==5.4.0 \
                django-braces==1.8.0 \
                django-debug-toolbar==1.3 \
                django-jinja==1.4.1 \
                django-photologue==3.2 \
                flake8==2.4.0 \
                gevent==1.0.2 \
                gunicorn==19.3.0 \
                jinja2==2.7.3 \
                logan==0.7.1 \
                markupsafe==0.23 \
                mots-vides>=2015.2.6 \
                pbr==1.1.1 \
                psycopg2==2.6.1 \
                pytest==2.7.2 \
                pytest-cov==1.8.1 \
                pytest-capturelog==0.7 \
                pytest-django==2.8.0 \
                pytest-mock==0.5.0 \
                python-social-auth==0.2.11 \
                pytz==2015.4 \
                zinnia-theme-bootstrap==0.4

WORKDIR /src
COPY ./src/ /src

# This is to make pbr work
RUN git init
RUN python setup.py develop
RUN app migrate

EXPOSE 8000
CMD ["app", "start"]
