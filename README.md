
This web application is the source code for StudyWhere. It is built with Python and Django.

Set Up:
1. create folder for project
2. Add virtual env
	* virtualenv env (creates the virtual environment)
    * source env/bin/activate (activates the virtual env)
3. Install django/djangorest
	* pip3 install django djangorestframework
4. Clone the project into the project folder
5. Install pillow to allow for images
	* pip install pillow
6. Install Google Map Package
	* pip install django-google-maps (add it to settings.py installed apps)
7. Install Map Widgets (search bar, markers)
	* pip install django-map-widgets (add it to settings.py installed apps)
	* [docs](https://media.readthedocs.org/pdf/django-map-widgets/latest/django-map-widgets.pdf)
8. Install Bootstrap
	* pip install react-bootstrap3 (add it to settings.py installed apps)

If you don't already have these:
	* brew install gdal geos
	* brew install proj

The first time you use the app:
	python manage.py makemigrations
	and then
	python manage.py migrate

To see the app in the browser:
	python manage.py runserver

