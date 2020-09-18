
FROM scrapers_scrapers_scrapers.base:v1

# python installs
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy app
COPY ./app /app

# prepare cron dirs
RUN mkdir /etc/periodic/1min
RUN chmod -R 777 /etc/periodic

# add 1 minute cron folder to crontab
RUN echo "*       *       *       *       *       run-parts /etc/periodic/1min" \
    >> /etc/crontabs/root

# set working directory
WORKDIR /app

# CMD ["crond", "-f"]

# ENTRYPOINT ["python"]
# CMD ["server.py"]
