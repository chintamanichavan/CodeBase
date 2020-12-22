# For versioning use specific version 
FROM node:lts-alpine

WORKDIR /app

# Catching and Layers
ADD package*.json ./

RUN npm install

ADD . .

CMD node index.js