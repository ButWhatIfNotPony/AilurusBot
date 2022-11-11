import discord
from discord.ext import commands

import time, random, sys

class Converters(commands.Cog):
    """Commands"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='miles2km', aliases=['m2km', 'miles2kilometers'])
    async def milesToKilometers(self, ctx, dist : float):
        """Converts Miles into Kilometers for us Metric CHADS."""
        total = dist * 1.609
        await ctx.send(f'{dist} Miles is approximately {total}KM.')


    @commands.command(name='km2miles', aliases=['km2m', 'kilometers2miles'])
    async def kilometersToMiles(self, ctx, dist : float):
        """Converts Kilometers into Miles for you Imperial PEASANTS."""
        total = dist / 1.609
        await ctx.send(f'{dist}KM is approximately {total} Miles.')
        
    
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Converters(bot))