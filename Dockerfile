FROM python:3.10

WORKDIR /test

COPY . /test

RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]

EXPOSE 5000

