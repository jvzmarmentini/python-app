FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app .

EXPOSE 8000

CMD ["python3", "main.py", "--host", "0.0.0.0", "--port", "8000"]
