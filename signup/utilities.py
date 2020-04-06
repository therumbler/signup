import logging
import os
import re

logger = logging.getLogger(__name__)

VALID_AUTH_TOKEN = os.environ["VALID_AUTH_TOKEN"]
def check_auth_header(header):
    authorized = False
    token = None
    try:
        token = re.search(r"Basic (.*)", header).group(1)
    except AttributeError:
        logger.error('cannot find token in header %s', header)
    
    if token == VALID_AUTH_TOKEN:
        authorized = True
    
    logger.info('authorized = %s', authorized)
    return authorized


