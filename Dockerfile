# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to avoid Python buffering
ENV PYTHONUNBUFFERED 1

# Install system dependencies including Tesseract OCR
RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    libsm6 \
    libxext6 \
    libxrender-dev && \
    apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "app.py"]
