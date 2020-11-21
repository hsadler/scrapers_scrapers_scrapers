
build-base:
	docker build \
	--no-cache \
	-f=base.Dockerfile \
	-t=scrapers_scrapers_scrapers.base:v1 .

build-app:
	docker build \
	--no-cache \
	-f=Dockerfile \
	-t=scrapers_scrapers_scrapers:local .

run-app:
	docker run -it --rm \
	-v=$(PWD)/app:/app \
	-v=$(PWD)/crons/1min:/etc/periodic/1min \
	-v=$(PWD)/crons/15min:/etc/periodic/15min \
	-v=$(PWD)/datastore:/datastore \
	-p=80:80 \
	--name=scrapers_scrapers_scrapers \
	scrapers_scrapers_scrapers:local

sh-app:
	docker run -it --rm \
	-v=$(PWD)/app:/app \
	-v=$(PWD)/crons/1min:/etc/periodic/1min \
	-v=$(PWD)/crons/15min:/etc/periodic/15min \
	-v=$(PWD)/datastore:/datastore \
	-p=80:80 \
	--name=scrapers_scrapers_scrapers \
	scrapers_scrapers_scrapers:local /bin/bash

up: run-app
