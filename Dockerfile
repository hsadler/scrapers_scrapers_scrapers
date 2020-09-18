
FROM scrapers_scrapers_scrapers.base:v1

# python installs
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy app
COPY ./app /app
WORKDIR /app

# ENTRYPOINT ["python"]
# CMD ["server.py"]
