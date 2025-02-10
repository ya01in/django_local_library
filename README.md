# django_local_library

django_local_library from mdn web doc. Local Library website written in Django

## Status

part 4 done

## Content

### Create Project

* Create a development environment for Django4.0* using virtualenvwrapper
  * `mkvirtualenv [env-name]`
  * `workon [env-name]`
  * `deactivate`
  * `rmvirtualenv [env-name]`
* Create git ignore
* Learn start and stop server using manage.py
  * `python3 manage.py runserver`

### Create Framework

* Learn to create skeleton website using python package: django-admin
  * `django-admin startproject [project-name]`
* Understand Django framwork, applications, urlmapper
* Create application using manage.py
  * `python3 manage.py startapp <app-name>`
* Database Migration
  * `python3 manage.py makemigrations`
  * `python3 manage.py migrate`

### Create Model

* Model design
* Model definitions
  * Fields
  * Metadata
  * Methods
  * Methods
* Types of field
* Model relationships
* Model manipulation

### Create Task for migration

* Setting up VSCode Task
* Create task for model and database migration

### Admin site

create admin site using project's admin.py, added data through it and customize admin view using ModelAdmin class.

* Create admin view
* Customize admin view
  * inline display
  * list display
  * section display
  * filter

### Create Views

Learn to create simple URL maps and views (where no data is encoded in the URL), get data from models, and create templates.

#### Flow

1. Determine what information we want to display in our pages
2. Define the URLs to use for returning those resources.
3. Create a URL mapper, views, and templates to display the pages.

#### url mapper -> view functions -> templates

* url mapping
* index page
* function based view generation
* html templates
* static resources
