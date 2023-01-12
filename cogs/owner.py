import discord
from discord.ext import commands

class Owner(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        """A simple command which only the owner has privilege to use :)"""
        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you! UwU')
        
    # Hidden means it won't show up on the default help menu.
    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog : str):
        """Command which Loads a Module."""

        cogg = "cogs." + cog

        try:
            self.bot.load_extension(cogg)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            
    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog : str):
        """Command which Unloads a Module."""

        cogg = "cogs." + cog

        try:
            self.bot.unload_extension(cogg)
        except Exception as e:
            await ctx.send(f'**ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
                
    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog : str):
        """Command which Reloads a Module."""
            
        cogg = "cogs." + cog

        try:
            self.bot.unload_extension(cogg)
            self.bot.load_extension(cogg)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
                
            
def setup(bot):
    bot.add_cog(Owner(bot))