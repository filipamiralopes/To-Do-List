<img src="https://www.devopsgroup.com/wp-content/uploads/2019/05/devopsgroup_devops_playbook_one_ring_001-03.svg" alt="Ring One" width="100"/>

# To-do List

Live here: https://middle-earth-to-do-list.herokuapp.com/ 

## Description
Simple Django RESTful API for a to-do list.

### Instructions
From your command line, navigate to where you want to save this project and create a new directory:\
`mkdir todolist`\
`cd todolist`

Once in this directory, create a virtual environment and activate it:\
`virtualenv venv`\
`source venv/bin/activate`

Copy and clone this github repo. Once done navigate to the project folder:\
`git clone git@github.com:filipamiralopes/ToDoList.git`\
`cd ToDoList`

And install the necessary requirements:\
`python -m pip install --upgrade pip`\
`python -m pip install -r requirements.txt`

The following instructions to install PostgreSQL are based on macOS and assuming you have Homebrew:\
`brew install postgresql`\
`brew services start postgresql`

Create a database in your Postgres server:\
`psql postgres`\
`CREATE DATABASE db_todolist;`\
`\c db_todolist` - this should connect you to the database\
`CREATE USER db_user;`\
`\q` - to leave the postgres server

Run these commands:\
`python manage.py makemigrations`\
`python manage.py migrate`

Create the default superuser:\
`python manage.py createsuperuser`

Set your `.env` file (you can find a .env.example in the directory of this project, just copy and rename it to .env)

And run the Django server:\
`python manage.py runserver`\
And navigate into: http://127.0.0.1:8000/

Go to this route and add the credentials you did while creating superuser:
http://127.0.0.1:8000/admin/

In order to run tests, run the following command within the project folder:\
`python manage.py test api.tests`\
or for a specific set of tests:\
`python manage.py test api.tests.test_tasks`
