import os
import asyncpraw
import discord
import requests
import json
import random
import time
import datetime
from pytz import timezone
from replit import db
from Bot.constants import *
from Bot.keep_alive import *
from Bot.helper import *

client = discord.Client()

reddit = asyncpraw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    user_agent = "pythonpraw",
)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  print_db("requests")


@client.event
async def on_message(message):

  #  If message is a Bot/non-prefixed ignore it, else split into single "command" & array of args.
  if message.author == client.user or not message.content.startswith('>'):
    return

  channel = message.channel
  command = message.content.split()[0].lower()[1:]
  args = [i.lower() for i in message.content.split() if not i.startswith('>')]

  # Send function makes it so we write less repetitive code.
  async def send(msg):
      await channel.send(msg)

  if command not in commands:
    await send("type >help to see my commands")
    return

  # Ver: Displays the latest version number along with the latest patch note
  if command == 'ver':
    patch_notes = ['This is my current version: 1.0', '1.0: The full release of the Amaniac Bot!'];
    for i in patch_notes:
      await send(i)
  
  # Help: Provides the Users with documentation on all the commands the bot
  # can do specific help on certain commands. 
  if command == 'help':
    await send("check your dms ;)")
    await message.author.send(help) 

  if command == 'hoes':
    await send("Where the hoes at?")

  if command == 'tonster12':
    await send(images["tonster12"])
  
  if command == 'quote':
    await send(random.choice(emojis) + "\t" +get_quote())

  if command == 'f' or command == 'respects':
    emoji = "🟥"

    temp = ""
    for i in range(5):
      temp += emoji + "\t"
    await send(temp)
    temp = ""
    await send(emoji)
    for i in range(5):
      temp += emoji + "\t"
    await send(temp)
    for i in range(3):
      await send(emoji)
  
  # Wednesday: If it is Wednesday, post "the" vine, else post it's not Wed.
  if command == 'wednesday' or command == 'wed':
    date = datetime.datetime.now() 
    date = date.astimezone(timezone('US/Pacific'))
    
    # it is wednesday
    if date.isoweekday() == 3:
      await send("It IS Wednesday my doods.")
      await send(images["wednesday"])
    elif date.isoweekday() == 4:
      await send(images["late_wed"])
    else:
      await send("It is NOT Wednesday my doods.")

  # Races: Sends the dnd races song video
  if command == 'races':
    await send(images["races"])
    await send(videos["races"])

  # dnd: Sends the crap guide of the asked class
  if command == 'dnd':
    for i in args:
      i = i.lower()
      if i == 'barb':
        await send(videos['barbarian'])
      elif i == 'wiz':
        await send(videos['wizard'])
      elif i == 'war':
        await send(videos['warlock'])
      elif i == 'pal':
        await send(videos['paladin'])
      elif i == 'sorc':
        await send(videos['sorcerer'])
      elif i == 'art':
        await send(videos['artificer'])
      elif i in videos:
        await send(videos[i])
      else:
        await send("I dont know that class!")
    
  # Cory: Sends Cory in the house anime intro
  if command == 'cory' or command == 'kory':
    await send(videos["cory"])

  # 4loko: Sends 4loko 
  if command == '4loko':
    await send("you have been four lokoed!!")
    await send(images["loko" + str(random.randint(1, 9))])
    await send(videos["4loko"])

  # Pablo: Sends an image of Pablo!
  if command == 'pablo':
    await send(images["pablo"+str(random.randint(1, 4))])

  # Suprise: Sends random picture from the group/individual
  if command == 'surprise':
    target = random.randint(1, 4)

    if target == 1:
      await send(images["colin"+str(random.randint(1, 2))])
    elif target == 2:
      await send(images["warren"+str(random.randint(1, 3))])
    elif target == 3:
      await send(images["paul"])
    else:
      await send(images["group"+str(random.randint(1, 8))])

  # Meme: Sends random meme from the dndmemes subreddit
  if command == 'meme':
    subreddit = await reddit.subreddit("dndmemes")
    hot = subreddit.hot(limit=50)
    subs = []

    async for submission in hot:
      subs.append(submission)

    random_sub = random.choice(subs)
    
    await send(random_sub.url)
  
  # Shots: time to take shots!
  if command == 'shots':
    await send("get ready to TAKE SHOTS!")
    
    for i in reversed(range(1, 11)):
      await send(i)
      time.sleep(1)
      
    await send(images["shots"])
    time.sleep(2)
    await send(images["party_parrots"])
    

  # Role: role any number of x-sided dice
  # EX: 2d20 = 2 - 20 sided dice
  if command == "role":
    for i in args:
      num = int(i.split('d')[0])
      max = int(i.split('d')[1])

      for j in range(num):
        await send(random.randint(1, max))
    
    
  # Ban: bans paul
  if command == 'ban':
    name = args[0]
    if name == "paul" and "counter" in db.keys():
      db["counter"] = str(int(db["counter"]) + 1);
      await send(name + " has been banned. He has been banned " + db["counter"] + " times!")
    elif name == "paul":
      db["counter"] = "1";
      await send(name + " has been banned.")
    else:
      await send(name + " can't be banned. Only paul is allowed to be banned!")

  # Request: I store requested commands to learn!
  if command == 'request':
    if len(args) > 1:
      com = args[0]
      details = args[1]
      
      if "requests" in db.keys():
        if any(i for i in db["requests"] if com == i[0]):
          await send("I am already considering the " + com + " command!")
          return
            
        db["requests"].append((com, details))

      else:
        db["requests"] = [(com, details)]

      await send("I will make note of that! Oh yes I will I will I will!!!!")
      
    else:
      await send("I need more information! Tell me your requested command in more detail!")
      await send("Oh tell me tell me tell me!")
      await send("format: >request [command name] [details]")

    
keep_alive()
client.run(os.environ['TOKEN'])
