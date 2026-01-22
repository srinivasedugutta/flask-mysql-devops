version: "3.8"

services:
  mysql:
    image: mysql:8.0
    container_name: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: flaskdb
      MYSQL_USER: flaskuser
      MYSQL_PASSWORD: flaskpass
    volumes:
      - mysql_data:/var/lib/mysql

  flask:
    image: docker.io/srinivasedugutta/flask-mysql-app:latest
    container_name: flask_app
    restart: always
    ports:
      - "8080:5000"
    depends_on:
      - mysql
    environment:
      DB_HOST: mysql
      DB_USER: flaskuser
      DB_PASSWORD: flaskpass
      DB_NAME: flaskdb

volumes:
  mysql_data:

