FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /photo_service

COPY requirements.txt ./
RUN pip install -r requirements.txt
