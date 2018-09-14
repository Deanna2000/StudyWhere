
This web application is the source code for StudyWhere. It is built with Python and Django.

Set Up:
1. create folder for project
2. Add virtual env
	* virtualenv env (creates the virtual environment)
    * source env/bin/activate (activates the virtual env)
3. Install django/djangorest
	* pip3 install django djangorestframework
4. Clone the project into the project folder
5. Install bootstrap 3
	* pip install django-bootstrap3
6. Install pillow to allow for images
	* pip install pillow
7. Install Google Map Package
	* pip install django-google-maps (add it to settings.py installed apps)


The first time you use the app or if you make any changes to the models:
	python manage.py makemigrations
	and then
	python manage.py migrate

To see the app in the browser:
	python manage.py runserver



