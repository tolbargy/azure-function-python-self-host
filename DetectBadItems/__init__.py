import json
import logging
import requests

import azure.functions as func

def main(servicebus: func.ServiceBusMessage, inputblob: func.InputStream):
    logging.info('Python DetectBadItems function started processing a message service bus: %s', servicebus)
    logging.info('Python DetectBadItems function started processing a blob file: %s', inputblob)    