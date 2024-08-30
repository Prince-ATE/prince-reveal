# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver" "0.0.0.0:8000"]