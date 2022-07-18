import discord
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Client()

@bot.event
async def on_ready():
    print("BOT IS ONLINE")

@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
            await msg.channel.send("hello " + username )

@bot.event
async def on_member_join(member): #server welcoming when somebody invited server
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}!")

bot.run(os.getenv('DISCORD_TOKEN'))