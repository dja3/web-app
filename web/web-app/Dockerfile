FROM node:8-alpine
MAINTAINER David Adams "djadams7211@gmail.com"
COPY . /web-app
WORKDIR /web-app
RUN npm install
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]