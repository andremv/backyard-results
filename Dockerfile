# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory to the container
COPY . .

# Expose the port on which the web app will run
EXPOSE 8000

# Start the web app
CMD ["python", "app.py"]
