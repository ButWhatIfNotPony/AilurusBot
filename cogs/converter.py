import discord
from discord.ext import commands

import time, random, sys

class Converters(commands.Cog):
    """Commands"""
    def __init__(self, bot):
        self.bot = bot
        
    
        
    
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Converters(bot))