postgres:
	# docker pull postgres:latest
#	docker rm -f postgres15
#	docker run --name django -e POSTGRES_USER=core -e POSTGRES_PASSWORD=faicist117 -e POSTGRES_DB=coreDB -p 5433:5432 -d postgres:latest
	docker build -t postgresdjango .
	docker run --name django -p 5433:5432 -d postgresdjango

django:
	docker start django