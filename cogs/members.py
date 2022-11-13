import discord
from discord.ext import commands

class Members(commands.Cog):
    """Commands"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member : discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')
        
    @commands.command(name='bamboo')
    async def bamboo(self, ctx):
        """WHAT! BAMBOO!!"""
        await ctx.send('WHERE?!? I WANT THE BAMBOO!! ITS M I N E.')
        
    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input : str):
        """A Simple Command which repeats our input."""
        await ctx.send(our_input)
    
    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member : discord.Member=None):
        """Simple command which shows the members Top Role."""
        
        if member is None:
            member = ctx.author
            
        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
        
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member : discord.Member=None):
        """A simple command which checks a members Guild Permissions.
           if member is not provided, the author will be checked."""
        
        if not member:
            member = ctx.author
            
        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)
        
        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        
        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)
        
        await ctx.send(content=None, embed=embed)


    @commands.command(name='hi', aliases=['hey', 'hello'])
    @commands.guild_only()
    async def sayHi(self, ctx):
        """Say Hi to me, and I'll respond :)"""
        user = ctx.author.name

        if user == 'Bodin':
            response = 'Hello Server Owner OwO!'
        else:
            response = f'Hi, {user}! How are you today? Been up to much lately? It was nice meeting you!'

        await ctx.send(response)
        
        
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Members(bot))