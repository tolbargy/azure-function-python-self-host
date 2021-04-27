import json
import logging
import requests

import azure.functions as func

def main(event: func.EventGridEvent, inputblob: func.InputStream):
    eventData = event.get_json()

    url = eventData['url']
    logging.info('Python DetectBadItems function started processing a blob file: %s', url)
    logging.info(eventData)
    logging.info(inputblob)

    if inputblob:
        processImage(img_bytes=inputblob.read(), url=url)
        logging.info('Python DetectBadItems function finished processing a blob file: %s', url)
