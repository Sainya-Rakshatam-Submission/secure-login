# Secure Login Challenge
This project addresses all the web vulnerabilities and implements login system in a secure way
## **Hosting Guide**

### 1. Download the code
First install git in the system, then type the following command in `command prompt`
```console
git clone https://github.com/Sainya-Rakshatam-Submission/secure-login.git
cd secure-login
```

### 2. Setup the Virtual Environment
Install `python-3.9` in the system, then type the following command in the console
```console
pip install virtualenv
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```
Now rename `example.env` to `.env` and now see this video on how to setup the `.env` file.

### 3. Setup the database
If you are in local environment then the project will automatically use the `sqlite` unless speficied the database url in the `.env` file.
Following `DATABASE URL`'s are supported [Click Here](https://github.com/jacobian/dj-database-url#url-schema)
And then install its respective database connector module from `pypi`.
If you are in `LOCAL` environment then no need to install the database connector module since it will be using sqlite :)

### 4. Migrate the sql queries to the database
Now in console type the following command
```console
python manage.py migrate
```
### 5. Create a superuser for the site
To create a superuser for the site type the following command in the sole
```console
python manage.py createsuperuser
```
after running the command provide the necessary details it asks

### 6. Compress the static files
To compress the static files then type the following command in the console
```console
python manage.py collectcompress
```

### 7. Now run the project
For the `windows` users, type the following command
```console
python manage.py runserver
```

and for the `Linux` and `Mac` users, type the following command
```python
gunicorn securelogin.asgi:application -k securelogin.workers.DynamicUvicornWorker --timeout 500
```

