FROM python:3.9-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy our producer code
COPY src/ ./src

# run the producer
CMD ["python", "src/producer.py"]
