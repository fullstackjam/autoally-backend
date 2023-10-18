# Use an official Python runtime as the base image
FROM python:3.10.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
