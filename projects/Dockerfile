# Slim python base image to reduce storage
FROM python:3.9-slim

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

# Installing dependencies needed
RUN pip install --upgrade pip && \
    pip install flask redis pandas

# Exposing the port that my app runs on
EXPOSE 5000

# commands to run my application 
CMD ["python", "app.py"]
