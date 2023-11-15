FROM python:alpine3.18
RUN apk add --no-cache tzdata
ENV TZ=America/Bogota
WORKDIR /app 
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./launch.py