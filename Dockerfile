FROM python:3.10

WORKDIR /app

COPY ./requirements.txt  /app/requirments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirments.txt

COPY ./* /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

