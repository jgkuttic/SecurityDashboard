# Installation Guide 
### Required Resources 
 + Run a local configuration of the application via Linux Ubuntu 16.04 or later. 
 + Versions: 
     - Django v1.9
     - AngularJS v1.7
     - Python 2.7
     - PostgreSQL v9.6

##### Follow the steps below to configure the correct environment (assumes clean build with no current dependencies): 
+ Install Git
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```

+ Download source code from repository 
```
git clone https://github.ncsu.edu/engr-csc-sdc/2016FallTeam03.git 
cd 2016FallTeam03
```
+ create virutal environment
```
sudo apt-get install python-virtualenv --fix-missing
virtualenv env
cd env
source bin/activate
```
+ Intsall requirements for project
```
pip install -r ../requirements.txt
```
+ Install PostgreSQL and dependencies
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
sudo apt-get install python-dev
sudo apt-get install python3-dev
```
+ Install pgAdmin, django and dependencies
```
sudo apt-get install libpq-dev --fix-misisng
wget https://ftp.postgresql.org/pub/pgadmin3/pgadmin4/v1.1/pip/pgadmin4-1.1-py2-none-any.whl
pip install pgadmin4-1.1-py2-none-any.whl
gedit lib/python2.7/site-packages/pgadmin4/config.py
Change SERVER MODE: False
python lib/python2.7/site-packages/pgadmin4/setup.py
```
Start pgAdmin4
```
python lib/python2.7/site-packages/pgadmin4/pgAdmin4.py
Navigate to: localhost:5050
```
+ Open new terminal(CTRL + SHIFT + TAB)
+ Activate virtual environment and install django
```
source bin/activate
pip install django
pip install djangorestframework
pip install django-filter
pip install django-cors-headers
pip install django-nose
pip install requests
```
+ Add user for postgres
```
sudo gedit /etc/postgresql/9.3/main/pg_hba.conf
CHANGE lines: 
# Database administrative login by UNix domain socket 
local   all        postgres                                     trust
# TYPE  DATABASE        USER            ADDRESS                 METHOD
# "local" is for Unix domain socket connections only
local   all             all                                     trust
sudo service postgresql restart
sudo -u postgres psql
ALTER USER postgres PASSWORD 'csc492team3';
\q
```

+ Install npm, node and bower
```
sudo apt-get install npm nodejs
sudo npm install -g bower
```
+ Install all the dependencies for the Web App
```
sudo npm install
```

### Starting PgAdmin, Django, and AngularJS
#### Once the environment is configured, follow this short list of commands to run each component of the application.

 + Start pgAdmin4
```
cd 2016FallTeam03/env
source bin/activate
python lib/python2.7/site-packages/pgadmin4/pgAdmin4.py
Navigate to: localhost:5050
```
+ Open new terminal(CTRL + SHIFT + TAB)
+ Start Django
```
cd 2016FallTeam03/env
source bin/activate
cd 2016FallTeam03/ContextualDashboard
python manage.py migrate (only done once, or as updates are applied)
python manage.py runserver
```

+ Start Web App
```
cd 2016FallTeam03/env
source bin/activate
cd 2016FallTeam03/angular-seed-master/app
sudo npm start
```

+ Django Testing
  - start pgAdmin and Django
```
cd 2016FallTeam03/ContextualDashboard/dashboard/
../manage.py test --pattern="test.py" 
```





