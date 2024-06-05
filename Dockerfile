FROM postgres

ENV POSTGRES_USER core
ENV POSTGRES_PASSWORD faicist117
ENV POSTGRES_DB coreDB

COPY sql/setup.sql /docker-entrypoint-initdb.d/
RUN echo "setup.sql copied to /docker-entrypoint-initdb.d/"