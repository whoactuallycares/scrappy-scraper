FROM python:3.10-buster
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

COPY site.py site.py 
COPY dbConnector.py dbConnector.py 
EXPOSE 8080/tcp
COPY src /var/www
CMD ["python3", "site.py"]