#Create a bot from https://discord.com/developers/applications
#Open your bot's Server Member and Message Content intents
#Add your bot to your server from https://discordapi.com/permissions.html

import discord
from discord.ext import commands
from ayarlar import *
from functions import *

intents = discord.Intents().all()
intents.message_content = True
Bot = commands.Bot(command_prefix='YOUR_BOTS_PREFIX', intents=intents)

#READY
@Bot.event
async def on_ready():
    print("Bot is ready")

#HELP
@Bot.command()
async def help(ctx, *args):
    if "commands" in args:
        await ctx.send("Your Command List")
    else:
        await ctx.send("Help For Your Bot") 

#HELLO
@Bot.command()
async def hello(ctx):
    await ctx.send("Hi")

Bot.run("YOUR_BOT'S_TOKEN")
