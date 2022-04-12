'''
This file contains the constants that the main bot code uses. This includes all the commands available, image urls, helper output strings, and any variables that hold commonly used data.
'''

commands = ["ver", "f", "respects", "ban", "quote", "wednesday", "wed", "meme", "tonster12", "races", "hoes", "role", "shots", "help", "cory", "kory", "4loko", "pablo", "surprise", "dnd", "request"]

help = '''
I am Amaniac bot 🤪

Please! tell me your commands! tell me tell me tell me tell me!  

  # developer stuff
  >ver - I tell you my latest version and patch notes

  # anything dnd 
  >dnd [class] - I send the crap guide of the given class
  >role [x dice]d[y sided] - I role any number of y sided dice
  >meme - dndmemes subreddit random meme

  # other 
  >ban [name] - Ban paul
  >hoes  - where they at?
  >f/respects - I send a giant F
  >gameoflife [user] - Calls out user for game of life. If attempt fails, then YOU down your drink # TODO 

  >cory/kory - cory in the house theme
  >4loko - get 4lokoed
  >pablo - sends a picture of the legend
  >surprise - sends a surprise group picture

  >quote - I send you a cute message (:
  >wednesday - It is wednesday my dudes
  >shots - I countdown from 10 to have everyone take a shot
  >tonster12 - the god himself 

  >request [command] [description] - I store the requested command and the given description for me to learn!
'''

emojis = [
  "😘",
  "😍",
  "🥰",
  "😋",
  "😄",
  "😚",
  "🤗",
  "😏",
  "😳",
  "🥵",
  "🤩",
  "😁",
  "😄",
]

images = {
  "wednesday": "https://www.youtube.com/watch?v=du-TY1GUFGk",
  "pablo1": "https://cdn.discordapp.com/attachments/613090999002071105/736050600877228052/IMG_4552.JPG",
  "pablo2": "https://cdn.discordapp.com/attachments/613090999002071105/613124209962516659/fc2ad509-4b1d-469e-a639-37ad6369a6c2.jpg",
  "pablo3": "https://cdn.discordapp.com/attachments/613090999002071105/613124076797689875/c28f8635-006e-415e-b544-c717bc647923.jpg",
  "pablo4": "https://cdn.discordapp.com/attachments/613090999002071105/613123349639331915/20181218_151656.jpg",
  "colin1": "https://cdn.discordapp.com/attachments/613090999002071105/613139269858623530/20150425_095627.jpg",
  "colin2": "https://cdn.discordapp.com/attachments/613090999002071105/613137620909948958/image0-25.jpg",
  "warren1": "https://cdn.discordapp.com/attachments/613090999002071105/613125443436150796/20181116_175833.jpg",
  "warren2": "https://cdn.discordapp.com/attachments/613090999002071105/613125443436150796/20181116_175833.jpg",
  "warren3": "https://cdn.discordapp.com/attachments/924742421751939101/961758896232484875/warrenlol.jpg",
  "paul": "https://cdn.discordapp.com/attachments/613090999002071105/627345785176064000/20190927_202606.jpg",
  "group1": "https://cdn.discordapp.com/attachments/613090999002071105/670539570550538240/20190328_191436.jpg",
  "group2": "https://cdn.discordapp.com/attachments/613090999002071105/614164325808209951/20150515_193501.jpg",
  "group3": "https://cdn.discordapp.com/attachments/613090999002071105/613129588398096384/IMG_20181026_223748_347.jpg",
  "group4": "https://cdn.discordapp.com/attachments/613090999002071105/613129210717929628/FB_IMG_1566251783918.jpg",
  "group5": "https://cdn.discordapp.com/attachments/613090999002071105/613127491149627413/0319161210.jpg",
  "group6": "https://cdn.discordapp.com/attachments/613090999002071105/613126923366957061/20181021_130844.jpg",
  "group7": "https://cdn.discordapp.com/attachments/613090999002071105/613123731208011776/20181021_141210.jpg",
  "group8": "https://cdn.discordapp.com/attachments/613090999002071105/613123618901065760/20180802_112604.jpg",
  "late_wed": "https://cdn.discordapp.com/attachments/547862983515308040/550771383978688514/uc1w4xzevwh21.jpg",
  "tonster12": "https://lh3.googleusercontent.com/pw/AM-JKLUEvjXidWDcGEbE3sj4fx0VM3KKM7wJqdXkbtKprTpsfv2u_iqm8XxkGybhsu_A_4WsmdkAu4woaqQQm6BwbKfBBowEcD6Jj9DQ6WWZfc1Mk07KTKpGL2BKo5jq3O-5OhGr0EWka3chmdPPbNpZIWY=s166-no?authuser=0",
  "races": "https://c.tenor.com/74rJWp3L16MAAAAC/crap-guide-dnd-crap-guide.gif",
  "shots": "https://res.cloudinary.com/wnotw/images/c_limit,w_1536,q_auto:good,f_auto/v1556554629/d1upwusr26nt5nchhiln/giphy-stickers-for-instagram-stories",
  "party_parrots": "https://acegif.com/wp-content/uploads/2020/b72nv6/partyparrt-4.gif",
  "loko1": "https://four-loko.imgix.net/products/el_lem_14.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko2": "https://four-loko.imgix.net/products/red_14.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko3": "https://four-loko.imgix.net/products/red_14.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko4": "https://four-loko.imgix.net/products/gold_14.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko5": "https://four-loko.imgix.net/products/fruitpunch_14.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko6": "https://four-loko.imgix.net/products/watermelon_14.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko7": "https://four-loko.imgix.net/products/peach_14.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko8": "https://four-loko.imgix.net/products/strawlem_12.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
  "loko9": "https://four-loko.imgix.net/products/grape_12.19.png?auto=format&ch=DPR&fit=crop&ixlib=php-1.1.0&w=320",
}

videos = {
  "cory": "https://www.youtube.com/watch?v=OkZtcNavwOY",
  "races": "https://www.youtube.com/watch?v=DBoqrSn1GR8",
  "4loko": "https://www.youtube.com/watch?v=y2cFkVfVf2Y",
  "artificer": "https://www.youtube.com/watch?v=tV7X76FKkeI",
  "barbarian": "https://www.youtube.com/watch?v=00EvO-X6Wu4",
  "bard": "https://www.youtube.com/watch?v=qiHXxrCB5yk",
  "cleric": "https://www.youtube.com/watch?v=y84OYRwzZU8",
  "druid": "https://www.youtube.com/watch?v=WMo_gCRMSfA",
  "fighter": "https://www.youtube.com/watch?v=nVReBH3QYD0",
  "monk": "https://www.youtube.com/watch?v=1CZDGFFHnI4",
  "paladin": "https://www.youtube.com/watch?v=Ch5vWBPCrl0",
  "ranger": "https://www.youtube.com/watch?v=P_qzyTFSrTE",
  "rogue": "https://www.youtube.com/watch?v=4FX_2UevHbE",
  "sorcerer": "https://www.youtube.com/watch?v=EHJGJL40cQs",
  "warlock": "https://www.youtube.com/watch?v=9mvTgXPHlvo",
  "wizard": "https://www.youtube.com/watch?v=U1Gs8WTddI4"
}