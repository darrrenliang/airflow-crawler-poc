import requests
import logging
import sys

# logger level settings
logging.basicConfig(
    filename='crawler.log', 
    filemode='w',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# crawler funciton
def crawler(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("Website endpoint:  %s", url)
            logging.info("Website status code:  %s", response.status_code)
            # logging.info(response.text)
        else:
            logging.error("Failed to crawl website: %s", response.status_code)
    except Exception as e:
        logging.error("An error occurred while crawling website: %s", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawler.py <url>")
        sys.exit(1)

    website_url = sys.argv[1]
    crawler(website_url)
