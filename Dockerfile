FROM python:3.10
WORKDIR /Echo-Tracker
COPY main.py /Echo-Tracker

RUN apt-get update && apt-get install tor -y
RUN pip3 install requests BeautifulSoup4 pyfiglet clint PySocks urllib3 tqdm

CMD tor > /dev/null & exec python3 main.py
