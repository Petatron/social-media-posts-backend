postgres:
	docker pull postgres:latest # Pull postgres image
	docker build -t postgresdjango . # Build postgres image
	docker run --name django -p 5433:5432 -d postgresdjango # Run container

django:
	docker start django # Start container

migrate:
	python manage.py migrate # Migrate database

env:
	conda env export > environment.yml # Export environment
	python convert.py # Convert environment.yml to environment.yaml

conda:
	conda update -n base conda # Update conda
	conda update --all command # Update all packages