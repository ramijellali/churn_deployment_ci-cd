# Use a smaller base image
FROM python:3.9-slim

WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies without cache to reduce size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Run the API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
