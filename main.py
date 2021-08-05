import os
import discord
import random
import requests
import json
import asyncio
from discord.ext import commands
from keep_alive import keep_alive


client = commands.Bot(command_prefix=['L!','l!'] )

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Use the command correctly')
	elif isinstance(error, commands.ArgumentParsingError):
		await ctx.send('Use the command correctly')
	elif isinstance(error, commands.BadArgument):
		await ctx.send('Use the command correctly')


keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
