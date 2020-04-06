import logging
import os

from signup.web import make_app
logger = logging.getLogger(__name__)

VALID_AUTH_TOKEN = os.environ["VALID_AUTH_TOKEN"]


app = make_app()



