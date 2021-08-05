import asyncio
import os
import discord
from discord.ext import commands
import random
import requests
import json
import time


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return quote


class General(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(' {0.user} has loaded General.py!'.format(self.client))
		await self.client.change_presence(
		    status=discord.Status.online,
		    activity=discord.Game("as my master's good devil 😈"))
		return

	@commands.command(aliases=['quote', 'motivate', 'encourage'])
	async def inspire(self, ctx):
		quote = get_quote()
		async with ctx.channel.typing():
			await asyncio.sleep(0.5)
			await ctx.send(quote)

	@commands.command(aliases=['hello', 'yo', 'hey'])
	async def hi(self, ctx):
		welcome_reply = [
		    f'Yo {ctx.author.mention}, Sup?',
		    f'Hey {ctx.author.mention}, How are ya doin?',
		    f'Helloo {ctx.author.mention}! My Frend!',
		    f'Hi there {ctx.author.mention}',
		    f'Looking for a companion? {ctx.author.mention}'
		]
		if ctx.author.id == 498115557581783040:
			async with ctx.channel.typing():
				await asyncio.sleep(0.5)
				await ctx.send("How may I help you Master?")
		else:
			async with ctx.channel.typing():
				await asyncio.sleep(0.5)
				await ctx.send(random.choice(welcome_reply))

	@commands.command()
	async def ping(self, ctx):
		time_1 = time.perf_counter()
		await ctx.trigger_typing()
		time_2 = time.perf_counter()
		ping = round((time_2 - time_1) * 1000)
		await ctx.send(f"Your Ping is **{ping}ms!** {ctx.author.mention}")

	@commands.command(aliases=['say', 'repeat'])
	async def echo(self, ctx, *, content: str):
		await ctx.message.delete()
		await ctx.send(content)

	@commands.command()
	async def about(self, ctx):
		if ctx.author.id == 498115557581783040:
			about = discord.Embed(
			    title="The sDevil",
			    description=" I am <@498115557581783040>\'s good little devil."
			)
			about.set_author(name="Lucifer")
			# about.set_thumbnail(url="https://forum.xda-developers.com/data/avatars/o/7047/7047058.jpg")
			about.set_footer(icon_url=ctx.author.avatar_url,
			                 text="I am glad to help you {}!".format(
			                     ctx.author.display_name))
			await ctx.send(embed=about)
			return


def setup(client):
	client.add_cog(General(client))
