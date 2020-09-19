
FROM scrapers_scrapers_scrapers.base:v1

# python installs
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy app
COPY ./app /app

# prepare cron dirs
RUN mkdir /etc/periodic/1min

# add 1 minute cron folder to crontab
RUN echo "* * * * * run-parts /etc/periodic/1min" \
    >> /etc/crontabs/root

# set permissions
RUN chmod -R 777 /etc/periodic

# set working directory
WORKDIR /app

# start crond and flask server
CMD ["sh", "startup.sh"]
