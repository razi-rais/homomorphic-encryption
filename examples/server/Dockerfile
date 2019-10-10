FROM ubuntu:16.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
&& apt-get upgrade -y
RUN apt-get install -y python3  \
&& apt-get install -y python3-pip  \
&& apt-get install -y libgmp3-dev  \
&& apt-get install -y  libmpfr-dev libmpfr-doc libmpfr4 libmpfr4-dbg \
&& apt-get install -y libmpc-dev
RUN pip3 install phe \
&& pip3 install Flask-API

COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["server.py"]
