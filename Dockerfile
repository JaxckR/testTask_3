FROM python:3.12-slim
RUN groupadd -r groupadmin && useradd -r -g groupadmin admin

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip

WORKDIR weatherApp/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod -R 777 *

WORKDIR src/

EXPOSE 8000

USER admin

RUN python manage.py collectstatic