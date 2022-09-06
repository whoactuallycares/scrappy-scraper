FROM postgres:14.5

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres
ADD init.sql /docker-entrypoint-initdb.d/
#COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
#CMD ["psql", "-U", "postgres", "-w", "-c", "postgres", "CREATE TABLE listings(\"id\" VARCHAR PRIMARY KEY, \"name\" VARCHAR, \"price\" VARCHAR, \"location\" VARCHAR, \"image_urls\" VARCHAR);"]