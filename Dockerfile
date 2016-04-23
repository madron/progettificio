FROM madron/uwsgi

MAINTAINER Massimiliano Ravelli <massimiliano.ravelli@gmail.com>

# Packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y python-psycopg2 python-imaging python-lxml \
    && rm -rf /var/lib/apt/lists/*

# Requirements
COPY requirements /src/requirements
RUN    pip install -r /src/requirements/prod.txt

# Source
COPY . /src
RUN chmod 755 /src/manage.py

# Nginx site
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /src/
ENV DJANGO_SETTINGS_MODULE=settings.prod

# Collect static files
RUN /src/manage.py collectstatic --link --noinput --verbosity=0

VOLUME ["/run/uwsgi"]

ENTRYPOINT ["/src/docker/entrypoint.sh"]
CMD ["uwsgi", "--master", "--processes", "1", "--threads", "1", "--http-socket", ":8000", "--chdir", "/src", "--python-path", "/src/apps",  "--wsgi", "settings.wsgi", "--stats", ":9191"]
