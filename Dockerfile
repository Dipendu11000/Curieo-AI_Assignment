FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
COPY main.py input.txt /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

