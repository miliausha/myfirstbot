import discord
intents = discord.Intents.all()

bot = discord.Client(intents = intents)

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

bot.run("OTk3NDIyNDQxNTU3MTM1NDAw.Gvc0pK.5-tBsIiJSvGLhX9FdPvilOGsgWfetfMaLG14Ps")

