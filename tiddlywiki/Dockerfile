FROM debian:wheezy
MAINTAINER Quan Zhou "public_zhou@outlook.com"

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get install -y nodejs && \
    npm install -g tiddlywiki

RUN tiddlywiki mywiki --init server

RUN tiddlywiki --server

EXPOSE 8080
