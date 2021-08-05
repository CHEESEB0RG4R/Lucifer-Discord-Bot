import discord
import random
import asyncio
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(' {0.user} has loaded Moderation.py!'.format(self.client))
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Game("as my master's good devil 😈"))
        return

    @commands.command(aliases=['clear', 'del', 'clr'])
    async def delete(self, ctx, arg=10):
        if ctx.author.id == 498115557581783040:
            async with ctx.channel.typing():
                await asyncio.sleep(0.5)
                await ctx.channel.purge(limit=arg)
                await ctx.channel.send(f"**{str(arg)}** messages deleted!")
                await ctx.channel.purge(limit=1)
        else:
            async with ctx.channel.typing():
                await asyncio.sleep(0.5)
                await ctx.channel.send("messages ah delete panna nee yaarda $@#!%")

    @commands.command()
    async def kick(self, ctx, arg: discord.Member, *, reason=None):
        if ctx.author.id == 498115557581783040:
            await arg.kick(reason=reason)
            await ctx.send(f'Kicked {arg.mention}')
        else:
            async with ctx.channel.typing():
                await asyncio.sleep(0.5)
                await ctx.channel.send("Don't do that, You've no permissions to do so!S")

    @commands.command()
    async def ban(self, ctx, arg: discord.Member, *, reason=None):
        if ctx.author.id == 498115557581783040:
            await arg.ban(reason=reason)
            await ctx.send(f'Banned {arg.mention}')
        else:
            async with ctx.channel.typing():
                await asyncio.sleep(0.5)
                await ctx.channel.send("Don't do that, You've no permissions to do so!")

    @commands.command()
    async def unban(self, ctx, *, arg):
        if ctx.author.id == 498115557581783040:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = arg.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')
                    return
        else:
            async with ctx.channel.typing():
                await asyncio.sleep(0.5)
                await ctx.channel.send("Don't do that, You've no permissions to do so!")


def setup(client):
    client.add_cog(Moderation(client))
