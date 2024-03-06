# ## Like an instruction file to copy your image (contents,application) to container 

# # Start your image with a node base image
# FROM node:18-alpine

# # The /app directory should act as the main application directory
# WORKDIR /app

# # Copy the app package and package-lock.json file
# #COPY package*.json ./

# # Copy local directories to the current local directory of our docker image (/app)
# COPY ./src ./src
# #COPY ./public ./public

# # Install node packages, install serve, build the app, and remove dependencies at the end
# # RUN npm install \
# #     && npm install -g serve \
# #     && npm run build \
# #     && rm -fr node_modules

# EXPOSE 3000

# # Start the app using serve command
# CMD [ "serve", "-s", "build" ]


FROM python:3.9

# Install dependencies
RUN pip install huey redis fastapi asyncio

# Copy your Huey application code into the container
COPY . /app
#COPY ./src ./app

# Set the working directory
WORKDIR /app

EXPOSE 3000

# Command to run the Huey application
#CMD ["huey_consumer.py", "huey_queue"]
CMD [ "python", "src/Controllers/KeyValueController.py" ]
