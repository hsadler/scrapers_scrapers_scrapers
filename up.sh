
# build app container
docker build \
    --no-cache \
    -f=Dockerfile \
    -t=scrapers_scrapers_scrapers:local .

# run docker container with exposed port
docker run -it --rm \
    -v=$PWD/app:/app \
    -v=$PWD/crons/1min:/etc/periodic/1min \
    -v=$PWD/crons/15min:/etc/periodic/15min \
    -p=80:80 \
    --name=scrapers_scrapers_scrapers \
    scrapers_scrapers_scrapers:local
