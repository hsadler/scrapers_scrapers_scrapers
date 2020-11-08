
up:
	sh up.sh

build:
	docker build \
	--no-cache \
	-f=base.Dockerfile \
	-t=scrapers_scrapers_scrapers.base:v1 .