# +=============================================+
# +===============+ Set up +===============+
# +=============================================+

# =====
# = Import =
# =====

import discord
import os
from discord.ext import commands
import random
from random import randint
import asyncio
import requests
import json
import traceback
from traceback import *
import TextToOwO
from TextToOwO import *

# =====
# = Prefix =
# =====

client = commands.Bot(command_prefix = 'suk!')

with open('settings.json') as f:
    data = json.load(f)

token = (data['token'])

# =====
# = Cogs =
# =====

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

    await ctx.send(f'Reloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# =====
# = On ready check =
# =====

@client.event
async def on_ready():
    # Prints that it is ready
    print ('------------------------------------')
    print ('Bot Name: ' + client.user.name)
    print ('Bot ID: ' + str(client.user.id))
    print ('Discord Version: ' + discord.__version__)
    print ('------------------------------------')

    # Sets the status to "Do Not Disturb", sets the game it is playing to "suk!help"
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('use \'suk!help\'.'))

# =====
# = Ping =
# =====

@client.command()
async def ping(ctx):

    # ===== Embed =====
    embed=discord.Embed(title='Ping', description=':ping_pong: Test the connection.', color=0x80ffff)
    embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.add_field(name='Result', value=f'Pong! {round(client.latency * 1000)}ms.', inline=False)
    embed.set_footer(text='Suki Bot')
    # ===============

    await ctx.send(embed=embed)

# =====
# = Error handler =
# =====

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):

        # ========== Embed ==========
        embed = discord.Embed(title='ERROR', description=':exclamation: Command not found.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_footer(text='Suki Bot')
        # =========================

        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):

        # ========== Embed ==========
        embed = discord.Embed(title='ERROR', description=':exclamation: Missing required arguments.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_footer(text='Suki Bot')
        # =========================

        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):

        # ========== Embed ==========
        embed = discord.Embed(title='ERROR', description=':exclamation: User is missing required permissions.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_footer(text='Suki Bot')
        # =========================

        await ctx.send(embed=embed)

    elif isinstance(error, commands.BotMissingPermissions):

        # ========== Embed ==========
        embed = discord.Embed(title='ERROR', description=':exclamation: Bot is missing required permissions.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.set_footer(text='Suki Bot')
        # =========================

        await ctx.send(embed=embed)

# +=============================================+
# +===============+ Log in +===============+
# +=============================================+

client.run(token)