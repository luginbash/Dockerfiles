FROM debian:wheezy
MAINTAINER Quan Zhou "public_zhou@outlook.com"

ENV ANACONDA_VERSION=2.3.0-Linux-x86_64

RUN apt-get update && \
    apt-get install -y axel bzip2 openssl && \
    rm -rf /var/lib/apt/lists/*

RUN axel -n5 -a http://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-$ANACONDA_VERSION.sh && \
    bash  Anaconda-$ANACONDA_VERSION.sh -b && \
    rm Anaconda-$ANACONDA_VERSION.sh

RUN /root/anaconda/bin/ipython profile create

RUN HOSTNAME=$(cat /etc/hostname) && \
    openssl req \
    -new \
    -days 365 \
    -nodes \
    -x509 \
    -subj "/C=US/ST=CA/L=SFO/O=myIPythonNoteBook/CN=$HOSTNAME" \
    -out /root/.ipython/profile_default/ipy.pem \
    -keyout /root/.ipython/profile_default/ipy.key

ENV PATH /root/anaconda/bin:$PATH

COPY profile_default /root/.ipython/

RUN ipython notebook --ip=0.0.0.0 &
EXPOSE 8888
