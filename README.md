
# scrapers_scrapers_scrapers

A collection of my web scrapers

---

## Run the app

### build the base image

```sh
docker build \
    --no-cache \
    -f=base.Dockerfile \
    -t=scrapers_scrapers_scrapers.base:v1 .
```

### spin-up the container for web scraping

```sh
sh spin_up.sh
```
