import aiohttp
import discord
import random
import asyncio
import requests
import json
import math
from discord.ext import commands

class Genshin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(' {0.user} has loaded Genshin.py!'.format(self.client))
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Game("as my master's good devil 😈"))
        return


    @commands.command()
    async def genshinmeme(self, ctx, arg=1):
        sendmemes = 0
        while sendmemes < arg:
            meme = discord.Embed(title='Here your genshin meme')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/Genshin_Memepact/new.json?sort=hot') as r:
                    res = await r.json()
                    url = res['data']['children'][random.randint(0, 25)]['data']['url']
                    print(url)
                    if url is not None:
                        meme.set_image(url=url)
                        await ctx.send(embed=meme)
                        sendmemes += 1
    @commands.command()
    async def characterwish(self, ctx):
      luck = random.randint(1,100)
      fivestars = ['Diluc','Jean','Venti','Ganyu']
      fourstars = ['Bennett','Sucrose','Amber','Lisa']
      if luck > 75:
        char = random.choice(fivestars)
        
      else:
        char = random.choice(fourstars)
       
      await ctx.send('You got ' + char)

def setup(client):
    client.add_cog(Genshin(client))
