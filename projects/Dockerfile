
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install flask redis pandas

EXPOSE 5000

CMD ["python", "app.py"]
