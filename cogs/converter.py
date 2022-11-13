import discord
from discord.ext import commands

import time, random, sys

class Converters(commands.Cog):
    """Commands"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='miles2kilometers', aliases=['m2km', 'miles2km'])
    async def milesToKilometers(self, ctx, dist : float):
        """Converts Miles into Kilometers for us Metric CHADS."""
        total = round(dist * 1.609, 3)
        await ctx.send(f'{dist} Miles is approximately {total}KM.')


    @commands.command(name='kilometers2miles', aliases=['km2m', 'km2miles'])
    async def kilometersToMiles(self, ctx, dist : float):
        """Converts Kilometers into Miles for you Imperial PEASANTS."""
        total = round((dist / 1.609), 3)
        await ctx.send(f'{dist}KM is approximately {total} Miles.')

    
    @commands.command(name='celsius2fahrenheit', aliases=['c2f', 'cels2fahr'])
    async def celciusToFahrenheit(self, ctx, temp : float):
        """Converts Celsius to Fahrenheit, for whatever reason you would prefer that."""
        total = round((temp * 1.8) + 32, 3)
        await ctx.send(f'{temp}' + chr(176) + f'C is approximatley {total}' + chr(176) + 'F.')


    @commands.command(name='fahrenheit2celsius', aliases=['f2c', 'fahr2cels'])
    async def fahrenheitToCelsius(self, ctx, temp : float):
        """Converts Fahrenheit to Celsius, for the better unit of temperature."""
        total = round((temp -32) * 0.5556, 3)
        await ctx.send(f'{temp}' + chr(176) + f'F is approximately {total}' + chr(176) + 'C.')


    @commands.command(name='kilograms2pounds', aliases=['kg2lbs', 'kilos2lbs'])
    async def kilogramsToPounds(self, ctx, weight : float):
        """Converts Kilograms to Pounds."""
        total = round(weight * 2.2, 3)
        await ctx.send(f'{weight}KG is approximately {total}LB.')


    @commands.command(name='pounds2kilograms', aliases=['lbs2kg', 'lbs2kilos'])
    async def poundsToKilograms(self, ctx, weight : float):
        """Converts Pounds to Kilograms."""
        total = round(weight / 2.2, 3)
        await ctx.send(f'{weight}LB is approximately {total}KG.')
        
    
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Converters(bot))