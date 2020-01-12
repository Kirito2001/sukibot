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
import TextToOwO
from TextToOwO import *

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client






    # +=============================================+
    # +===============+ Features +===============+
    # +=============================================+

    # =====
    # = Kick =
    # =====

    @commands.command(aliases=['kickuser'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):

        await member.kick(reason = reason)

        # ===== Embed =====
        embed=discord.Embed(title='Kick', description=':foot: Kick a user.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Result', value=f'Kicked {member}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    # =====
    # = Ban =
    # =====

    @commands.command(aliases=['banuser'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):

        await member.ban(reason = reason)

        # ===== Embed =====
        embed=discord.Embed(title='Ban', description=':hammer: Ban a user.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Result', value=f'Banned {member}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))