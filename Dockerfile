FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential libffi-dev ffmpeg aria2 python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "modules/main.py"]

