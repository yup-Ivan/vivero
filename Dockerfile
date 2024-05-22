FROM python:3.10.10-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]