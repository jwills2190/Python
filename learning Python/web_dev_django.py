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

# Open VS code folder project_one, with two files. 
# Export and import modules with 'from (filename) import (function name);
    # Do this to use files in more than one place, as well as the functions.
# Django needs a virtual environment to run. May need to install virtual environment.
# Command to start virtual environment: virtualenv + folder name
# install virtual environment, comes as library, use PIP or python package manager. Think of it as an app store, knows how to install it. Never google and then download library
# pip install virtualenv - initialize virtual environment with virtualenv venv
# venv/scripts/activate - done every time you want to run a project
# **** V IMPORTANT!!!! python -m virtualenv venv *****
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
# open the new folder in your editor and now there is MVC. views.py = controller, models.py = M, and V = templates/HTML which we will create.
# models is the cornerstone of any app. 
# Slag = used in news, refers to articles. unique identifier. 
# classes ALWAYS begin with capital letters. Class is a blueprint to create an object.
# The first thing you should do after you run command python manage.py startapp is take the name after our new project and add it on the setting.py file under INSTALLED_APPS.
# after you're done with your model, run python manage.py makemigrations to setup the blueprint.

