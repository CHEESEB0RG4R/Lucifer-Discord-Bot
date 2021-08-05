import aiohttp
import discord
import random
import asyncio
import requests
import json
from discord.ext import commands


class Actions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(' {0.user} has loaded Actions.py!'.format(self.client))
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Game("as my master's good devil 😈"))
        return

    @commands.command(aliases=['Kill','KILL','kILL'])
    async def kill(self, ctx, arg=''):
        kill = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(kill)
        if arg == '':
            await ctx.channel.send('Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} killed you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/kill/' + gif + '.gif'))

    @commands.command(aliases=['Threaten','THREATEN','tHREATEN'])
    async def threaten(self, ctx, arg=''):
        kill = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(kill)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} threatens you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/threaten/' + gif + '.gif'))

    @commands.command(aliases=['Pat','pAT','PAT'])
    async def pat(self, ctx, arg=''):
        kill = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(kill)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} pats you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/pat/' + gif + '.gif'))

    @commands.command(aliases=['Kiss','KISS','kISS'])
    async def kiss(self, ctx, arg=''):
        kill = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(kill)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} kisses you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/kiss/' + gif + '.gif'))

    @commands.command(aliases=['Bite','BITE','bITE'])
    async def bite(self, ctx, arg=''):
        bite = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(bite)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} bites you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/bite/' + gif + '.gif'))

    @commands.command(aliases=['Bully','BULLY','bULLY'])
    async def bully(self, ctx, arg=''):
        bully = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(bully)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} bullies you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/bully/' + gif + '.gif'))

    @commands.command(aliases=['Hug','HUG','hUG'])
    async def hug(self, ctx, arg=''):
        hug = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(hug)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} hugs you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/hug/' + gif + '.gif'))

    @commands.command(aliases=['Slap','SLAP','sLAP'])
    async def slap(self, ctx, arg=''):
        slap = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(slap)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} slaps you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/slap/' + gif + '.gif'))

    @commands.command(aliases=['Bonk','BONK','bONK'])
    async def bonk(self, ctx, arg=''):
        bonk = ['1', '2', '3', '4', '5', '6']
        gif = random.choice(bonk)
        if arg == '':
            await ctx.channel.send('Ok... Next time mention someone on whom you wanna use actions...')
        else:
            await ctx.channel.send(f'{ctx.author.name} bonks you ' + arg)
            await ctx.channel.send(file=discord.File('./resources/bonk/' + gif + '.gif'))


def setup(client):
    client.add_cog(Actions(client))
