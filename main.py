import aiohttp
import discord
import os
import time

bot = discord.Bot()

token =os.getenv("TOKEN") 

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=['962454553209470996'],description='Pings the bot')
async def ping(ctx):
    t1 = time.time()
    message = await ctx.respond("Pong!")
    t2 = time.time()
    ms = (t2 - t1) * 1000
    await message.edit(content=f"Pong! `{ms:.0f}ms`")
    
@bot.slash_command(guild_ids=['962454553209470996'], description='Gets a random a VERY funny joke')
async def joke(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://official-joke-api.appspot.com/random_joke') as response:
            data = await response.json()
            await ctx.respond(f"{data['setup']}—{data['punchline']}")
            
bot.run(token)
