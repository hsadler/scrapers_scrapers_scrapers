
# build app container
docker build \
	--no-cache \
	-f=Dockerfile \
	-t=scrapers_scrapers_scrapers:local .

# run docker container with exposed port
docker run -it --rm \
    -p=80:80 \
    --name=scrapers_scrapers_scrapers \
    scrapers_scrapers_scrapers:local

# example of running a volume for the application files:
# docker run -it --rm \
#     -v=$PWD:/go/src \
#     -p=8090:8090 \
#     --name=go_web_app go_web_app:local \