FROM python:3.8-slim-buster

WORKDIR /app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN pip install --upgarde pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . . 

# COPY ./entrypoint.sc /
# ENTRYPOINT ["sh","/entrypoint.sh"]

CMD ["gunicorn", "--bind", ":8000", "--timeout 0", "--workers", "3", "dzt_ocr.wsgi:application"]
#ENTRYPOINT [“gunicorn”, “work.wsgi:application”, “--bind”, “0.0.0.0:8000”]
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]