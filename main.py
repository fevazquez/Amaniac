import os
import asyncpraw
import datetime
import random 
import time
import discord
import asyncio

from pytz import timezone
from replit import db
from discord.ext import commands
from enum import Enum
from Bot.constants import *
from Bot.keep_alive import *
from Bot.helper import *

Gods = Enum('Gods', 'tonster12 pablo')
bot = commands.Bot(command_prefix='>', case_insensitive=True)
reddit = asyncpraw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    user_agent = "pythonpraw",
)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  print_db("requests")
  #print_db("proof")


@bot.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
      f'Hi {member.name}, you just made the worst decision of your life joining this server!'
  )
  

@bot.command(
  help="I send the latest version and patch notes",
	brief="Developer information",
  aliases=['ver']
)
async def version(ctx):
  for i in patch_notes:
    await ctx.send(i)


@bot.command(
  help="Sends the crap guide to dnd races video, aka the best music video ever!",
	brief="Sends the races video to the channel."
)
async def races(ctx):
  await ctx.send(images["races"])
  await ctx.send(videos["races"])

  
@bot.command(
  help="Im looking for them, let me know where they at tho",
	brief="Where the hoes at?",
  aliases=['woes']
)
async def hoes(ctx):
  await ctx.send("Where the hoes at?")
  await ctx.send(images["hoes"])


@bot.command(
  help="I call upon one of the gods! The one and only Tonster12 or The infamous Pablo will respond your call...",
  brief="get a visit from one of the gods...",
  alias=['worship']
)
async def pray(ctx):
  roll = random.randint(1, 3)
  await ctx.send("Sending your prayers....")
  time.sleep(2)

  if roll < 3:
    await ctx.send("Looks like a God is hearing your prayers! BEHOLD THE PRESENCE OF GOD!")

  if roll == Gods.tonster12.value:
    await ctx.send(images["tonster12"])
  elif roll == Gods.pablo.value:
    await ctx.send(images["pablo"+str(random.randint(1, 4))])
  else:
    await ctx.send("No God has answered your prayers... You are not worthy!")
  

@bot.command(
  help="I compliment you or a user you tag <3",
  brief="come and find out...",
  aliases=['tell', 'comp']
)
async def compliment(ctx, user: discord.User):
  await ctx.send(user.mention + "\t" + random.choice(emojis) + "\t" +get_quote())

@compliment.error
async def compliment_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(random.choice(emojis) + "\t" +get_quote())
    

@bot.command(
  help="I let you know if it is wednesday, my dudes",
	brief="Is it Wednesday?",
  aliases=['wed']
)
async def wednesday(ctx):
  date = datetime.datetime.now() 
  date = date.astimezone(timezone('US/Pacific'))
  
  # it is wednesday
  if date.isoweekday() == 3:
    await ctx.send("It IS Wednesday my doods.")
    await ctx.send(images["wednesday"])
  # it is thursday
  elif date.isoweekday() == 4:
    await ctx.send(images["late_wed"])
  # every other day
  else:
    await ctx.send("It is NOT Wednesday my doods.")


@bot.command(
  help="We ban Paul from the server! I will display the amount of times he has been banned",
	brief="Ban Paul"
)
async def ban(ctx, name):
  if name == "paul" and "counter" in db.keys():
    db["counter"] = str(int(db["counter"]) + 1);
    await ctx.send(name + " has been banned. He has been banned " + db["counter"] + " times!")
  elif name == "paul":
    db["counter"] = "1";
    await ctx.send(name + " has been banned.")
  else:
    await ctx.send(name + " can't be banned. Only paul is allowed to be banned!")

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Who are you trying to ban? Please tell me tell me tell me!')


@bot.command(
  help="I pick and send a random meme from the dndmemes subreddit",
	brief="I send dnd Meme"
)
async def meme(ctx):
  subreddit = await reddit.subreddit("dndmemes")
  hot = subreddit.hot(limit=50)
  subs = []

  async for submission in hot:
    subs.append(submission)

  random_sub = random.choice(subs)
  await ctx.send(random_sub.url)


@bot.command(
  help="I role any number of x sided dice", 
  brief="I role dice!"
)
async def roll(ctx, *args):
  # Role: role any number of x-sided dice
  # EX: 2d20 = 2 - 20 sided dice
  
  if len(args) < 1:
    await ctx.send("I need to know how many dice you want to roll!")
    return 
    
  for i in args:
    num = int(i.split('d')[0])
    max = int(i.split('d')[1])

    for j in range(num):
      await ctx.send(random.randint(1, max))
        
@roll.error
async def roll_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("What kind of dice are you trying to roll? Tell me tell me tell me!")
  if isinstance(error, commands.BadArgument):
    await ctx.send("Thats a strange dice you are having me roll! Thats beyond my power!")


@bot.command(
  help="I count down from 10, at the end everyone drinking must take a shot!",
  brief="Shots o clock!"
)
async def shots(ctx):
  await ctx.send("get ready to TAKE SHOTS!")
  
  for i in reversed(range(1, 11)):
    await ctx.send(i)
    time.sleep(1)
    
  await ctx.send(images["shots"])
  time.sleep(2)
  await ctx.send(images["party_parrots"])


@bot.command(
  help="A user gets 4lokoed!",
  brief="4loko someone",
  aliases=['4loko']
)
async def floko(ctx, user: discord.User):
    await ctx.send(user.mention + " has been four lokoed!!")
    await ctx.send(images["loko" + str(random.randint(1, 9))])
    await ctx.send(videos["4loko"])

@floko.error
async def floko_error(ctx, error):
  if isinstance(error, commands.BadArgument): 
    await ctx.send('Im not sure who you are trying to 4loko... Tell me tell me tell me!')

  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('You 4lokoed yourself!')
    await floko(ctx, ctx.author)

@bot.command(
  help="Callout someone for game of life! They target must provide proof within a minute!",
  brief="Call game of life on a player that is drinking",
  aliases=['gol']
)
async def gameoflife(ctx, user: discord.User):
  await ctx.send(ctx.author.mention + " calls game of life on " + user.mention + "‼️")
  await ctx.send(user.name + " has 1 minute to provide proof or has to down their drink!")

  if "proof" in db.keys():
    db["proof"][user.name] = False
  else:
    db["proof"] = { user.name : False }

  await asyncio.sleep(60)
  
  if db["proof"][user.name]:
    await ctx.send(ctx.author.mention + " looks like you fucked up! NOW DOWN YOUR DRINK!")
  else:
    await ctx.send(user.mention + " looks like you didnt provide proof... NOW DOWN YOUR DRINK!")
  
@gameoflife.error
async def gameoflife_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("You didnt tell me who to challenge! Oh tell me tell me tell me!")


@bot.command(
  help="I send the crap guide to dnd video of the provided class!",
  brief="Want some information on the provided dnd class?"
)
async def dnd(ctx, *args):
  if len(args) < 1:
    await ctx.send("I need to know what class to look for!")
    return 
    
  for i in args:
    i = i.lower()
    if i == 'barb':
      await ctx.send(videos['barbarian'])
    elif i == 'wiz':
      await ctx.send(videos['wizard'])
    elif i == 'war':
      await ctx.send(videos['warlock'])
    elif i == 'pal':
      await ctx.send(videos['paladin'])
    elif i == 'sorc':
      await ctx.send(videos['sorcerer'])
    elif i == 'art':
      await ctx.send(videos['artificer'])
    elif i in videos:
      await ctx.send(videos[i])
    else:
      await ctx.send("I dont know that class!")

@dnd.error
async def dnd_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send('I could not find that class...')
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You didnt tell me a class! Oh tell me tell me tell me!")


@bot.command(
  help="I send a giant f to pay respects composed of random emojis",
  brief="Press f to send respects",
  alias=['f']
)
async def respect(ctx):
  emoji = "🟥"
  temp = ""
  for i in range(5):
    temp += emoji + "\t"
    
  await ctx.send(temp)
  temp = ""
  await ctx.send(emoji)
  for i in range(5):
    temp += emoji + "\t"
    
  await ctx.send(temp)
  for i in range(3):
    await ctx.send(emoji)
    
  
@bot.command(
  help="I send a random picture of the crew!",
  brief="A surprise awaits!",
  aliases=['surp']
)
async def surprise(ctx):
  # Suprise: Sends random picture from the group/individual
  target = random.randint(1, 4)

  if target == 1:
    await ctx.send(images["colin"+str(random.randint(1, 2))])
  elif target == 2:
    await ctx.send(images["warren"+str(random.randint(1, 3))])
  elif target == 3:
    await ctx.send(images["paul"])
  else:
    await ctx.send(images["group"+str(random.randint(1, 8))])


@bot.command(
  help="I store requested commands to learn! I will consider said command oh yes I will I will I will!",
	brief="Want me to learn a command?",
  aliases=['req']
)
async def request(ctx, *args):
  # Request: I store requested commands to learn!
  if len(args) > 1:
    com = args[0]

    # append all the details into a single streing to store
    details = ""
    for i in args[1:]: 
      details += i + " "
    
    if "requests" in db.keys():
      if any(i for i in db["requests"] if com == i[0]):
        await ctx.send("I am already considering the " + com + " command!")
        return
          
      db["requests"].append([com, details])

    else:
      db["requests"] = [[com, details]]

    await ctx.send("I will make note of that! Oh yes I will I will I will!!!!")
    
  else:
    await ctx.send("I need more information! Tell me your requested command in more detail!")

@request.error
async def request_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send('I cant understand this command!')
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I need more information! Tell me your requested command in more detail!")
      await ctx.send("Oh tell me tell me tell me!")
      await ctx.send("format: >request [command name] [details]")


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("Looks like I dont know that command!")
    await ctx.send("Type >help to get a list of my commands")
    await ctx.send("Or do you want me to learn this command? Oh yes I take feedback oh yes oh yes oh yes!")
    await ctx.send("Type >help request for more information!")


@bot.event
async def on_message(message):

  #  If message is a Bot/non-prefixed ignore it
  if message.author == bot.user:
    return
    
  # check for the game of life command
  name = message.author.name
  if len(message.attachments) > 0 and "proof" in db.keys() and name in db["proof"]:
    db["proof"][name] = True

  await bot.process_commands(message)
    
  # Help: Provides the Users with documentation on all the commands the bot
  # can do specific help on certain commands. 
  # if command == 'help':
  #   await send("check your dms ;)")
  #   await message.author.send(help) 
  
  # # Cory: Sends Cory in the house anime intro
  # if command == 'cory' or command == 'kory':
  #   await send(videos["cory"])


keep_alive()
bot.run(os.environ['TOKEN'])
