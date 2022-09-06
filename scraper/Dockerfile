FROM python:3.10-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY dbConnector.py dbConnector.py 
COPY scraper.py scraper.py 

CMD ["python3", "scraper.py"]