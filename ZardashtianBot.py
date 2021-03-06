# Imports #

import discord
import random
import asyncio
import logging
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import when_mentioned_or
from discord.utils import get
import platform
import time
import datetime
import texttable
import wolframalpha
import copy
import json
import os
import requests
from discord.utils import find
from cleverwrap import CleverWrap
import aiohttp
import psutil
from discord.ext.commands.cooldowns import BucketType
import humanize
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

BOT_TOKEN = ("NDY0ODI2NzM3MTg5MDYwNjA4.XU6dyw.vxc8aawUIzx7Uz-9IhGyBo3b_6c")

# Prefixes #

bot = commands.Bot(command_prefix="Z-", status=discord.Status.idle, activity=discord.Game(name="Loading..."), case_insensitive=True)

client = commands.Bot

client = discord.Client()

client = commands.Bot(command_prefix='Z-')

# Variables #

#	#	# Fun! #	#	#

# Beta CMDS #

@client.event
async def on_message(message):
    if message.content.startswith('!bitcoin'):
      price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate']
      await client.send_message(message.channel, "Bitcoin is $" + price)
      await client.send_message(message.channel, "HODL HODL")
    if "repl.it" in message.content:
      await client.send_message(message.channel, slogan[randint(0,len(slogan) - 1)])
    if message.content.startswith('!dadjoke'):
      joke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).text
      await client.send_message(message.channel, joke)
    if message.content.startswith('!random'):
      await client.send_message(message.channel, 'You rolled a ' + str(randint(1,6)))
    if message.content.startswith('!xkcd'):
      await client.send_message(message.channel, 'get ready to laugh... or something')
      latest = requests.get('https://xkcd.com/info.0.json').json()
      num = randint(1, latest['num'])
      comic = requests.get('https://xkcd.com/' + str(num) + '/info.0.json').json()
      await client.send_message(message.channel, comic['img'])
      await client.send_message(message.channel, '_' + comic['alt'] + '_')
      
    if message.content.startswith('!quote'):
      await client.send_message(message.channel, 'thinking...')
      r = requests.get('https://talaikis.com/api/quotes/random/')
      q = r.json()
      await client.send_message(message.channel, q['quote'] + ' -- ' + q['author'])
      
    if message.content.startswith('!gif '):
      await client.send_message(message.channel, 'researching')
      tag = message.content[5:]
      r = requests.get('http://api.giphy.com/v1/gifs/search?q=' + tag + '&api_key=hCKgiae5XgjiYbKPTdgrSuh8P7l2xWMT')
      q = r.json()
      await client.send_message(message.channel, q['data'][0]['url'])
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

# Creeper CMD #

@client.command()
async def creeper(ctx):
    await ctx.send('aww man')

# 8ball #

@client.command(name='8ball',
                description="Answers a stoopid and pointless question.",
                brief="Answers from Ur Mum.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx, context):
    possible_responses = [
        'That is a resounding no you idot',
        'It is not looking good (like me!)',
        'That question is too hard!',
        'It is quite possible :thinking: ',
        'Definitely (Not!)',
    ]
    await ctx.send(random.choice(possible_responses) + ", " + context.message.author.mention)
    
# Math  add #

@client.command()
async def add(ctx, left : int, right : int):
    """Adds Two Numbers."""
    await ctx.send(left + right)

# Math Subtraction #

@client.command()
async def subtract(ctx, left : int, right : int):
	"""Subtracts Two Numbers."""
	await ctx.send(left - right)

# Math Multiplication #

@client.command()
async def multiply(ctx, left : int, right : int):
	"""Multiplies Numbers."""
	await ctx.send(left * right)

# Math Division #

@client.command()
async def divide(ctx, left : int, right : int):
	"""Divides Numbers!"""
	try:
	        await ctx.send(left // right)
	except ZeroDivisionError:
		await client.send("You cannot divide by 0! :thinking:")
        
# Ping #

@client.command()
async def ping(ctx):
    """Pings the bot."""
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000 / 2)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

# Shoot Command #

@client.command(name='shoot',
                description="Shoot an enemy!",
                brief="Shoot your enemies....",
                pass_context=True)
async def shoot(ctx, context, target: discord.Member):
    possible_responses = [
        'You missed your shot!',
        'Uh oh! The fuzz have arrived!',
        'You hit! ' + target.mention,
        'Your enemy ' + target.mention + ' dies a bloody death!',
        'Ew, blood!',
    ]
    await ctx.send(random.choice(possible_responses) + ", " + context.message.author.mention);

# Stab Command #

@client.command(name='stab',
                description="Stab an enemy!",
                brief="Stab your enemies....",
                pass_context=True)
async def stab(ctx, context, target: discord.Member):
    possible_responses = [
        'You spill their guts!',
        'Oh no, the Po-Po!',
        'You stab! ' + target.mention,
        'Your enemy ' + target.mention + ' dies a bloody death! (Lots of blood and guts)',
        'Ew, blood!',
    ]
    await ctx.send(random.choice(possible_responses) + ", " + context.message.author.mention);

# Info CMD #

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Zardashtian Bot", description="New,Noice and very easy to use.", color=0xeee657)

    # give info about you here #
    embed.add_field(name="Author", value="@GreatZardasht#4218")

    # Shows the number of servers the bot is member of. #
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite this bot to their server #
    embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?client_id=464826737189060608&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FuYSydfN&scope=bot")

    # Shows the number of servers the bot is member of. #
    embed.add_field(name="Latest Changelog", value="updated ban and unban and turned everycmd starting to a small letter no caps needed after Z- now")

    await ctx.send(embed=embed)

# Status Message #

@client.event
async def on_ready():
    print('The bot is ready!')
    print('Logged in as')
    print(client.user.name)
    print('Why Is Asyncio Bullying Us')
    	
# # # Owner Only Cmds # # #

# Status Changer Cmd #

@client.command()
@commands.is_owner()
async def statusc(self,ctx,*args):
    if len(args) != 0:
        acttype = 0
        if args[0] == "!watching":
            acttype = 3
            args = args[1:]
        act = discord.Activity(name=" ".join(args),type=acttype)
        await self.bot.change_presence(activity=act)

# # # Moderation # # #

# purge #

@client.command ( )
async def clear(ctx, amount=100) :
    """clears spam/messages to make space"""
    await ctx.channel.purge (limit=amount)

# Support Us #

@client.command()
async def support(ctx):
         """Support us for better things"""
         await ctx.send("Join Us Here chat with our friendly staff https://discord.gg/uYSydfN")

# Ban Command #

@client.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    """Bans specified user"""
    dm = discord.Embed(title="You have been banned from a certain guild!", color=0xFF0000)
    dm.add_field(name="Moderator:",
                    value=ctx.message.author.display_name)
    dm.add_field(name="Reason:", value=f"{reason}")
    dm.set_thumbnail(url=member.avatar_url)
    await member.send(embed=dm)  # Send DM
    await member.ban(reason=reason)  # Ban
    await ctx.message.delete()  # Delete The Message
    await ctx.send('member has been banned.')

# Kick Command #

@client.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def kick(ctx, member: discord.Member, *, reason='No reason provided.'):
    """Kicks specified user"""
    dm = discord.Embed(title="You have been kicked from a certain guild!", color=0xFF0000)
    dm.set_thumbnail(url=member.avatar_url)
    dm.add_field(name="Reason:", value=f"{reason}")
    dm.add_field(name="Moderator:",
                    value=ctx.message.author.display_name)
    await member.send(embed=dm)  # Send DM
    await member.kick(reason=reason)  # Kick
    await ctx.message.delete()  # Delete The Message
    await ctx.send('member has been kicked.')

# Unban Command #

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
@commands.bot_has_permissions(administrator=True)
async def unban(ctx, userName: discord.User):
    """Unban a user ( Oh Snap Here We Go Again)"""
    await client.unban(userName)
    await ctx.send("Successful!")

client.run(BOT_TOKEN)
