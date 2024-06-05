postgres:
	docker pull postgres:latest
	docker build -t postgresdjango .
	docker run --name django -p 5433:5432 -d postgresdjango

django:
	docker start django

migrate:
	python manage.py migrate