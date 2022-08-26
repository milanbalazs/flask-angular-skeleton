FROM nginx:1.19.2-alpine

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./*.conf /etc/nginx/
COPY ./docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD [""]
