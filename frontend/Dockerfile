# pull official base image
FROM node:lts-alpine

# set work directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN apk update 
RUN npm install

# copy project
COPY ./ .

# build app for production with minification
RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]

# https://linuxtut.com/en/09384726105eee53bbb6/
# https://v2.vuejs.org/v2/cookbook/dockerize-vuejs-app.html