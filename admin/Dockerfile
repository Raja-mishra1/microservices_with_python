FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
# Switches to a non-root user and changes the ownership of the /app folder"
RUN useradd appuser && chown -R appuser /app
USER appuser
CMD python manage.py runserver 0.0.0.0:8000
