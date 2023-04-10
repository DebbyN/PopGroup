# Dockerfile

# Loading the Python used
FROM python:3.10-slim-buster

# Working directory for the app in the image
WORKDIR /app

# Copies the requirements.txt from the computer where created to the image
COPY requirements.txt requirements.txt

# Installs the requirements specified in the requirements file
RUN pip3 install -r requirements.txt

# Copies all files from the same directory
COPY . /app

EXPOSE 8000

# runs the server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]