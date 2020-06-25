# Django ActivityManager

This is a simply application which looks at the activity periods of different users.

## Install Requirements

```python
pip install -r requirements.txt
```

## Populating Dummy Records

To create dummy records on the Database, run the below command:

```python
python manage.py generate_random admin@example.com
```

The above command runs a custom `manage.py` management command. It first creates an admin user `admin@example.com`, with password `demo`, if such as user doesn't exist already.

It then creates 10 dummy user records on the database.

## Running the Server

To run the server, use:

```python
python manage.py runserver 0.0.0.0:8000
```

Now, go to the login page using `http:SERVER_IP:8000/login` and login with any user or admin credentials.

# Demo Application

Server URL Link (Hosted using PythonAnywhere): http://accornition.pythonanywhere.com

Sample Admin Credentials:
```
Email: admin@example.com
Password: demo
```
