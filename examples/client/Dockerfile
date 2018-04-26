FROM ubuntu:16.04

RUN apt-get update \
&& apt-get install python3 -y \
&& apt-get install python3-pip -y \
&& apt-get install libgmp3-dev -y \
&& apt-get install -y libmpfr-dev libmpfr-doc libmpfr4 libmpfr4-dbg \
&& apt-get install libmpc-dev -y \
&& pip3 install phe \
&& pip3 install Flask-API \
&& pip3 install flask_cors \
&& pip3 install requests

COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["client.py"]
