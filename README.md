# social-media-posts

[![codecov](https://codecov.io/gh/Petatron/social-media-posts-backend/graph/badge.svg?token=NQSZTckJmr)](https://codecov.io/gh/Petatron/social-media-posts-backend)


## Get Started
**Step 1.** Set up `python3-pip`
```
apt install python3-pip
```
for Linux, or
```
curl https://bootstrap.pypa.io/get-pip.py | python3
```
for MacOS

**Step 2.** Install required dependencies with `requirements.txt`
```
pip3 install -r requirements.txt
```
**Step 3.** Set up [PostgreSQL server](https://hub.docker.com/_/postgres/) and Django environment under Docker
```
make postgres
make django
```
Checkout [Makefile](Makefile) for the commands running under the hood.

**Step 4.** Tryout by running `manage.py`
```
python3 manage.py runserver
```
In your browser, you should see a webpage at `localhost:8000` with 404 error. This means the server is ready to respond to requests. 

Now you can use Postman to emulate requests to this server.