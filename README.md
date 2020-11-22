
# scrapers_scrapers_scrapers

A collection of web scrapers. 

Currently includes configurable scraping for Samtrygg and Blocket rental listings.

---

## Run the app

### build the base image

```sh
make build-base
```

### spin-up the container for web scraping

```sh
make up
```

## Samtrygg listings scraper

### Define your scrape configuration in file:
```
app/config/samtrygg_processing.py
```
Note: `rank options` is not currently used

The scraper runs on a cron every 15 minutes.

### View scrape results via browser:
All Samtrygg results:
```
http://localhost/samtrygg/all
```
Relevant Samtrygg results:
```
http://localhost/samtrygg/relevant
```

## Blocket listings scraper

### Define your scrape configuration in file:
```
app/config/blocket_scrape_config.py
```

### View scrape results via browser:
Relevant Blocket results:
```
http://localhost/blocket/relevant
```
Note: hitting this endpoint causes multiple Blocket API calls to occur. Use with caution.






