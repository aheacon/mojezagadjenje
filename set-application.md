---
title: "Getting started with django"
author: Anel Husakovic
date: March 9, 2020
output: project
---

### Install virtualenv
- Install `pip` and `pip3`\
```
$ sudo apt-get -y install python-pip
$ sudo apt-get -y install python3-pip
$ pip --version
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
$ pip3 --version
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```
- Latest version of pip
```
>> python3 -m pip install --user --upgrade pip
>> python3 -m pip --version
pip 20.0.2 from /home/anel/.local/lib/python3.6/site-packages/pip (python 3.6)
```
- Install packages using pip (python package manager used to install and update packages) and virtual [env1](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

  When using python3 or newer it is better to use [venv](https://docs.python.org/3.6/library/venv.html#module-venv).
  ```
  $ sudo apt install python3-venv
  $ python3 -m venv -h
  ```
  Additionally (pip install virtualenwrapper) (see bellow more or in Project: django and nginx)

### 1) Create virtualenvironment
---
  To create virtual environment, recommended way is to use:\
  `python3 -m venv env`
* python3 (`-m` => module script)

  This will place virtual env (a `bin/`, `lib/`, `lib64/`, `share/`, etc) in folder.
  
  In order to delete `rm -rf /path/to/env`

### 2) Get into virtualenvironment
----
`$ source env/bin/activate` \
- environment variable will be modified;\
- to exit from virtual env: `$ deactivate`
```
echo $PATH #inside of environment
/home/anel/aheacon/mojezagadjenje/env/bin:#REST OF PATH
```
- `$ which python && which python3`
  ```
  /home/anel/aheacon/mojezagadjenje/env/bin/python
  /home/anel/aheacon/mojezagadjenje/env/bin/python3
  ```
Inside `env/bin` there are python2 and python3 exectuables.

### 3) Install django => "django-admin.py"
---
* Before starting the new project make sure you are in `env` and you have installed module django.
```
$ pip3 install django
$ python -m django --version # python3 is not working here
$ which django-admin
/home/anel/aheacon/mojezagadjenje/env/bin/django-admin
$ django-admin version
3.0.4
```
#### 3.1) Start new project in django
* To start the [new project](https://docs.djangoproject.com/en/3.0/intro/tutorial01/#creating-a-project) use __django-admin startproject project-name__.\
We will have to be in `env`.
```
$(env) django-admin startproject my_pollution
$(env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ pwd
/home/anel/aheacon/mojezagadjenje/my_pollution
$(env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ ls -l
total 8
-rwxr-xr-x 1 anel dell  632 Mar  9 13:19 manage.py
drwxr-xr-x 2 anel dell 4096 Mar  9 13:19 my_pollution
$(env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution/my_pollution$ ls -l
total 16
-rw-r--r-- 1 anel dell  401 Mar  9 13:19 asgi.py
-rw-r--r-- 1 anel dell    0 Mar  9 13:19 __init__.py
-rw-r--r-- 1 anel dell 3106 Mar  9 13:19 settings.py
-rw-r--r-- 1 anel dell  754 Mar  9 13:19 urls.py
-rw-r--r-- 1 anel dell  401 Mar  9 13:19 wsgi.py
```
  We will get directory with some auto-generated code.\
  Top directory is name of project, and the same name bellow is for the application directory.
### 4) Run the application
---
* Already here we can start the development server which is missing some migrations:
```
(env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

March 09, 2020 - 12:22:13
Django version 3.0.4, using settings 'my_pollution.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[09/Mar/2020 12:22:20] "GET / HTTP/1.1" 200 16351
[09/Mar/2020 12:22:20] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[09/Mar/2020 12:22:20] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[09/Mar/2020 12:22:20] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[09/Mar/2020 12:22:20] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[09/Mar/2020 12:22:20] "GET /favicon.ico HTTP/1.1" 404 1978
```
#### 4.1) Create the application
When running this parent a [django-admin](https://docs.djangoproject.com/en/1.11/ref/django-admin)

* Start django application using: __python3 manage.py startapp application-name__
- Name of project `my_pollution` cannot be the same as name of app `my_pollution`.
```
# Previous example with different name
(env) anel@anel:~/my_playground/django/my_projects$ python enroll_students/manage.py startapp enroll_students
CommandError: 'enroll_students' conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.
```
- It is better to give application a different name, different from project name.
- Even better is to create name of app with prefix `_app`, for example: `_app_pollution_1`.
```basj
(env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ python3 manage.py startapp _app_pollution_1
(env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ ls -la
total 20
drwxr-xr-x 4 anel dell 4096 Mar  9 13:24 .
drwxr-xr-x 5 anel dell 4096 Mar  9 13:19 ..
drwxr-xr-x 3 anel dell 4096 Mar  9 13:24 _app_pollution_1
-rw-r--r-- 1 anel dell    0 Mar  9 13:22 db.sqlite3
-rwxr-xr-x 1 anel dell  632 Mar  9 13:19 manage.py
drwxr-xr-x 3 anel dell 4096 Mar  9 13:22 my_pollution
```
  This project directory (from project, not app) has `settings.py` where can be found variable `INSTALLED_APPS` where we need to register our app.
  - Delete the app [link](https://stackoverflow.com/questions/35745220/how-to-remove-an-app-from-a-django-projects-and-all-its-tables):
    - If app is not registered, just `rm -rf`.
    - If yes we have to delete it from `settings.py`.
#### 4.2) Start the server
* Development server, automatic reload\
	`python manage.py runserver 0:8000  # for all hosts on network; without 0: only localhost`
  - However, we should migrate table to get rid of warnings.
#### 4.3) Migrate the tables
* **Migration** means to migrate tables from `INSTALLED_APPS` found in `my_pollution/settings.py`(`django.contrib.admin` etc), 
- Also change in the same folder `Time_zone` to `Europe/Sarajevo` 
##### 4.3.1) Migrate the tables for default django setup
- Apply migration with **./manage.py migrate** or: \
`python manage.py migrate`
  ```bash
  (env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ ./manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
  Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying sessions.0001_initial... OK
  (env) anel@eacon:~/aheacon/mojezagadjenje/my_pollution$ ./manage.py runserver
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  March 09, 2020 - 15:34:46
  Django version 3.0.4, using settings 'my_pollution.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```

##### 4.3.2) Register apps  '_my_app.apps.MyAppConfig'
* From `_app_pollution_1/apps.py` register app by adding `'_app_pollution_1.apps.AppPollution1Config'` to `settings.py`
* It is good to create a custom `_app_pollution_1_/urls.py` per application, since Django looks `<project-name>/urls.py` (`my_pollution/urls.py`) not our application specific one, so we have to link it (application specific url) by __include__ that file to `my_pollution/urls.py`.
* Create functions in views of application and use `HttpResponse` in views to send to browser.

##### 4.3.3) Migrate the tables for specific application
  We will later specify for which app we want migration ex.\
  `python manage.py migrate _app_pollution_1`.

#### 4.4) Setup the database
* Setting up the datebase:
- In order to use `mariadb` install :\
`pip install django mysqlclient`
In production above line didn't work, workaround:
`pip install --upgrade setuptools.` -> not working\
`sudo apt-get install python3-de libmysqlclient-dev` -> worked
/// not working with pip3 /// mysqlclient-1.4.6
[digital-ocean-link](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)
- Change to mysql: [set database](https://docs.djangoproject.com/en/3.0/ref/settings/#databases) (support for [MariaDB](https://docs.djangoproject.com/en/dev/ref/databases/#mariadb-notes) in `django 3.0`) in `<project>/settings.py`\
  - change configuration for [auth-plugin](https://stackoverflow.com/a/54072297) in `/etc/mysql/conf.d`
  - For [not-auth-plugin solution](https://mariadb.com/kb/en/error-logging-in/).
- For `sqlite`:\
	`sudo apt-get install sqlite3 libsqlite3-dev`
- Had some problems in configuring mariadb:\
    Workaround:
    - Make sure you delete `~/.my.cnf`
    - Install mariadb (10.1) - **not recommended** [how to install](https://linuxize.com/post/how-to-install-mariadb-on-ubuntu-18-04/): 
    `$ sudo apt update && sudo apt install mariadb-server`
    - Delete if you have already installed:
    ```bash
      $ sudo apt-get remove --purge mariadb-server mariadb-client
      $ sudo apt-get autoremove
      $ sudo apt-get autoclean
      $ sudo apt-get install mariadb-server mariadb-client 
    ```
    - **Recommended** way to install mariadb `10.4` is from [mariadb repo](https://downloads.mariadb.org/mariadb/repositories/#distro=Ubuntu&distro_release=bionic--ubuntu_bionic&mirror=yongbok&version=10.4):
    ```bash
      $ sudo apt-get install software-properties-common
      $ sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'
      $ sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://mariadb.mirror.triple-it.nl/repo/10.4/ubuntu bionic main'
      $ sudo apt update
      $ sudo apt install mariadb-server
      - **Creating a new user**
      - Log in with `root` user: `sudo mysql` and create a new user, or
      use `unix_socket`,
      - Or create a new user with `mysqld_safe`:
    ```
    - Stop the service: `sudo systemctl stop mysql`
    - Start `mysqld_safe`
    ```bash
      $ sudo mysqld_safe --skip-grant-tables &
    ```
    - Log in into unprotected server `mysql`
    - Execute script: `source create_user_mysqld_safe.sql;` or do it manually:
      * `flush privileges`;
      * Create new user and grant privileges: 
        ```sql
          $ create user eco_anel identified by 'a'; # host=`%`
          $ select user,host from mysql.user \G 
          $ select * from mysql.global_priv\G # only for 10.4
          # we will have to add grants to user here
          $ show grants for 'eco_anel'@'%';
          $ select * from mysql.user where user='eco_anel'\G
          $ grant all privileges on *.* to 'eco_anel'@'%';
        ```
    - Stop the mysqld_safe (or `sudo kill -9 PID`):\
    `sudo mysqladmin shutdown`
    - Start the `mysql` service, start the client and create your database: \
    ```bash
      $ sudo systemctl start mysql
      $ mysql -u eco_anel -p
      >> mysql : 
      >> change password: 
      SET PASSWORD FOR 'eco_anel'@'%' = PASSWORD('newpass');
      >>Login again!
      >> source database_script.sql
    ```
    - [Authentication in mariadb](https://mariadb.org/authentication-in-mariadb-10-4/)
### 5) Working with database
#### 5.1) Using migrations
- **Model** is django object saved in database
- Create a models in `app/models.py`
- **Migration** - changes to already existing database (creating new tables, columns, indexes,etc.)
- Make sure that your app is registered in `settings.py`, under `INSTALLED_APPS`.
- Create a new migrations `./manage makemigrations --help`, test (`--dry-run`)
  ```bash
  ./manage.py makemigrations --dry-run
  Migrations for '_app_pollution_1':
    _app_pollution_1/migrations/0001_initial.py
      - Create model table_co
      - Create model table_h2s
      - Create model table_no
      - Create model table_no2
      - Create model table_nox
      - Create model table_o3
      - Create model table_pm10
      - Create model table_pm25
      - Create model table_so2
  ```
  As can be seen new migration `0001` of application `_app_pollution_1`is created in `_app_pollution_1/migrations`.
- Test sql commands `./manage.py sqlmigration _app_pollution_1 0001` will tell us which queries 
will be executed on database.
- Update migrations(first check `--plan`): `./manage.py migrate --plan`
- I already have created tables and applying migration will create new tables
`_app_pollution_1_table_co` vs `table_co`:
```sql
+-----------------------------+
| Tables_in_ekoforumdb        |
+-----------------------------+
| _app_pollution_1_table_co   |
| _app_pollution_1_table_h2s  |
| _app_pollution_1_table_no   |
| _app_pollution_1_table_no2  |
| _app_pollution_1_table_nox  |
| _app_pollution_1_table_o3   |
| _app_pollution_1_table_pm10 |
| _app_pollution_1_table_pm25 |
| _app_pollution_1_table_so2  |
| auth_group                  |
| auth_group_permissions      |
| auth_permission             |
| auth_user                   |
| auth_user_groups            |
| auth_user_user_permissions  |
| django_admin_log            |
| django_content_type         |
| django_migrations           |
| django_session              |
| table_co                    |
| table_h2s                   |
| table_no                    |
| table_no2                   |
| table_nox                   |
| table_o3                    |
| table_pm10                  |
| table_pm25                  |
| table_so2                   |
+-----------------------------+
28 rows in set (0.001 sec)
```
- However even if `table_co` didn't exist in database, again it would create a name of a table with prefix of application name.
#### 5.2) Using custom data via shell
- Add some custom data using: `./manage.py shell`
- Add some data:
```python
# Import models from application
>>> from _app_pollution_1.models import table_so2
# Not working with the name in the database
>>> from _app_pollution_1.models import _app_pollution_1_table_so2
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: cannot import name '_app_pollution_1_table_so2'
# Create a row
>>> s=table_so2(_city="Zenica", _location="Bilimisce", _value=121);
>>> table_so2.objects.all();
<QuerySet []>
# Save row
>>> s.save();
# Show all rows
>>> table_so2.objects.all();
<QuerySet [<table_so2: SO2 from Zenica: 121 at 2020-03-11 13:52:59.789245+00:00>]>
>>> s=table_so2(_city="Sarajevo", _location="Stup", _value=223);
>>> s.save()
# Show first row
>>> table_so2.objects.first();
<table_so2: SO2 from Zenica: 121 at 2020-03-11 13:52:59.789245+00:00>
>>> table_so2.objects.all();
<QuerySet [<table_so2: SO2 from Zenica: 121 at 2020-03-11 13:52:59.789245+00:00>, <table_so2: SO2 from Sarajevo: 223 at 2020-03-11 13:57:29.101073+00:00>]>
# Delete first row
>>> table_so2.objects.first().delete()
(1, {'_app_pollution_1.table_so2': 1})
>>> table_so2.objects.all();
<QuerySet [<table_so2: SO2 from Sarajevo: 223 at 2020-03-11 13:57:29.101073+00:00>]>
```
The same result there is on database side:
```sql
MariaDB [ekoforumdb]> select * from _app_pollution_1_table_so2;
+----+----------+-----------+--------+----------------------------+
| id | _city    | _location | _value | _date                      |
+----+----------+-----------+--------+----------------------------+
|  2 | Sarajevo | Stup      |    223 | 2020-03-11 13:57:29.101073 |
+----+----------+-----------+--------+----------------------------+
1 row in set (0.001 sec)
```

### 6) Create a views and show data from database
#### 6.1) Adding templates

- By default DjangoTemplates is looking under each app for `templates` subdirectory -> [link](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#write-views-that-actually-do-something)
- Good practice is to __namespace__ templates: example: `<some_folder>/index.html` is calling `<_my_app>/<templates>/<some_folder>/index.html`.
- Do not use variable name with underscore in models like: `_city`.
- Every change will need to run `./manage.py makemigrations && ./manage.py migrate`
- Template inheritance (Django Template Language DTL not Jinja2)
- Redirecting `reverse()` and adding the name of routes

### 7) Web scrapping of data
- Install `beautiful soup` via `pip3` and `selenium`:\
`python3 -m pip install requests`\
`python3 -m pip install --user "beautifulsoup4"`\
or above didn't work-> `pip3 install beautifulsoup4`\
`python3 -m pip install --user "selenium"`\
or above didn't work-> `pip3 install selenium`\
`gecodriver` needed https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
download to `env/bin` or system wide to `/usr/bin`
good [link](https://stackoverflow.com/questions/44723713/python-beautifulsoup-iterating-through-tags-and-attributes)

### 8) Using admin interface app/admin.py 
---
- register models we want to use
- create user
`./manage.py createsuperuser anel`
- login into admin site `localhost:8000/admin`
```python
from .models import Airport, Flight

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.site_header = 'My project'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'My project adminsitration' # default: "Django site admin"
```

### 9) django managment commands
#### 9.1) cron jobs
- Useful [link](https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/)
- `pip install django-cron` # not working for `pip3`
- `settings.py` -> `INSTALLED_APPS`-> `django_crontab`
- create a file `cron.py` and update `settings.py`
```
CRONJOBS = [
    ('*/2 * * * *', '_app_pollution_1_.cron.my_cron_job')
]
```
- `python manage.py crontab add` to create crontab file
- check that file in `crontab -e` (command with hash of cronjob)
- Show crontab
```
$ ./manage.py crontab show
Currently active jobs in crontab:
3986a1f44924b90d4ef2b53c22fbf426 -> ('* * * * *', '_app_pollution_1_.cron.my_cron_job')
```
- Check the cron jobs [crontab-guru](https://crontab.guru/#*_*_*_*_*)
- `python manage.py crontab remove`
- Run the server for changes
- `journalctl -u cron` show messages for unit cron
- No need to restart cron service? `sudo systemctl restart cron`
- Problems with postfix: `sudo apt-get install --reinstall postfix`
- Not needed: `sudo dpkg-reconfigure postfix`
- To disable `MAILTO` use `>/dev/null 2>&1` at the end of cronjob.
#### 9.1.1) Use management commands to be executed in cron job
- Create a cron job via: `crontab -e`
- Alternatively we can write a script to runt hat for us
```

```
- run script as a command in `crontab -e`
https://www.youtube.com/watch?v=2xmfgl-hI9A
- Rename `settings.py` to `settings-shared.py`, create custom file
and create a symlink to `settings.py` which is ignored
- Create `management` directory and `commands` subdirectory where commands will reside and using which can be invoked `python manage my_command`, see [link](https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/)
```bash
$ ./manage.py help
 [_app_pollution_1]
    hello
./manage.py hello Anel --no-color
Hello from CLI "Anel"
```
- Cron job example:
```
$ ./manage.py cron_job --help
$ ./manage.py cron_job
```

#### 9.2) command for deleting all data using django ORM
`./manage.py delete_measurments`
`./manage.py dbshell` to check
```sql
select * from _app_pollution_1_table_co;
```

### 10) Guarding the password
#### 10.1) gitignore
`my_pollution/settings_shared.py`

#### 10.2) Guard via python-decouple - not used
- Guard settings using environment variable or [python-decouple](https://github.com/henriquebastos/python-decouple)
- [talk about pass on github](https://www.youtube.com/watch?v=2uaTPmNvH0I&feature=youtu.be)
- pip install what needed (`unipath`, `dj_database_url`) and change `settings.py`
- exit scale mode and full screen ubuntu VM - `F11`

- Zadaci: 
1. Bolji frontend
2. Podijeliti index html na vise parcijalnih dijelova i includati
3. Prikazati sve podatke po lokacijama
4. Prosiriti i za ostale gradove
5. Istraziti i napraviti listu alarma

### 11) Setting up production
#### 11.1) Script for production (or docker) -> should be checked not sure
We can create a script for production:
```
python3 -m pip install --user --upgrade pip
python3 -m venv env
source env/bin/activate
pip install django
sudo apt install libmysql-client python3-dev
python3 -m pip install requests
pip3 install beautifulsoup4 selenium
```

#### 11.2) How to deploy the server

##### 11.2.1) Create a unit - service /* systemd */
** Follow the link bellow **
Install uwsgi globally (not in venv) `sudo pip3 install uwsgi`.

To check does our application work out of virtual env, make sure to add `/env` to home directory (instead will be `local encoding error`):
```
uwsgi --http 0.0.0.0:9000 --home /home/anel/mojezagadjenje/env --chdir /home/anel/mojezagadjenje/my_pollution --wsgi-file /home/anel/mojezagadjenje/my_pollution/my_pollution/wsgi.py --plugin python36 --master
```
Alternatively we can run this in a `.ini` file and run it `uwsgi test.ini`, where `test.ini`:
```bash
[uwsgi]
home=  /home/anel/mojezagadjenje/env
chdir= /home/anel/mojezagadjenje/my_pollution
wsgi-file=/home/anel/mojezagadjenje/my_pollution/my_pollution/wsgi.py

http=0:9000
```
Insted of `http` we can use sockets, it will be one machine [link](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html), but will need nginx.

Also we want to start this at boot.
In `/etc/systemd/system/` create a file which will be a name of service
For example: `sudo touch mojezagadjenje.service`
Copy the following:
```bash
[Unit]
Description=uWSGI Emperor service
[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown anel:www-data /run/uwsgi'

ExecStart=/usr/local/bin/uwsgi --emperor /home/anel/uwsgi-files
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
[Install]
WantedBy=multi-user.target
```
Make sure that the you have correct user: `anel -> $whoami` and correct group `www-data`.
**Don't forget to restart nginx.** No need to restart `uwsgi` service (it is loaded and inactive)
Service will run a file from `/home/anel/uwsgi-files`.

##### 11.2.2) Create a custom script in `~/uwsgi-files`

Now we need to run `wsgi.py` from project of interest and to create a socket. To do so we weill create `mojezagadjenje.ini` in directory `~/uwsgi-files` (same name as a service, more info needed?)
```bash
[uwsgi]
home = /home/anel
chdir = %(home)/mojezagadjenje/my_pollution/my_pollution
wsgi-file =%(chdir)/wsgi.py
master=true
processes=5

socket = /home/anel/mojezagadjenje.sock
vacuum = true
chown-socket = anel:www-data
chmod-socket = 660
```
##### 11.2.3) Create nginx config file
In `/etc/nginx/sites-available` create file `mojezagadjenje` with 
content bellow and symlink that to `/etc/nginx/sites-enabled` in order to enable it.
```bash
server {
    listen 9000;
    server_name 51.15.114.199;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
      root /home/anel/mojezagadjenje/my_pollution;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/anel/mojezagadjenje.sock;
    }
}
```
Check the firewall: `sudo ufw status`, it can be allowed for specific port only: `sudo ufw allow 8000`.

In general, alternative to application server (uwsgi) is gunicorn.

[Link used for setting up django app with uwsgi](https://medium.com/@panzelva/deploying-django-website-to-vps-with-uwsgi-and-nginx-on-ubuntu-18-04-db9b387ad19d)
[nice one](https://www.devdungeon.com/content/how-deploy-django-nginx-and-uwsgi)
[digital-ocean using init script](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)
[django-deployment](https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/uwsgi/)

### 12) From deployment to locally
- Copy `settings_shared` (from `my_config` local director) and create `settings.py` from `settings_anel.py`
- Create virtual environment:
- Install django
- Install mysqlclient
check for packages (dpkg -ls package): libmysqlclient-dev,(or libmariadbclient-dev/not working missing some dependecies), python3-dev (install with apt)

(https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)
```
python3 -m venv env && \
source ./env/bin/activate && \
pip3 install django &&  \
pip install mysqlclient && \
python3 -m pip install requests && \
pip3 install beautifulsoup4 && \
pip3 install selenium
```
- Run `./manage.py runserver` and go to localhost.
- Finish with venv `deactivate`


