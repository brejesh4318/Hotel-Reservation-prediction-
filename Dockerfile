FROM python:slim

# Avoid writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy all files into the image
COPY . .

# Install Python dependencies (editable mode or normal requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Run your training pipeline (if required at build time – usually not recommended)
# If this is just for deployment, remove the line below
# RUN python pipeline/training_pipeline.py

# Expose a port (optional if you’re running an API)
EXPOSE 5000

# Run your application (make sure "application.py" exists and is executable)
CMD ["python", "application.py"]


