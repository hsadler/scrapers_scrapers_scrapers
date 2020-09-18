# parent image
FROM python:3.6-alpine

# OS installs
RUN apk add --no-cache \
	bash \
    vim