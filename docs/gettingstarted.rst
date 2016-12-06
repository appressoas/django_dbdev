###############
Getting started
###############


*******
Install
*******
::

    $ pip install django_dbdev


*****************************
Configure your Django project
*****************************
Add ``django_dbdev`` to ``INSTALLED_APPS``, and setup one of the database backends (below).


Setup for PostgreSQL
====================
Add the following to your Django settings::

    from django_dbdev.backends.postgres import DBSETTINGS

    DATABASES = {
        'default': DBSETTINGS
    }


Setup for MySQL
===============
Add the following to your Django settings::

    from django_dbdev.backends.mysql import DBSETTINGS

    DATABASES = {
        'default': DBSETTINGS
    }


.. note::

    If you use the mariadb or mysql packages for homebrew on OSX, you
    must also set :obj:`~django.conf.settings.DBDEV_MYSQL_BASEDIR` as
    an environent variable or Django setting. We recommend using an
    environment variable to avoid affecting other developers on the
    same project, and because it allows you to fix it for all your
    Django projects.

    For mariadb it will look something like this::

        export DBDEV_MYSQL_BASEDIR=/usr/local/Cellar/mariadb/10.0.10/

    The version number will vary. For mysql the only difference will be
    the name of the directory (mysql instead of mariadb).


****************************
Avoiding port-number-crashes
****************************
If you are developing multiple projects simultaneously, or just have 
a lot of stuff running on various ports and want to avoid a crash, 
you can specify the port for dbdev by adding this line below ``DATABASES``
in ``settings.py``::

    DATABASES['default']['PORT'] = <my_random_port_number>
    
where `my_random_port_number` is the port you want your dbdev-database to 
run on. We recommend using a port somewhere in the range 20.000-50.000.


*****************************************
Developing for multiple database backends
*****************************************
The ``dbdev_testproject`` explained in :doc:`develop` in an example of one such
setup. The only thing required is a way of specifying which DB backend to use,
and that can be done in many ways.
