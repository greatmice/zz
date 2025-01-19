import aiohttp
import discord
import os
import time

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(guild_ids=['962454553209470996'],description='Pings the bot')
async def ping(ctx):
    t1 = time.time()
    message = await ctx.respond("Pong!")
    t2 = time.time()
    latency = int((t2 - t1) * 1000)
    await message.edit(content=f"Pong! `{latency}ms`")
    
@bot.slash_command(guild_ids=['962454553209470996'], description='Gets a random a VERY funny joke')
async def dadjoke(ctx): 
    async with aiohttp.ClientSession() as session:
        async with session.get("https://icanhazdadjoke.com",headers = {
        'Accept': 'application/json'
    }) as response:
            data = await response.json()
            await ctx.respond(f"{data['joke']}")
            
bot.run(os.getenv("TOKEN"))
