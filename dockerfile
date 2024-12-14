# Use Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files from GitHub repository
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/fkr00t/ascify.git . && \
    apt-get remove -y git && apt-get autoremove -y

# Install application dependencies
RUN pip install --no-cache-dir .

# Set the entry point for the `ascify` command-line tool
ENTRYPOINT ["ascify"]

# Set the default argument (can be overridden at runtime)
CMD ["-h"]
