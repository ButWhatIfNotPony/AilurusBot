import discord
from discord.ext import commands

class Listener(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event listener which is called when a user is banned from the guild."""
        
        print(f'{user.name}-{user.id} was bannded from {guild.name}-{guild.id}')
        
def setup(bot):
    bot.add_cog(Listener(bot))