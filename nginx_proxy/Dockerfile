FROM nginx:1.12

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install --assume-yes python-pip python-dev python-setuptools build-essential
RUN pip install j2cli

ADD nginx.conf.j2 /
ADD nginx-site.conf.j2 /
ADD uwsgi_params /etc/nginx/conf.d/uwsgi_params
ADD docker-entrypoint.sh /

RUN chmod a+rx /docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
