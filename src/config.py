import os

# Environment paths
APP_PATH = f"{os.path.dirname(__file__)}"+"/"
ENV_PATH = APP_PATH+"../.env"
JSON_PATH = f"{APP_PATH}../accounts.json"

# Text colours
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
VIOLET = "\x1b[35m"
CYAN = "\x1b[36m"