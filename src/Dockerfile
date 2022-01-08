FROM python:3.8-slim

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Bundle application source
COPY ./src /src

# Start application
CMD ["uvicorn", "src.main:APP", "--host", "0.0.0.0", "--port", "8000"]
