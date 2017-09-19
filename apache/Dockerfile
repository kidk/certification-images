FROM httpd:2.4-alpine

COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY src/ /usr/local/apache2/htdocs/
RUN mkdir /var/log/apache
