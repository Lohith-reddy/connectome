FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock* ./

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev --no-root

# Copy application code
COPY src/ ./src/
COPY frontend/ ./frontend/
COPY .env.example .env

# Create necessary directories
RUN mkdir -p data artifacts logs

# Install the package
RUN poetry install --no-dev

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-m", "brain_connectivity.main"]
