import discord
from discord.ext import commands

import sys, traceback


def get_prefix(bot, message):
    '''A callable Prefix for our bot. This could be edited to allow per server prefixes.'''
    
    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['~', '#', '+']
    
    # Check to see if we are outside of a guild (server). e.g. DMs etc.
    if not message.guild:
        # Only allow # to be used in DMs.
        return '#'
        
    # If we are in a guild, we allow for the user to mention us or us any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)
    

# Below cogs represents our folder our cogs are in. Following is the file name. So 'example.py' in cogs, would be cogs.example
# Think of it like a dot path import.
initial_extensions = ['cogs.owner', 'cogs.members', 'cogs.calculator', 'cogs.listeners', 'cogs.games', 'cogs.converter']

# Below is the description that displays in the help menu
description = '''AilurusBot is written in Python!
                 Powered by a Raspberry Pi 3B+ :)'''

bot = commands.Bot(command_prefix=get_prefix, description=description, activity=discord.Game(name='Bamboo Eating Simulator 2022'))

# Here we load our extensions(cogs) listed above in [init_exts].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')

with open("TOKEN.txt", 'r') as f:
    TOKEN = f.read()
    
bot.run(TOKEN, bot=True, reconnect=True)
