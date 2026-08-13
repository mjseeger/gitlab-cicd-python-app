FROM python:3.12-slim

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Run as a non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

CMD ["python", "-m", "app.main"]
