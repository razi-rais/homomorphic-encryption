FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install python3 -y \
&& apt-get install python3-pip -y \
&& apt-get install libgmp3-dev -y \
&& apt-get install -y libmpfr-dev libmpfr-doc libmpfr4 libmpfr4-dbg \
&& apt-get install libmpc-dev -y \
&& pip3 install phe \
&& pip3 install Flask-API

COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["server.py"]
