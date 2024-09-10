# social-media-posts

[![codecov](https://codecov.io/gh/Petatron/social-media-posts-backend/graph/badge.svg?token=NQSZTckJmr)](https://codecov.io/gh/Petatron/social-media-posts-backend)


## Get Started
**Step 1.** Environment setup
- Use `python3-pip`:
```
apt install python3-pip
```
or
```
curl https://bootstrap.pypa.io/get-pip.py | python3
```
- Use `Conda`:
```
https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links
```
Make sure you have set up the conda executable in your PATH and in your IDE like PyCharm.


**Step 2.** Install required dependencies with dependencies manager `pip` or `conda` with the dependencies file `requirements.txt` or `environment.yml` respectively inside project.
```
pip3 install -r requirements.txt
```
or
```
conda env create -f environment.yml
```
then activate the environment
```
conda activate social-media-posts
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

**Step 5.** Make API requests

Now you can use Postman to emulate requests to this server.
- User registration: `POST` request to `http://localhost:8000/api/auth/register/` with JSON body
```
{
    "username": "mosausesa21assq",
    "first_name": "Mickey",
    "last_name": "Mouse",
    "password": "12345678",
    "email": "moausqqqseasq@yopmail.com"
}
```
- User login: `POST` request to `http://localhost:8000/api/auth/login/` with JSON body
```
{
    "password": "12345678",
    "email": "moausqqqseasq@yopmail.com"
}
```
- User lookup: `GET` request to `http://localhost:8000/api/user/`
- Get refresh token: `POST` request to `http://localhost:8000/api/auth/refresh/` with JSON body
```
{
    "refresh": " "
}
```
- Create post: `POST` request to `http://localhost:8000/api/post/` with JSON body
- Make sure to include the `Authorization` header with the value `Bearer TOKEN` where `TOKEN` is the access token from the login response.
```
{
    "author": "<author_id>",
    "body": "A simple post"
}
```
- Like a post: `POST` request to `http://localhost:8000/api/post/post_id/like/` with JSON body. Make sure to include the `Authorization` header with the value
Bearer TOKEN. For unlike a post, use `POST` request to  `http://localhost:8000/api/post/post_id/unlike/`.