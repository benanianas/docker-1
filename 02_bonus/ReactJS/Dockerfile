FROM ubuntu

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash
RUN apt-get install -y nodejs
RUN npx create-react-app nodeapp
WORKDIR nodeapp

ENTRYPOINT npm start

#docker build -t react
#docker run -it -p 3000:3000 react
