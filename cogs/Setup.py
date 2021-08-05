import asyncio
import os
import discord
from discord.ext import commands
import random
import requests
import json


class Setup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(' {0.user} has loaded Setup.py!'.format(self.client))
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Game("as my master's good devil 😈"))
        return

    @commands.command()
    async def load(self, ctx, extension):
        if ctx.author.id == 498115557581783040:
            self.client.load_extension(f'cogs.{extension}')
            await ctx.send(f'{extension} module loaded')
        else:
            await ctx.send(f'Command restricted! {ctx.author.mention}')

    @commands.command()
    async def reload(self, ctx, extension):
        if ctx.author.id == 498115557581783040:
            self.client.reload_extension(f'cogs.{extension}')
            await ctx.send(f'{extension} module reloaded')
        else:
            await ctx.send(f'Command restricted! {ctx.author.mention}')

    @commands.command()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        if ctx.author.id == 498115557581783040:
            await ctx.send(f'{extension} module unloaded')
        else:
            await ctx.send(f'Command restricted! {ctx.author.mention}')

    @commands.command()
    async def botping(self, ctx):
        await ctx.send(f'My ping  is **{round(self.client.latency * 1000)}ms!**')


def setup(client):
    client.add_cog(Setup(client))
