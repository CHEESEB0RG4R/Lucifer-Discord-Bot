import aiohttp
import discord
import random
import asyncio
import requests
import json
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(' {0.user} has loaded Fun.py!'.format(self.client))
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Game("as my master's good devil 😈"))
        return

    @commands.command(aliases=['8ball', 'predict'])
    async def _8ball(self, ctx, *, question):
        predictions = [f"As I see it, yes. {ctx.author.mention}", f"Ask again later. {ctx.author.mention}",
                       f"Better not tell you now. {ctx.author.mention}",
                       f"Cannot predict now. {ctx.author.mention}",
                       f"Concentrate and ask again. {ctx.author.mention}", f"Don’t count on it. {ctx.author.mention}",
                       f"It is certain. {ctx.author.mention}",
                       f"It is decidedly so. {ctx.author.mention}",
                       f"Most likely. {ctx.author.mention}", f"My reply is no. {ctx.author.mention}",
                       f"My sources say no. {ctx.author.mention}", f"Outlook not so good. {ctx.author.mention}",
                       f"Outlook good. {ctx.author.mention}",
                       f"Reply hazy, try again. {ctx.author.mention}", f"Signs point to yes. {ctx.author.mention}",
                       f"Very doubtful. {ctx.author.mention}",
                       f"Without a doubt. {ctx.author.mention}",
                       f"Yes. {ctx.author.mention}",
                       f"Yes – definitely. {ctx.author.mention}", f"You may rely on it. {ctx.author.mention}"]

        async with ctx.channel.typing():
            await asyncio.sleep(0.5)
            await ctx.reply(random.choice(predictions))

    @commands.command()
    async def rps(self, ctx, arg):
        rps = ['rock', 'paper', 'scissor']
        bot_choice = random.choice(rps)
        user_choice = str(arg).lower()

        if user_choice == 'rock':
            if bot_choice == 'rock':
                about = discord.Embed(title="Well well,If it ain't the fckin draw...")
                about.set_author(name="🗿 vs 🗿")
                await ctx.send(embed=about)
            elif bot_choice == 'paper':
                about = discord.Embed(title="I win...Nothing so great about it...")
                about.set_author(name="🗿 vs 📃")
                await ctx.send(embed=about)
            elif bot_choice == 'scissor':
                about = discord.Embed(title="You win...Congrats...")
                about.set_author(name="🗿 vs ✂️")
                await ctx.send(embed=about)
        elif user_choice == 'scissor':
            if bot_choice == 'rock':
                about = discord.Embed(title="I win...Nothing so great about it...")
                about.set_author(name="✂️vs 🗿")
                await ctx.send(embed=about)
            elif bot_choice == 'paper':
                about = discord.Embed(title="You win...Congrats...")
                about.set_author(name="✂️vs 📃")
                await ctx.send(embed=about)
            elif bot_choice == 'scissor':
                about = discord.Embed(title="Well well,If it ain't the fckin draw...")
                about.set_author(name="✂️vs ✂️")
                await ctx.send(embed=about)
        elif user_choice == 'paper':
            if bot_choice == 'rock':
                about = discord.Embed(title="You win...Congrats...")
                about.set_author(name="📃  vs 🗿")
                await ctx.send(embed=about)
            elif bot_choice == 'paper':
                about = discord.Embed(title="Well well,If it ain't the fckin draw...")
                about.set_author(name="📃 vs 📃")
                await ctx.send(embed=about)
            elif bot_choice == 'scissor':
                about = discord.Embed(title="I win...Nothing so great about it...")
                about.set_author(name="📃 vs ✂️")
                await ctx.send(embed=about)
        else:
            await ctx.send(
                "It seems that I have to teach you this. You have to chose one from rock/paper/scissor in a rock paper scissor game")

    @commands.command()
    async def animeme(self, ctx, arg=1):
        sendmemes = 0
        while sendmemes < arg:
            memes = discord.Embed(title="Here your Animeme")
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/Animemes/new.json?sort=hot') as r:
                    res = await r.json()
                    url = res['data']['children'][random.randint(0, 25)]['data']['url']
                    if url is not None and url != "https://www.youtube.com/*":
                        async with aiohttp.ClientSession() as ch:
                            async with ch.get('https://www.reddit.com/r/AnimeFunny/about.json') as over18:
                                over_18 = await over18.json()
                                check = over_18['data']['over18']
                                if check is False:
                                    memes.set_image(url=url)
                                    await ctx.send(embed=memes)
                                    sendmemes += 1

    @commands.command()
    async def meme(self, ctx, arg=1):
        sendmemes = 0
        while sendmemes < arg:
            meme = discord.Embed(title='Here your meme')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                    res = await r.json()
                    url = res['data']['children'][random.randint(0, 25)]['data']['url']
                    print(url)
                    if url is not None:
                        meme.set_image(url=url)
                        await ctx.send(embed=meme)
                        sendmemes += 1

    @commands.command()
    async def dankmeme(self, ctx, arg=1):
        sendmemes = 0
        while sendmemes < arg:
            meme = discord.Embed(title='Here your DankMeme')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                    res = await r.json()
                    url = res['data']['children'][random.randint(0, 25)]['data']['url']
                    if url is not None:
                        meme.set_image(url=url)
                        await ctx.send(embed=meme)
                        sendmemes += 1

    @commands.command()
    async def anigif(self, ctx, arg=1):
        sendmemes = 0
        while sendmemes < arg:
            meme = discord.Embed(title='Here your AnimeGif')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/animegifs/new.json?sort=hot') as r:
                    res = await r.json()
                    url = res['data']['children'][random.randint(0, 25)]['data']['url']
                    if url is not None:
                        meme.set_image(url=url)
                        await ctx.send(embed=meme)
                        sendmemes += 1

    @commands.command()
    async def animesupply(self, ctx, arg=1):
        sendmemes = 0
        while sendmemes < arg:
            meme = discord.Embed(title='Here your daily anime suppply')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/awwnime/new.json?sort=hot') as r:
                    res = await r.json()
                    url = res['data']['children'][random.randint(0, 25)]['data']['url']
                    if url is not None:
                        meme.set_image(url=url)
                        await ctx.send(embed=meme)
                        sendmemes += 1


def setup(client):
    client.add_cog(Fun(client))
