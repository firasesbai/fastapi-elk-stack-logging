FROM python:3.8-slim

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Bundle application source
RUN mkdir /src/
COPY . /src

# set workdir
WORKDIR /src

# Start application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
