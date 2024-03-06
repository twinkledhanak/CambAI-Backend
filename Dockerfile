FROM python:3.9

# Install dependencies
RUN pip install huey redis re fastapi asyncio

# Copy your Huey application code into the container
COPY . /app
#COPY ./src ./app

# Set the working directory
WORKDIR /app

EXPOSE 3000

# Command to run the Huey application
#CMD ["huey_consumer.py", "huey_queue"]
CMD [ "python", "src/Controllers/KeyValueController.py" ]
