FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFEDED 1

RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /code

RUN pip install --upgrade pip

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 8000

CMD [ "python3", "main.py" ]