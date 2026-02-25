FROM apache/spark:4.1.1

# Set working directory inside container
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Default command: run your script
CMD ["spark-submit", "main.py"]
