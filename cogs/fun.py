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

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client






    # +=============================================+
    # +===============+ Features +===============+
    # +=============================================+

    # =====
    # = 8Ball =
    # =====

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):

        eightBallResult = [
                "Where my bepis?",
                "It is decidedly so.",
                "Without a doubt.",
                "Yos - definitely.",
                "U may rely on it.",
                "As I see it, yos.",
                "Most likely.",
                "Fren, i thinc u done too many spinnos.",
                "Yos.",
                "Sparkly sniffer on your pupper point to yos.",
                "Reply hazy, try again.",
                "Don give up! Believe in u.",
                "Better not tell u now.",
                "Cannot predict now.",
                "Ask again after gibing chimcken.",
                "Don't count on it.",
                "Why ask when you have Shibe?",
                "My sources say no.",
                "Stop it, u are doing me a frighten.",
                "Heckin doubtful."]

        # ===== Embed =====
        embed=discord.Embed(title='8ball', description=f':8ball: Ask the magic 8ball.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Question', value=f'{question}', inline=False)
        embed.add_field(name='Answer', value=f'{random.choice(eightBallResult)}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    # =====
    # = Doggo image =
    # =====

    @commands.command(aliases=['doggoimage', 'dogimg', 'dogimage'])
    async def doggoimg(self, ctx):
        raw = requests.get('https://dog.ceo/api/breeds/image/random')

        img = json.loads(raw.text)

        await ctx.send(img['message'])

    # =====
    # = Shibe image =
    # =====

    @commands.command(aliases=['shibeimage', 'shibaimg', 'shibaimage'])
    async def shibeimg(self, ctx):
        raw = requests.get('https://dog.ceo/api/breed/shiba/images/random')

        img = json.loads(raw.text)

        await ctx.send(img['message'])

    # =====
    # = Coin flip =
    # =====

    @commands.command(aliases=['flipcoin'])
    async def coinflip(self, ctx):

        flipResultPool = [
            'Heads',
            'Tails'
        ]

        flipResult = random.choice(flipResultPool)

        # ===== Embed =====
        embed=discord.Embed(title='Coinflip', description=f':moneybag: Flip a coin.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Flip', value=f'{flipResult}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    # =====
    # = Roll dice =
    # =====

    @commands.command(aliases=['rolldice'])
    async def rolldie(self, ctx, amount = 6):
        outcome = (randint(1,amount))

        # ===== Embed =====
        embed=discord.Embed(title='Rolldie', description=':game_die: Roll a die.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Die', value=f'd{amount}', inline=False)
        embed.add_field(name='Outcome', value=f'{outcome}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    # =====
    # = Rps =
    # =====

    @commands.command(aliases=['rockpaperscissors'])
    async def rps(self, ctx, playerChoice):

        comChoicePool = ['rock', 'paper', 'scissors']

        comChoice = random.choice(comChoicePool)

        if (playerChoice == comChoice):
            rpsResult = ('Draw')
        # Player chooses rock
        elif (playerChoice == 'rock'):
            if (comChoice == 'paper'):
                rpsResult = ('Shibe Wins')
            else:
                rpsResult = ('Hooman Wins')

        # Player chooses paper
        elif (playerChoice == 'paper'):
            if (comChoice == 'scissors'):
                rpsResult = ('Shibe Wins')
            else:
                rpsResult = ('Hooman Wins')

        # Player chooses scissors
        elif (playerChoice == 'scissors'):
            if (comChoice == 'rock'):
                rpsResult = ('Shibe Wins')
            else:
                rpsResult = ('Hooman Wins')

        else:
            rpsResult = ('An error occured')

        # ===== Embed =====
        embed=discord.Embed(title="RPS", description=":scissors: Rock, paper, scissors.", color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Hooman', value=f'{playerChoice}', inline=True)
        embed.add_field(name='Shibe', value=f'{comChoice}', inline=True)
        embed.add_field(name='Result', value=f'{rpsResult}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    # =====
    # = Shoot =
    # =====

    @commands.command()
    async def shoot(self, ctx, member : discord.Member):
        shotOrMissPool = [
            'shot',
            'missed']

        shotOrMissResult = random.choice(shotOrMissPool)

        # ===== Embed =====
        embed=discord.Embed(title='Shoot', description=f':gun: Shoot someone.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Shot or miss?', value=f'You {shotOrMissResult} {member}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    # =====
    # = Rate Hooman =
    # =====

    @commands.command(aliases=['rate'])
    async def ratehooman(self, ctx, member : discord.Member):

        rating = randint(0,100)

        # ===== Embed =====
        embed=discord.Embed(title='Ratehooman', description=f':chart_with_upwards_trend: Analyse the rating of a hooman.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Rating', value=f'Hooman {member} is rated {rating}/100', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)

    @commands.command(aliases=['weebify'])
    async def weeb(self, ctx, *, text):

        weebText = (owo.text_to_owo(f'{text}'))

        # ===== Embed =====
        embed=discord.Embed(title='Weeb', description=f':sushi: Weebify your sentences.', color=0x80ffff)
        embed.set_author(name=f'{ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='Message', value=f'{weebText}', inline=False)
        embed.set_footer(text='Suki Bot')
        # ===============

        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Fun(client))