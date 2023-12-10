FROM python:3.10
WORKDIR /WhatsMyName
COPY main/main.py /WhatsMyName

RUN apt-get update && apt-get install tor -y
RUN pip3 install requests BeautifulSoup4 pyfiglet clint PySocks urllib3

CMD tor > /dev/null & exec python3 main.py
