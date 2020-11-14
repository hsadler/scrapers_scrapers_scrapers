
FROM scrapers_scrapers_scrapers.base:v1

# python installs
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy app
COPY ./app /app

# copy cron scripts
COPY ./crons /etc/periodic/

# add crons to crontab
RUN echo "* * * * * run-parts /etc/periodic/1min" \
    >> /etc/crontabs/root
RUN echo "0 8 * * * run-parts /etc/periodic/9am" \
    >> /etc/crontabs/root
RUN echo "0 12 * * * run-parts /etc/periodic/1pm" \
    >> /etc/crontabs/root
RUN echo "0 17 * * * run-parts /etc/periodic/6pm" \
    >> /etc/crontabs/root

# set permissions
RUN chmod -R 777 /etc/periodic

# set working directory
WORKDIR /app

# start crond and flask server
CMD ["sh", "startup.sh"]
