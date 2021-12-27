import discord
from discord.ext import commands
import random
from gif import GIF
import time
# from Reminder import reminder

def read_token():
    with open("Token.txt", "r") as f:
        lines = f.readlines()
        token = lines[0].strip()
    return token

deadline = []
       
client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print("BOT is Online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Join"):
        await message.channel.send(random.choice(GIF.bloons_gif()))
    await client.process_commands(message)

@client.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@client.command()
async def bloons(ctx):
    await ctx.reply('Lets play Bloons TD 6')
    
@client.command()
async def wordlenght(ctx, *arg):
    await ctx.send("Word Count is: {}".format(len(arg), ",".join(arg)))

@client.command()
async def lettercount(ctx, *, arg):
    await ctx.send('{} arguments: {}'.format(len(arg), ', '.join(arg)))

@client.command()
async def reminder(ctx, *, arg):
    await ctx.send("List has been added")
    deadline.append()

TOKEN = read_token()

client.run(TOKEN)
