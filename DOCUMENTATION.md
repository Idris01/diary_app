# Diary API
This is a simple django Diary API that performs CRUD operations

## Installation Procedure (Using Git Bash)
The installation procedure is as detailed below

- Clone the repository from ```https://github.com/idris01/diaryapi.git``` 

- Move into the cloned Directory  ```cd diary_api```
> Note: The current version of python 3 is required to for this app

- inside the ``` diaryapi``` run the python command ``` pip install pipenv ``` and wait for the the installation to complete.

pipenv is a python package that is used in creating a virtual environment for specific project, this is very helpful because of likely variation in peoject dependecies, such that a project will be isolated with its own dependecy.

- At the completion of ```pipenv``` installation run the command ```pipenv shell``` to activate the virtual environment, next run the commamd ```pipenv install``` to install all project dependecies

- Move into the project directory ```cd backend``` and run the following commands:
 * ```python3 manage.py makemigrations diary``` ,this command sets up the sqlite database by converting the python code into sql code.

 * ```python3 manage.py migrate```  this command creates the db.sqlite3 database.

 * finally run ```python3 manage.py runserver``` to start the server.




