import sys
sys.path.append('..')

from service.scrape_samtrygg import ScrapeSamtrygg

scrape_result = ScrapeSamtrygg.scrape()
with open("/test_scrape.txt", "w") as f:
    f.write(scrape_result)