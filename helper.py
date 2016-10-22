

# from pyzipcode import ZipCodeDatabase
import bs4
# import urllib2
from bs4 import BeautifulSoup
# from model import connect_to_db, db, School
from xml.dom.minidom import parse, parseString
import requests
import os
# from model import Images
# from states import get_state_full_name

# API_KEY_GS = os.environ.get("api_key_gs")
# API_KEY_NUMBEO = os.environ.get("API_KEY_NUMBEO")



def row2dict(row):
    dictionary = {}
    for column in row.__table__.columns:
        dictionary[column.name] = str(getattr(row, column.name))

    return dictionary


def hash_password(password):
    import hashlib
    hash1 = hashlib.md5(password)
    hashed = hash1.hexdigest()
    return hashed














