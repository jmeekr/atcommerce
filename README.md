Atcommerce
----------

For the full description see this [gist](https://gist.github.com/bmuller/3ddc2e0319727c1b02f2a45cc9360064)  
For the test file see this [pastebin](https://pastebin.com/raw/ZKWDLhxw)

This take home test assumes files are a TSV,
where fields are separated by `\t` and rows are
separated by `\n`. Which are then stored in a database
and viewed.

Branches
--------

There are two working branches `dev` and `fix_queries`,
and a `dev-rebase` branch for `master`. 

Install
-------

This is a pretty standard Django installation.
See the `requirements.pip` file for specific libraries.

Create virtualenv for Python 3.6.

* `python3 -m venv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage migrate`
* `python manage runserver`
* Access on `localhost:8000` by default.
* Dashboard view is on `/v1/api/dashboard/`
* File Upload view is on `/v1/api/upload`
* Upload a TSV and then move over to the dashboard to view.

About
-----

We are using a Sqlite3 database because it's quicker to setup
than a full Postgres installation.

The `settings.py` is a little customized.  Notably we
raise an exception is there is no env variable `SECRET` for
the secret key. While for debug it does not matter it's always better
to take the precautions ahead of time.

We did not have time to write a playbook for deployment, but usually
we throw one inside the root of the Django project.

This project is using the Django Rest Framework for a 'dashboard' view.
Since it gives us a quick api view.

The User Model is still based on the default django user model, the idea
was to create a User Profile, and have user authorize through `/auth/login`
to be able to access the api endpoints.

Most of what is notable for the project is in the api module.
Which is broken down into two types of views.  Django Rest Framework
views are under dashboard.  Regular Django views are under views.
Models are under models.

There was a decision that if a record is updated in the TSV we update that 
record in the database.  Realistically we probably want to save that
information, and create a field for 'updated_time' and maybe more meta
information.

TODO
----

Write tests...

Unfortunately we spent a lot of time trying to work through the boiler plate
for Django and DRF since it's been a while.  Also spent a lot of time fighting
with QuerySets, to setup a proper setUp tearDown case.

Otherwise we would do two methods.  One would be a mock file which sends the
test file's data directly to the parser and test the function of parsing.

We would also test uploading the file directly with a request object against
the api.

We _really_ need to validate the TSV file, since it is probably a database dump
it is probably okay for now.

We need to decide on fields which can and cannot be NULL.

We need to save the model for the file uploads by user, and description, and
also authenticate that the user is logged in.

Create a deployment strategy using Nginx, Gunicorn, and Postgresql.

Uploading Files References
---------------
* [Django Docs](https://docs.djangoproject.com/en/2.0/ref/models/fields/)
* [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)

Misc
----

We say we, which is me, because 'I' don't believe in first person for
projects.
