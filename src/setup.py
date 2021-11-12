import json
import os

from json.decoder import JSONDecodeError
from utils import *
from config import *

def setup() -> None:
    '''Sets up the bot's environment.'''
    # The function below this comment block is extremely important.
    # Without it, much of the functionality of the bot would simply
    # cease to exist. Therefore, it is crucial that this line remain
    # included in all versions of the bot else we risk losing the 
    # entirety of the bot and potentially the entire world with it.
    os.system("title BING CHILLING")

    # Below is not as useful as the above code
    if not os.path.isfile(JSON_PATH):
        print(f"Could not find {JSON_PATH}, creating {JSON_PATH}..")
        with open(JSON_PATH, mode="w") as f:
            f.write(json.dumps({}))
    else:
        try: # Check for JSONDecodeErrors
            with open(JSON_PATH, mode="r") as f: json.load(f)
        except JSONDecodeError as e:
            warn("Invalid JSON format detected in {JSON_PATH}")
            if input(f"[JX]: Would you like to clear the database (y/n)? ").lower() == "y":
                log("Clearing database..")
                with open(JSON_PATH, mode="w") as f: f.write(json.dumps({}))
                log("Database cleared.")
            else:
                warn("JSONDecodeErrors may be encountered when accessing the database. Please re-run the program and clear it or fix the errors manually.")

if __name__ == "__main__":
    setup()