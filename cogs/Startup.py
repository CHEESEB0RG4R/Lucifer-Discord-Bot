import discord
from discord.ext import commands


class Startup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(' {0.user} has loaded Startup.py!'.format(self.client))
        print(' {0.user} is here...Watch yourself... '.format(self.client))
        await self.client.change_presence(status=discord.Status.online,
                                          activity=discord.Game("as my master's good devil 😈"))
        return

    async def on_member_join(self, member):
        print(f'Hey {member.mention}, Welcome to our server!')
        guild = self.client.get_guild(855070062423834673)
        general_channel = guild.get_channel(855070062423834676)
        await general_channel.send(f'Hey {member.mention}, Welcome to our server!')

def setup(client):
    client.add_cog(Startup(client))
