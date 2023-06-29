FROM python:3.10-bullseye

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]