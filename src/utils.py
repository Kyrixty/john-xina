import datetime
import json
import os
from typing import Any

from config import *

def log(msg: str) -> None:
    '''Logs a message (``msg``).'''
    print(GREEN + "[JX]: " +  msg)

def warn(msg: str) -> None:
    '''Warns a message (``msg``).'''
    print(YELLOW + "[JX]: " + msg)

def error(msg: str) -> None:
    '''Shows an error of content ``msg``.'''
    print(RED + "[JX]: " + msg)

def accountExists(id: str) -> bool:
    '''Returns True if an account with the user's id exists.'''
    with open(JSON_PATH, mode="r") as f: return str(id) in json.load(f)

def createAccount(id: str, signupBonus: float=0) -> bool:
    '''Creates an account given a user's ID. Returns False if account is found, True if creation successful.'''
    user = {
        "date-created": str(datetime.datetime.now().date()),
        "time-created": str(datetime.datetime.now().time()),
        "sc": signupBonus,
    }

    db = getDB()
    db[id] = user

    if not accountExists(id):
        setDB(db)
        return True
    return False

def deleteAccount(id: str) -> bool:
    '''Deletes an account given a user's ID. Returns False if account not found, True if deletion successful.'''
    db = getDB()
    if accountExists(id):
        del db[str(id)]
        setDB(db)
        return True
    else:
        return False

def getDB() -> dict:
    '''Returns JSON database.'''
    with open(JSON_PATH, mode="r") as f: return json.load(f)

def setDB(db: dict) -> None:
    '''Sets the current database to ``db``.'''
    with open(JSON_PATH, mode="w") as f: f.write(json.dumps(db, indent=4))

def getUser(id: str) -> dict:
    '''Returns the user, if they exist. None otherwise.'''
    db = getDB()
    if accountExists(id):
        return db[str(id)]
    return None

def setUser(id: str, user: dict) -> None:
    '''Saves a user to the database.'''
    db = getDB()
    if accountExists(id):
        db[str(id)] = user
        setDB(db)

def getUserAttribute(id: str, attr: str):
    '''Returns the user's attribute value if it exists, None otherwise.'''
    try:
        user = getUser(id)
        if attr in user:
            return user[attr]
        return None
    except Exception as e:
        return None

def setUserAttribute(id: str, attr: str, value: Any) -> None:
    user = getUser(id)
    if user:
        user[attr] = value
        setUser(id, user)
