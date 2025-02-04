# syntax=docker/dockerfile:1

# Set Python version as an argument (for easy version upgrades).
ARG PYTHON_VERSION=3.13.1
FROM python:${PYTHON_VERSION}-slim as base

# Prevent Python from writing pyc files and buffering stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies needed for mysqlclient and build tools
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    python3-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements.txt before source code for Docker caching optimization
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-privileged user for the app to run under.
ARG UID=10001
RUN adduser --disabled-password --gecos "" --home "/nonexistent" --shell "/sbin/nologin" --no-create-home --uid "${UID}" appuser

# Switch to the non-privileged user
USER appuser

# Copy the source code into the container.
COPY . .

# Expose the application port.
EXPOSE 8000

# Run the application.
CMD ["waitress-serve", "--port=8000", "webstore.wsgi:application"]
