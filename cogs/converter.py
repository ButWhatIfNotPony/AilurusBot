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
        total = round(dist * 1.609, 3)
        await ctx.send(f'{dist} Miles is approximately {total}KM.')


    @commands.command(name='km2miles', aliases=['km2m', 'kilometers2miles'])
    async def kilometersToMiles(self, ctx, dist : float):
        """Converts Kilometers into Miles for you Imperial PEASANTS."""
        total = round((dist / 1.609), 3)
        await ctx.send(f'{dist}KM is approximately {total} Miles.')

    
    @commands.command(name='cels2fahr', aliases=['c2f', 'celsius2fahrenheit'])
    async def celciusToFahrenheit(self, ctx, temp : float):
        """Converts Celsius to Fahrenheit, for whatever reason you would prefer that."""
        total = round((temp * 1.8) + 32, 3)
        await ctx.send(f'{temp}' + chr(176) + f'C is approximatley {total}' + chr(176) + 'F.')

    @commands.command(name='fahr2cels', aliases=['f2c', 'fahrenheit2celsius'])
    async def fahrenheitToCelsius(self, ctx, temp : float):
        """Converts Fahrenheit to Celsius, for the better unit of temperature."""
        total = round((temp -32) * 0.5556, 3)
        await ctx.send(f'{temp}' + chr(176) + f'F is approximately {total}' + chr(176) + 'C.')
        
    
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Converters(bot))