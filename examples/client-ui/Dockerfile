FROM ubuntu:16.04

RUN apt-get update \
&& apt-get install python3 -y \
&& apt-get install python3-pip -y \
&& pip3 install Flask-API \
&& pip3 install flask_cors \
&& pip3 install requests

COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["app.py"]
