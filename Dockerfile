# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask source code
COPY src/ ./src

# Set environment variables for Flask
ENV FLASK_APP=src/hk_monitoring.py
ENV FLASK_RUN_HOST=0.0.0.0


# Run the Flask app
CMD ["python", "src/hk_monitoring.py"]

