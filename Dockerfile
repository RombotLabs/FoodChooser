# Use an official Python runtime as a parent image
FROM python:3.14.0-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first for better Docker caching
COPY flask/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY flask/ flask/

# Switch to the Flask app directory
WORKDIR /app/flask

# Set environment variables (disable debug mode in production)
ENV FLASK_ENV=production

# Run the app with Gunicorn (production-grade WSGI server)
# -w 4 = 4 worker processes
# -b 0.0.0.0:5000 = bind to all interfaces on port 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
