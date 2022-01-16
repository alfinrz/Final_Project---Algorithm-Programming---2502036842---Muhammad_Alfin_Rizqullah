import random
from discord.ext import commands #this is dicord.py a popular module for discord bot that has been discontinued
from GIF import TENOR_CLIENT 

#API token, stored in different file for security reasons
def get_tenor_token(): 
    with open("C:\\Users\\alfin\\Documents\\Discord_Bot\\Final\\gif.txt", "r") as c: #Due to issues with Windows that required the absolute path of the file, and double backslash
        lines = c.readlines()
        token = lines[0].strip()
    return token

def get_discord_token():
    with open("Token.txt", "r") as f: #For some reason this specific file didn't need the absolute path like above
        lines = f.readlines()
        token = lines[0].strip()
    return token

TENOR_TOKEN = get_tenor_token() #this is required in order to gain access to the Tenor api
DISCORD_TOKEN = get_discord_token() #this is required in order to gain access to the Discord api
Tenor_client = TENOR_CLIENT(TENOR_TOKEN) #this will create a Tenor_client object in order to be able to use in this file

#this will be the prefix that is used to interact with .commands code
client = commands.Bot(command_prefix='/')

#.event will iniate the code providing every condition is met
@client.event
async def on_ready():
    print("BOT is Online")

#discord.py uses async instead of normal sync in order to keep going even if a process is going to take time 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #this will detect wheter the text is an invite link to the games Bloons TD 6
    if  "https://" in message.content and "coop" in message.content or "boss" in message.content:
        bloons_code = message.content[-6:] 
        await message.channel.send(bloons_code)
        await message.channel.send(Tenor_client.get_random_bloons())
    await client.process_commands(message)

#.command will only iniate if the prefix is entered before the specific command

#this specific command will help the user in knowing what commands this bot contain
@client.command()
async def use(ctx): #async def is a requirement in discord.py for function
    await ctx.send("/bloons") 
    await ctx.send("/hello")
    await ctx.send("/gog")
    await ctx.send("/playbloons")

#will simply reply with "Hello!" when prompt
@client.command()
async def hello(ctx):
    await ctx.reply('Hello!')

#when called it would simply reply accordingly 
@client.command()
async def playbloons(ctx):
    await ctx.reply('Lets play Bloons TD 6')

#if the user simply want a randomize gif of bloons, they can simply call on this command
@client.command()
async def bloons(ctx):
    await ctx.send(Tenor_client.get_random_bloons())

#if the user want a randomize gif of gog, simply call this command
@client.command()
async def gog(ctx):
    await ctx.send(Tenor_client.get_random_gog())

#this is required in order for the bot to start
@client.command()
async def vote(ctx):
    x = ["yes", "no"]
    await ctx.reply(random.choice(x))

client.run(DISCORD_TOKEN)