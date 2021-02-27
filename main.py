import traceback
import discord,os
from discord.ext import commands,tasks
import urllib.request
import asyncio


intents = discord.Intents.default()
client = commands.Bot(command_prefix = '+', intents = intents)
client.remove_command('help')

token = 'ODIzOTY2OTM5NzAwNTI3MTU0.YFohAg.C-8aMyxws1WsOhSW9UovTbkedhY'

@client.event
async def on_ready():
    tv = discord.Activity(type=discord.ActivityType.watching, name=f'Your Cockpit')
    await client.change_presence(status=discord.Status.online, activity=tv)
    os.system('title Bedouin Discord Bot --LOGS')
    os.system('color 0a')
    print("Bot Initialized!.")

@client.command()
async def post(ctx, channel : discord.TextChannel, *, args):

    argus = args.split('////')
    embed = discord.Embed(
        colour = discord.Colour.gold()
        )
    title = argus[1].replace("////","").strip()
    subtitle = argus[2].replace("////","").strip()
    content = argus[3].replace("////","").strip()
    if "--nofooter" in args:
        pass
    else:
        footrr = argus[4].replace("////","").strip()
        embed.set_footer(text=footrr)
    if "--nothumb" in args:
        pass
    else:
        thumb = argus[5].replace("////","").strip()
        embed.set_thumbnail(url = thumb)
    embed.set_author(name=title)
    embed.add_field(name=subtitle, value=content)
    await channel.send(embed=embed)

@client.command()
async def pic(ctx, channel : discord.TextChannel, *, msg):
    await channel.send(msg)

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

client.run(token)