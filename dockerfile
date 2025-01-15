# Use Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (xclip for clipboard support on Linux)
RUN apt-get update && apt-get install -y \
    xclip \  # Required for clipboard functionality on Linux
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Copy the application files from the local directory
COPY . .

# Install application dependencies
RUN pip install --no-cache-dir .

# Set the entry point for the `ascify` command-line tool
ENTRYPOINT ["ascify"]

# Set the default argument (can be overridden at runtime)
CMD ["-h"]