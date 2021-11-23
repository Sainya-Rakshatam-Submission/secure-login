# Secure Login Challenge
This project addresses all the web vulnerabilities and implements login system in a secure way

**Web vulnerabilities addressed**
- Cross Site Forgery Request
- Clickjacking
- SQL/NoSQL/LDAP/XML Injection
- XSS Attack
- Response Manipulation
- Sensitive Information Disclosure
- Authentication Bypass
- Parameter Pollution & Mass Assignment
- Credentials Over Unencrypted Channel
- Missing Brute-Force Protection
- User Enumeration
- Throttling Requests
- Remote Code Execution

## **Hosting Guide**

### 1. Download the code
First install git in the system, then type the following command in `command prompt`
```console
git clone https://github.com/Sainya-Rakshatam-Submission/secure-login.git
cd secure-login
```

### 2. Setup the Virtual Environment
Install `python-3.9` in the system, then run the following command in the console
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
[Click here for the video explanation](https://youtu.be/6iw5sA89gMo)

### 4. Migrate the sql queries to the database
Now in console run the following command
```console
python manage.py migrate
```
### 5. Create a superuser for the site
To create a superuser for the site run the following commands line by line in the sole
```console
python manage.py createsuperuser
```
after running the command provide the necessary details it asks

### 6. Compress the static files
To compress the static files then run the following command in the console
```console
python manage.py collectcompress
```

### 7. Edit the CORS and ALLOWED_HOST header
Make sure to edit the `CORS` and `ALLOWED_HOST` header, otherwise you won't be able to access the site from the desired attched domain. [Click here to goto the CORS and ALLOWED_HOST header](https://github.com/Sainya-Rakshatam-Submission/secure-login/blob/master/securelogin/settings.py#L172)

### 8. Edit the THROTTLING REQUESTS bumber
Make sure to edit the `AXES_FAILURE_LIMIT` confiiguration, this is the max number of failed login attempts, Defaults to 5. [Click here to goto the THROTTLING REQUESTS configuration](https://github.com/Sainya-Ranakshetram-Submission/secure-login/blob/master/securelogin/settings.py#L215)

### 8. Now run the project
For the `windows` users, run the following command
```console
python manage.py runserver
```

and for the `Linux` and `Mac` users, run the following command
```console
gunicorn securelogin.asgi:application -k securelogin.workers.DynamicUvicornWorker --timeout 500
```

Kamboom! The site is up on http://127.0.0.1:8000 in local environment, now the credentials that you have given while creating the superuser using the createsuperuser command.

## Youtube Video Explaining all

[![Secure Coding Challenge | Submission](http://img.youtube.com/vi/6iw5sA89gMo/0.jpg)](http://www.youtube.com/watch?v=6iw5sA89gMo "Secure Coding Challenge | Submission")
