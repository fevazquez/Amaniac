import requests
import discord
import json
import random
from replit import db

def get_quote():
  response = requests.get("https://complimentr.com/api")
  json_data = json.loads(response.text)
  quote = json_data['compliment']
  return(quote)


def print_db(key):
  if key in db:
    for i in db[key]:
      print(i)
  else:
    print("The key: " + key + " is not in the database!")