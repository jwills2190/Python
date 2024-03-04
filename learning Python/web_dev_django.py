# library is a collection of functions.
# frameworks is a bit more, collection of modules. 
# Deep dive into MVC and the process. Get really good at it.

# Windows - command prompt, Mac - terminal
# Basic commands: 
    # mkdir: make directory = create folder for project. (mkdir project_one)
    # navigate to folder or file with cd 
    # move out one file or folder with cd ..
    # Windows: dir to see folders and files, mac = ls
    # To create files: Mac = touch(followed by file name), Windows = echo > (filename)

# Open VS code project folder
# Export and import modules with 'from (filename) import (function name);
    # Do this to use files in more than one place, as well as the functions.
# Django needs a virtual environment to run. May need to install virtual environment.
# **** V IMPORTANT!!!! python -m virtualenv venv ***** - for Windows
# install virtual environment, comes as library, use PIP or python package manager. Think of it as an app store, knows how to install it. Never google and then download library
# pip install virtualenv - initialize virtual environment with virtualenv venv
# venv\scripts\activate - done every time you want to run a project

# install libraries only with virtual environment activated.
# pip install django
# pip install pillow
# always want to be using exact same libraries, version and everything.
# pip freeze > requirements.txt = where you save text files
# initialize django project with = django-admin startproject (project name)

# __init__.py is an empty file that makes a folder a python module. Typically don't have to do anything with it.
# ASGI & WSGI are entry points from server to app. This about them when you deploy to live server. We don't have to worry about them now.
# Settings is a main file where you find all global settings for your project.
    # keep secret_key secret. You get a new one for every project.
    # Allowed_hosts is where you would put allowed IP addresses or domain names.
    # Installed_Apps are preinstalled modules ready to use. think of modules as blocks, and we will be building out own modules.
    # .admin module is a small program that builds back end for site administration. You can build everything from scratch, but if you want to build something simple you can do so.
    # .auth module is for authenticating users. 
    # .contenttypes - responsible for tracking relations between different tables
    # ROOT_URLCONF - URL dispatcher
    # templates - HTML files. One and the same. provide where django might find HTML 
# urls.py is the url dispatcher. this is where paths are held.

#---------------------------------------------------------------------------------#

# First things first, create database. cd into project folder, then to manage.py file
# command python manage.py - gives you list of commands.
# migrate and makemigrations: usually confusing
    # Schema's are already in place, we'll build our own schema and models.
    # makemigrations creates blueprint for database based on the schema. need to create fields you want in your database.
    # migrate will actually create the database.
# first makemigrations command then migrate. However, when you create first project there are schemas in place. 
# python manage.py migrate - creates our database.
# Must use 'python manage.py' ahead of commands.
# if we check dir in our project folder, you'll see db.sqlite3 database!
# next create superuser with 'python manage.py createsuperuser'
# python manage.py runserver - django comes with built in server
    # you will receive something like - Starting development server at http://127.0.0.1:8000/
    #open this in the broswer 
# ctrl + c stops the server.
# startapp command will help you to create a module/app. python manage.py startapp (name)
# The first thing you should do after you run command python manage.py startapp is take the name after our new project and add it on the setting.py file under INSTALLED_APPS.
# navigate to models.py file in your project folder
# open the new folder in your editor and now there is MVC. views.py = controller, models.py = M, and V = templates/HTML which we will create.
# classes ALWAYS begin with capital letters. Class is a blueprint to create an object.
# after you're done with your model, run python manage.py makemigrations to setup the blueprint.
# Then run python manage.py migrate once again.
# in migrations folder there is a 0001_initial file. There is an 'id' that is automatically added because relational databases require a unique identifier or primary key.
# then run python manage.py migrate to apply migrations.
# got the admin.py file in your project folder. Then import the model to the admin.py file.
# admin.site.register('model name')

#-----------------------------------------------------------------#

# Now that we have the db setup and we can add data according to our models..
# Create a view. 
# Implement CRUD. First view is list, which renders everything from database. Second is detail or individual item list. This step is implemented in views.
# Then we create URL which goes in URL.py
# Third step is need HTML template
# -> from django.views.generic.list import ListView at top of views.py file
# -> create class with model name and ListView
# -> Make sure to import model.
# open urls.py and import the model from the other folder. add the urlpatterns like so
    # from django.contrib import admin
    # from django.urls import path
    # from garage.views import CarsListView

    # urlpatterns = [
    #     path('admin/', admin.site.urls),
    #     path('allcars/', CarsListView.as_view(), name="cars_list")
    # ]
# then you go to your project folder and create a folder in it called templates. Then another folder inside templates with the same name as the project folder. if the project folder is garage, you create a templates folder in it, then another garage folder inside the templates folder.
# you'll receive an error stating "Exception Value: garage/cars_list.html"
# create a html file using the name of the missing error file.
# Then we basically use python version of EJS to render stuff onto DOM.

# For detailed view we go to views.py and import from django.views.generic.detail import DetailView
# add a dynamic pyrameter such as - path("allcars/<int:pk>/",CarDetailView.as_view(), name="detail_list") under urlpatters.
# the Detail View class should look something like this. class CarDetailView(DetailView): model = Cars
# Then create a detail view html file.
# We type on html doc with {%%}. and start with {% for i in object_list %}. Closing for loops with {% endfor %}
# to make items clickable we need 'from django.urls import reverse' on models.py file

# Then we add this on the file -  def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})

# use something like ( <a href={{car.get_absolute_url}}>{{car.make}} {{car.model}}</a>) on list html file to get links to individual pages.
# static files vs media files. 