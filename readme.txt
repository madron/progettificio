# Build
docker build -t madron/progettificio .

# Run tests
docker run --rm -e DJANGO_SETTINGS_MODULE=settings.test madron/progettificio /src/manage.py test

# Run
docker-compose up

# Enjoy
http://localhost


# cms fixtures
./manage.py dumpdata --indent=4 cms djangocms_text_ckeditor > progettificio/fixtures/progettificio.json
