# Imports #

import discord
import random
import asyncio
import logging
from discord.ext import commands, tasks
from itertools import cycle
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

BOT_TOKEN = ("NDY0ODI2NzM3MTg5MDYwNjA4.XTcjmQ.KFHHHz1AfFa9VQ3aiNh1lGw-bjk")

# Prefixes #

bot = commands.Bot(command_prefix="Z-", status=discord.Status.idle, activity=discord.Game(name="Loading..."), case_insensitive=True)

changinggame = True

client = commands.Bot(command_prefix='Z-')

# Variables #



#	#	# Fun! #	#	#

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
async def Ping(ctx):
	"""Pangs! :ping_pong:"""
	await ctx.send("Pong! :ping_pong:")

# Shoot Command #

@client.command(name='Shoot',
                description="Shoot an enemy!",
                brief="Shoot your enemies....",
                pass_context=True)
async def Shoot(ctx, context, target: discord.Member):
    possible_responses = [
        'You missed your shot!',
        'Uh oh! The fuzz have arrived!',
        'You hit! ' + target.mention,
        'Your enemy ' + target.mention + ' dies a bloody death!',
        'Ew, blood!',
    ]
    await ctx.send(random.choice(possible_responses) + ", " + context.message.author.mention);

# Stab Command #

@client.command(name='Stab',
                description="Stab an enemy!",
                brief="Stab your enemies....",
                pass_context=True)
async def Shoot(ctx, context, target: discord.Member):
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

    # give users a link to invite thsi bot to their server #
    embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?client_id=464826737189060608&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FuYSydfN&scope=bot")

    await ctx.send(embed=embed)

# Status Message #

@client.event
async def on_ready():
    print('The bot is ready!')
    print('Logged in as')
    print(client.user.name)
    print('Why Is Asyncio Bullying Us')

@client.event   
async def game_changer():
	changinggame = True
	while True:
		randint = random.randint(1, 3)
		users = 0
		for guild in bot.guilds:
			users = users + guild._member_count
		users = format(users, ',d')
		guilds = format(len(bot.guilds), ',d')
		if randint == 1:
			await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"{users} users in {guilds} guilds"))
			await asyncio.sleep(300)
			return
		if randint == 2:
			await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Fire is currently in BETA"))
			await asyncio.sleep(300)
			return
		if randint == 3:
			me = bot.get_user(414822379475304449)
			await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Created by {me}"))
			await asyncio.sleep(300)
			return

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

# Support Us #

@client.command()
async def Support(ctx):
         """Support us for better things"""
         await ctx.send("Join Us Here chat with our friendly staff https://discord.gg/uYSydfN")

# Kick Command #

@client.command(pass_context = True)
async def Kick(ctx, userName: discord.User):
    """Kick a user""" 
    try:
       await client.kick(userName)
       await ctx.send("Successful!")
    except:
       await ctx.send("You don't have permissions :thinking:")

# Ban Command #

@client.command(pass_context = True)
async def Ban(ctx, userName: discord.User):
    """Ban a user""" 
    try:
       await client.ban(userName)
       await ctx.send("Successful!")
    except:
       await ctx.send("You don't have permissions :thinking:")
   

# Unban Command #

@client.command(pass_context = True)
async def Unban(ctx, userName: discord.User):
    """Unban a user ( Oh Snap Here We Go Again)""" 
    try:
       await client.unban(userName)
       await ctx.send("Successful!")
    except:
        await ctx.send("You don't have permissions :thinking:")

# Other important crap #
    
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(str(os.environ.get('BOT_TOKEN')))
