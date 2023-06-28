FROM python:3.10-bullseye

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY ./app ./app

ENTRYPOINT [ "python", "main.py" ]