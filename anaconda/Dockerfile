FROM debian:latest
MAINTAINER Quan Zhou "public_zhou@outlook.com"

RUN wget -O - http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-2.1.0-Linux-x86_64.sh | \
    bash - -b && \
    rm Anaconda-2.1.0-Linux-x86_64.sh
ENV PATH /root/anaconda/bin:$PATH 
