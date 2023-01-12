import discord
from discord.ext import commands

import time, random, sys

class Games(commands.Cog):
    """Commands"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='8ball')
    @commands.guild_only()
    async def m8b(self, ctx, text=""):
        """Will answer any yes or no questions.. by contacting my ancestors.."""
        await ctx.send(f'P L E A S E  A S K  Y O U R  Q U E S T I O N...')
            
        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
            
        question = await self.bot.wait_for("message", check=check)
        
        replies = [
            'LET ME THINK ON THIS...',
            'AN INTERESTING QUESTION...',
            'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
            'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
            'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
            'YES... NO... MAYBE... I WILL THINK ON IT...',
            'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
            'I SHALL CONSULT MY VISIONS...',
            'YOU MAY WANT TO SIT DOWN FOR THIS...'
        ]
        
        answers = [
            'YES, FOR SURE',
            'MY ANSWER IS NO',
            'ASK ME LATER',
            'I AM PROGRAMMED TO SAY YES',
            'THE STARS SAY YES, BUT I SAY NO',
            'I DUNNO MAYBE',
            'FOCUS AND ASK ONCE MORE',
            'DOUBTFUL, VERY DOUBTFUL',
            'AFFIRMITIVE',
            'YES, THOUGH YOU MAY NOT LIKE IT',
            'NO, BUT YOU MAY WISH IT WAS SO'
        ]
        
        if question.content.lower() == "cancel" or question.content.lower() == "quit":
            await ctx.send(f'N E V E R M I N D  T H E N...')
        else:
            await ctx.send(random.choice(replies))
            time.sleep(3)
            await ctx.send(random.choice(answers))
        
    @commands.command(name='diceroll', aliases=['rolldice'])
    @commands.guild_only()
    async def dice_roll(self, ctx, num=0):
        """Rolls dice with as many sides as you want!"""
        
        
        if num == 0:
            message = await ctx.send(f'Enter a number of sides:')
            
            def check(msg):
                return msg.author == ctx.author
                
            message = await self.bot.wait_for("message", check=check)
            msg = message.content
        else:
            message = num
            msg = message
                
        if msg == 'Cancel' or msg == 'Quit' or msg == 'cancel' or msg == 'quit':
            await ctx.send(f'Nevermind then...')
            return
            
        coming = await ctx.send(f'Here it comes...')
        time.sleep(1)
        await ctx.send(f"**{random.randint(1, int(msg))}**")

    
    @commands.command(name='rps', aliases=['rockpaperscissors'])
    @commands.guild_only()
    async def play_RPS(self, ctx, turn=None):
        """Play a game of Rock, Paper, Scissors! (Don't worry, its random lol)"""

        turns = ["rock", "raper", "rcissors"]
        botAnswer = random.choice(turns)

        if turn == None:
            message = await ctx.send(f'Sure, pick Rock, Paper, or Scissors:')

            def check(msg):
                return msg.author == ctx.author

            message = await self.bot.wait_for("message", check=check)
            msg = message

        if msg.lower() != 'rock' or msg.lower() != 'paper' or msg.lower() != 'scissors':
            await ctx.send(f'Please enter a valid tunr :(... Rock, Paper, or Scissors:')
        elif msg.lower() == 'quit' or msg.lower() == 'cancel':
            await ctx.send(f'Oh.. Ok.. Nevermind then.')
        else:
            if msg.lower() == botAnswer:
                await ctx.send(f'**{botAnswer}!**')
                time.sleep(0.5)
                await ctx.send(f'It\'s a tie! :)')
            elif msg.lower() == "rock" and botAnswer == "scissors":
                await ctx.send(f'**{botAnswer}!**')
                time.sleep(0.5)
                await ctx.send(f'You win!! :)')
            elif msg.lower() == "paper" and botAnswer == "rock":
                await ctx.send(f'**{botAnswer}!**')
                time.sleep(0.5)
                await ctx.send(f'You win!! :)')
            elif msg.lower() == "scissors" and botAnswer == "paper":
                await ctx.send(f'**{botAnswer}!**')
                time.sleep(0.5)
                await ctx.send(f'You win!! :)')
            else:
                await ctx.send(f'**{botAnswer}!**')
                time.sleep(0.5)
                await ctx.send(f'You lose!! :)')
            
        
    
# The setup function below is neccersary. Remeber we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Games(bot))