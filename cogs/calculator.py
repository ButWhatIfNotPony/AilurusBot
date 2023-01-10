import sys
import math
import asyncio
import discord
from discord.ext import commands

class Calculator(commands.Cog):
    """A SUPER FAST EXTREME HIGH SPEED TOP OF THE RANGE CALCULATOR!!!"""
    
    def ___init___(self, bot):
        self.bot = bot
        
    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first : float, second : float):
        """DOES ADDITION! (use: {number} {number})"""
        total = first + second
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='sub', aliases=['minus'])
    @commands.guild_only()
    async def do_subtraction(self, ctx, first : int, second : int):
        """DOES SUBTRACTION! (use: {number} {number})"""
        total = first - second
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='mul', aliases=['times'])
    @commands.guild_only()
    async def do_multiplication(self, ctx, first : int, second : int):
        """DOES MULTIPLICATION! (use: {number} {number})"""
        total = first * second
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='div', aliases=['divide'])
    @commands.guild_only()
    async def do_division(self, ctx, first : int, second : int):
        """DOES DIVISION! (use: {number} {number})"""
        total = first / second
        if (second == 0):
            await ctx.send(f'You can\'t divide by 0...')
        else:
            await ctx.send(f'= **{total}**')
        
        
    @commands.command(name='mod', aliases=['modulo'])
    @commands.guild_only()
    async def do_modulo(self, ctx, first : int, second : int):
        """DOES MODULO! (use: {number} {number})"""
        total = first % second
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='pow', aliases=['power'])
    @commands.guild_only()
    async def do_power(self, ctx, first : int, second : int):
        """DOES POWER! (use: {number} {power})"""
        total = pow(first, second)
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='per', aliases=['percent'])
    @commands.guild_only()
    async def do_percentage(self, ctx, first : float, second : float):
        """DOES PERCENTS! (use: {percentage} {number})"""
        percentage = first / 100
        total = second * percentage
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='sqr', aliases=['root', 'squareroot'])
    @commands.guild_only()
    async def do_square_root(self, ctx, *, first : int):
        """DOES SQUARE ROOT! (use: {number})"""
        total = math.sqrt(first)
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='pi')
    @commands.guild_only()
    async def do_pi(self, ctx):
        """DISPLAY PI!"""
        total = math.pi
        await ctx.send(f'= **{total}**')
        
    @commands.command(name='area')
    @commands.guild_only()
    async def shape_area(self, ctx, shape : str, height : float, width : float):
        """WORKS OUT AREA OF SHAPES! (use: {name of shape} {height} {width})"""
        shape = shape.lower()
        
        if shape == "rectangle":
            h = height
            w = width
            
            rect_area = w * h
            await ctx.send(f'= **{rect_area}**')
            
        elif shape == "square":
            s = height
            
            sqr_area = s * s
            await ctx.send(f'= **{sqr_area}**')
            
        elif shape == "triangle":
            h = height
            w = width
            
            tri_area = 0.5 * h * w
            await ctx.send(f'= **{tri_area}**')
            
        else:
            await ctx.send(f'Sorry, that isnt a valid shape, a valid shape is: Rectangle, Square or triangle.')
            
    @commands.command(name='circle')
    @commands.guild_only()
    async def circle(self, ctx, type : str, num : float):
        """WORKS OUT CIRCLES! (use: {area or circumference} {radius})"""
        type = type.lower()
        
        if type == "area":
            pi = math.pi
            r = num
            
            cir_area = pi * r * r
            await ctx.send(f'= **{cir_area}**')
            
        elif type == "circumference" or "circum" or "cir":
            pi = math.pi
            r = num
            
            cir_circum = 2 * pi * r
            await ctx.send(f'= **{cir_circum}**')
            
        else:
            await ctx.send(f'Please enter a valid input: Area or Circumference.')
            
    @commands.command(name='vol', aliases=['volume'])
    @commands.guild_only()
    async def do_volume(self, ctx, shape : str, length : float, height : float, width : float):
        """WORKS OUT VOLUME OF 3D THINGS! (use: {shape} {values})"""
        shape == shape.lower()
        
        if shape == "cube":
            l = length
            w = width
            h = height
            
            vol_cube = l * w * h
            
            await ctx.send(f'= **{vol_cube}**')
            
        elif shape == "pyramid" or "pyra":
            l = length
            w = width
            h = height
            
            vol_pyra = (l * w * h) / 3
            await ctx.send(f'= **{vol_pyra}**')
            
        elif shape == "cone":
            r = length
            h = width
            pi = math.pi
            
            vol_cone = (pi * pow(r, 2) * h) / 3
            await ctx.send(f'= **{vol_cone}**')
            
        elif shape == "cylinder" or "cyl":
            pi = math.pi
            r = length
            h = width
            
            vol_cyl = pi * pow(r, 2) * h
            await ctx.send(f'= **{vol_cyl}**')
            
        elif shape == "sphere":
            pi = math.pi
            r = length
            
            vol_sphere = (4/3) * pi * pow(r, 3)
            await ctx.send(f'= **{vol_sphere}**')
            
        else:
            await ctx.send(f'Sorry, the shape you selected isnt availible, please select from: cube, pyramid, cone, cylinder or sphere.')
        
def setup(bot):
    bot.add_cog(Calculator(bot))