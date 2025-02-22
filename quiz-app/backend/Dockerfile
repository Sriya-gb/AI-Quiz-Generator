# Use an official Python runtime as base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

#  Create a writable cache directory
RUN mkdir -p /app/cache

#  Set environment variables
ENV TRANSFORMERS_CACHE="/app/cache"
ENV HF_HOME="/app/cache"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 7860

# Run FastAPI using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
