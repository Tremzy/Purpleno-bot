import discord
from discord import app_commands
from discord.ext import commands
from discord import FFmpegPCMAudio
from colorama import Style
from colorama import Fore
import os
import random
import asyncio
import string
import mysql.connector
import time
import datetime
from datetime import datetime
import json
import subprocess
import typing
from typing import List
import nacl
import platform 
import youtube_dl
from requests import get
import requests
import openai
import math
import base64


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.bans = True
activity = discord.Activity(name=f"/help | ", type=discord.ActivityType.watching)
bot = commands.Bot(command_prefix="$", intents= discord.Intents.all())
MAX_MEMBERS_PER_SECOND = 1
members_count = []
message_counts = {}
warns = {}
reportbanneds = []
voicebanneds = []
economybanneds = []
global userentries
userentries = []
mutecl = {}
nitrocl = {}
money = {}
inv = {}
COOLDOWN = 30
channelsdeleted = {}
workcl = {}
crimecl = {}
channeldelcd = {}
trashcl = {}
robcl = {}
taxes = {}
minecl = {}
digcl = {}
usertickets = []
global cooldwnsays
global taxgame
taxgame = False
evadecl = {}
cooldwnsays = ["Slow down bozo, you dont need to rush anywhere", "Chill, pill mate!", "You need to cool down a bit, its already warm here 😏", "Hey, hey hey! You have the time, just chill..."]
huntcl = {}
shopitems = {"Shovel": 3500,"Pickaxe": 4000, "Rifle": 5000, "Anti-rob pack": 3000, "Fishing rod": 2500, "Redbull": 500, "Wallet expander": 4000, "Phone": 1100, "Pistol": 7900, "Bread": 500, "Gum": 250, "Ammo": 1800, "Monster": 600, "Pet food": 200, "Cheese": 400, "Hamburger": 1000, "Pizza" : 1000, "Gyros": 1000, "Taco": 1000}
sellitems = {"Fish": 750, "Coal": 300, "Ruby": 550, "Iron": 400, "Diamond": 900, "Gold": 750, "Silver": 380, "Copper": 350, "Junk": 150, "Stone": 80, "Empty beer": 170, "Steel": 560, "Broken glass": 120, "Rabbit": 500, "Deer": 1500, "Sheep": 1200, "Bear": 3000, "Capybara": 8000, "Cow": 1800, "tape": 300, "vape": 300, "wood": 300, "cigar": 300, "cheese": 300}
usersettings = {}
donations = {}
antirob = {}
dead = {}
onmarket = {}
realestates = {"Store": 280000, "Property": 250000, "Bank": 435000, "Gas station": 140000, "Pharmacy": 365000}
userproperty = {}
activitycl = {}
global gway
gway = True
userlevel = {}
sentences = ["If you are getting an `Unhandled exception` or `Unhandled error` try installing **.Net** at **https://dotnet.microsoft.com/** if the problem resists, contact the support team for further support and investigation at your problem.", "There are *legit*, *rage* `configs` (`cfg`). You can **download** it, and put it in `.\Fedfigs` folder in `.\SteamLibrary\steamapps\common\Team Fortress 2`. Then run the *game* and inject the **cheat** using *any* injector, in the cheat menu, search for an icon positioned in the **top-right** part, and press it. There is a *label* named `Configs`, search the configs you put in the folder, *select* it and press `Load`. You just *loaded* a config.", "Go to the `Visuals` section in your cheat menu, then head to `Misc`. At the top-left of the panel, there is a dropdown with a label of *Removals*. Use the dropdown and select *Scope*, *Zoom*.", "To inject the cheat (.dll file), you can use a recommended injector: Xenos. Use this https://github.com/Tremzy/Xenos link, to download the injector and extract the 7zip file. Then run it as administrator, at the dropdown with a label of process, select the process named `hl2`. Then at the images section, press on the `Add` button. Search your cheat .dll file, then click on the `Inject` button. If you ran into any errors or exceptions, please report this to the support team, to fix your problem.", "If you encounter in a game crash error, clear your `./custom` folder in your TF2 files (usuall located at `C:\SteamLibrary\steamapps\common\Team Fortress 2\tf\custom`). If the error still resists, try install **.Net** at **https://dotnet.microsoft.com/**.", "You can use Luas for extra improvements for your cheats (e.g. custom Anti-aim, custom Visuals...). To use them, firstly you need to have a working Lua. Then you need go to your `.\Fedfigs` folder, that is located in your TF2 files (usually in `C:\SteamLibrary\steamapps\common\Team Fortress 2\Fedfigs`). Then search for a folder named `Lua`, and place your Lua file here. Then startup the game with the cheat injected, open your menu and enter the settings panel, and click on `Load lua`, then load your lua.", "You gain a higher rank in the hierarchy, and access to moderating tools (e.g. mute). And it also bypasses the cooldown for some commands.", "Go to `Hvh` in your cheat menu, at the top-left of the panel, search a section named `Tickbase-exploit`. Turn on the feature, then select the options and select the two option, `Wait for dt` and `No warp`. Then, you can customize your options as you like."]
userxp = {}
randsentcl = {}
economybanneds = []
activitybanneds = []
watchedusers = []
addroles = {"Steam": 1095082771787034744, "EA": 1095082797296795819, "Supercell": 1095082818280902656, "Facebook": 1095082842658197706, "Instagram": 1095082863164141700, "Tiktok": 1095082905983787008, "Youtube": 1095082927559286835, "Twitter": 1095082951521345656, "Reddit": 1095082972182491188, "Spotify": 1095082993942536293, "OBS": 1095083014654005429, "Riot Games": 1095083097369878730, "Bethesda": 1095083131440205825, "Unity": 1095083151518339072, "Roblox": 1095083175190995075, "Epic Games": 1095083203779375224, "Mojang": 1095083233122717846, "Rockstar Games": 1095083254916333691}
@bot.event
async def on_ready():
    memberschannel = bot.get_channel(1055981268845736046)
    cmdchannel = bot.get_channel(1105571851368927243)
    now = datetime.now()
    global current_time
    current_time = now.strftime("%D %H:%M:%S")
    print(f"Bot started with {Fore.LIGHTBLUE_EX}{bot.user}{Fore.RESET} ID |{Fore.LIGHTMAGENTA_EX} {current_time} {Fore.RESET}")
    await bot.change_presence(activity=discord.Activity(name = f"/help | Currently in {len(bot.guilds)} servers!", type=discord.ActivityType.watching))
#    added_users = []
#    for i in range(len(bot.get_guild(1075140354656981053).members)):
#        try:
#            added = await bot.get_guild(1075140354656981053).members[i].add_roles(bot.get_guild(1075140354656981053).get_role(1095252686791790712))
#            added_users.append(bot.get_guild(1075140354656981053).members[i])
#            print(f"Added role {added} to {bot.get_guild(1075140354656981053).members[i]}")
#        except Exception as err:
#                    cmdchannel = bot.get_channel(1105571851368927243)
#            await cmdchannel.send(f"Couldnt add roles to {bot.get_guild(1075140354656981053).members[i]}, error: {err}")
    try:
        await bot.tree.sync()
    except Exception as e:
        await cmdchannel.send("Commands failed to sync: {e}")
    bot.add_view(Help())

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id in voicebanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from `Voice`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await member.send(embed = embed)
        return
    if before.channel is None and after.channel is not None:
        privatevoice = discord.utils.get(member.guild.voice_channels, id=1105571554059894794)
        if after.channel == privatevoice:
            new_channel = await member.guild.create_voice_channel(name=f"{member}'s voice channel")
            cmdchannel = bot.get_channel(1105571851368927243)
            await cmdchannel.send(f"{member} created a channel")
            await member.move_to(new_channel)
    if before.channel is not None and after.channel is None:
        channel = before.channel
        if len(channel.members) == 0:
            if channel.name.endswith(f"voice channel"):
                await channel.delete()
                cmdchannel = bot.get_channel(1055981268845736046)
                await cmdchannel.send(f"{member} deleted his channel")
    if member.id in watchedusers:
        cmdchannel = bot.get_channel(1105571851368927243)
        if before.channel is None and after.channel is not None:
            await cmdchannel.send(f"**Watched user!** {member.mention} joined the {after.channel} voice channel.")
        else:
            await cmdchannel.send(f"**Watched user!** {member.mention} left the {before.channel} voice channel.")

@bot.event
async def on_member_join(user):
    memberschannel = bot.get_channel(1105777383673430056)
    await memberschannel.edit(name = 'Total members: {}'.format(memberschannel.guild.member_count))
    cmdchannel = bot.get_channel(1105571851368927243)
    await cmdchannel.send(f"{user} joined the server, total users {user.guild.member_count}")
    added = user.guild.get_role(1105572081334227074)
    await user.add_roles(added)
    await cmdchannel.send(f"Added {added} to user {user}")
    if user not in members_count:
        members_count.append(user)
    if len(members_count) > MAX_MEMBERS_PER_SECOND:
        await user.kick(reason="RAID DETECTED")
        await cmdchannel.send(f"{user} RAID DETECTED")
    await asyncio.sleep(10)
    members_count.clear()

@bot.event
async def on_member_remove(user):
    memberschannel = bot.get_channel(1105777383673430056)
    await memberschannel.edit(name = 'Total members: {}'.format(memberschannel.guild.member_count))
    cmdchannel = bot.get_channel(1105571851368927243)
    await cmdchannel.send(f"{user} left the server, total users {user.guild.member_count}")
@bot.event
async def on_channel_delete(channel):
    for log in await channel.guild.audit_logs(limit=10).flatten():
        if log.action == discord.AuditLogAction.channel_delete and log.target == channel:
            if log.user.id not in channelsdeleted:
                channelsdeleted[log.user.id] = 1
            else:
                channelsdeleted[log.user.id] += 1
            channeldelcd[log.user.id] = time.time()
            if time.time() - channeldelcd[log.user.id] < 10:
                await log.user.ban(reason="NUKE DETECTED")
            else:
                channeldelcd[log.user.id] = time.time()

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    """List all commands"""
    embed = discord.Embed(title = "Help", description = f"{interaction.user} there are the commands: \n \n - `/help` | This message \n - `/ping` | Shows the Bot's ping/latency \n", color=discord.Color.blue())
    await interaction.response.send_message(embed = embed)
@bot.tree.command(name="nitro")
async def nitro(interaction: discord.Interaction, amount: int):
    """Generate random nitro codes""" 
    premiumrole = interaction.user.guild.get_role(1105777909773373470)
    if premiumrole not in interaction.user.roles:
        if interaction.user.id in nitrocl and time.time() - nitrocl[interaction.user.id] < 120:
            embed = discord.Embed(title="Nitro", description=f"You have exceeded the time limit to use this command, time before you can use it again: **{120 - round(time.time() - nitrocl[interaction.user.id])} seconds** ", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            nitrocl[interaction.user.id] = time.time()
        else:
            if amount > 15:
                embed = discord.Embed(title = "Nitro", description = f"Invalid amount", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed) 
                return
            for i in range(amount):
                lower_case = "qwertzuiopasdfghjklyxycvbnm"
                upper_case = "QWERTZUIOPASDFGHJKLYXCVBNM"
                good = lower_case + upper_case + string.digits * 2
                length = 16
                code = "".join(random.sample(good, length))
                await interaction.user.send("https://discord.com/gifts/" + code)
            embed = discord.Embed(title = "Nitro", description = f"All nitro codes sent", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            nitrocl[interaction.user.id] = time.time()
    else:
        if amount > 15:
            embed = discord.Embed(title = "Nitro", description = f"Invalid amount", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            return
        for i in range(amount):
            lower_case = "qwertzuiopasdfghjklyxycvbnm"
            upper_case = "QWERTZUIOPASDFGHJKLYXCVBNM"
            good = lower_case + upper_case + string.digits * 2
            length = 16
            code = "".join(random.sample(good, length))
            await interaction.user.send("https://discord.com/gifts/" + code)
        embed = discord.Embed(title = "Nitro", description = f"All nitro codes sent", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    """Shows the bot ping"""
    cmdchannel = bot.get_channel(1105571851368927243)
    embed = discord.Embed(title = "Bot's ping", description = f"**Latency: {round(bot.latency * 1000)} ms**", color=discord.Color.blue())
    await interaction.response.send_message(embed = embed)
    await cmdchannel.send(f"{interaction.user} requested the ping of the bot")
@bot.tree.command(name="unban")
async def unban(interaction: discord.Interaction, user: discord.Member):
    """Unban a user"""
    if interaction.user.guild_permissions.ban_members:
        await interaction.user.guild.unban(user=user)
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} unbanned {user}")
        embed = discord.Embed(title = "Unban", description = f"**{user} has been unbanned**", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    else:
        await interaction.response.send_message(f"You dont have permissions to do this.")
@bot.tree.command(name="lock")
async def lock(interaction: discord.Interaction, time: int):
    """Locks the channel"""
    if interaction.user.guild_permissions.mute_members:
        await interaction.channel.set_permissions(interaction.user.guild.default_role, send_messages = False, view_channel = False)
        embed = discord.Embed(title = "Lock", description = f"Channel has been locked by {interaction.user.mention}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        await asyncio.sleep(time * 60)
        await interaction.channel.set_permissions(interaction.user.guild.default_role, send_messages = True, view_channel = False)
        embed = discord.Embed(title = "Unlock", description = f"Channel has been unlocked by {interaction.user.mention}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        await interaction.response.send_message(f"You dont have permissions to do this.")
@bot.tree.command(name="ban")
async def ban(interaction: discord.Interaction, user: discord.Member):
    """You can ban a user with this command"""
    if interaction.user.guild_permissions.ban_members:
        await interaction.guild.ban(user)
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} banned {user}")
        embed = discord.Embed(title = "Ban", description = f"**{user} has been banned**", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        await interaction.response.send_message(f"You dont have permissions to do this.")
@bot.tree.command(name="kick")
async def kick(interaction: discord.Interaction, user: discord.Member):
    """You can kick a user with this command"""
    if interaction.user.guild_permissions.kick_members:
        await interaction.guild.kick(user)
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} banned {user}")
        embed = discord.Embed(title = "Kick", description = f"**{user} has been kicked**", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        await interaction.response.send_message(f"You dont have permissions to do this.")
@bot.tree.command(name="work")
async def work(interaction: discord.Interaction):
            """Work and get money"""
            if interaction.user.id in economybanneds:
                embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
                return
            if interaction.user.id in workcl and time.time() - workcl[interaction.user.id] < COOLDOWN:
                embed = discord.Embed(title="Work", description=random.choice(cooldwnsays), color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
            else:
                moneygot = random.randint(0, 1500)
                if interaction.user.id not in money:
                    money[interaction.user.id] = 0
                money[interaction.user.id] += moneygot
                if moneygot == 0:
                    embed = discord.Embed(title="Work", description="You literally got nothing from work bruh 💀", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                else:
                    embed = discord.Embed(title="Work", description=f"You worked somewhere, and somehow got paid `{moneygot}$`", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                workcl[interaction.user.id] = time.time()

@bot.tree.command(name="tax")
@app_commands.choices(payorevade=[discord.app_commands.Choice(name="pay", value=1), discord.app_commands.Choice(name="evade", value=2)])
async def tax(interaction: discord.Interaction, payorevade: typing.Optional[discord.app_commands.Choice[int]]):
    """Check your taxes, pay it"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id not in money:
        money[interaction.user.id] = 0
    if interaction.user.id not in taxes:
        taxes[interaction.user.id] = 0
    if not payorevade:
        embed = discord.Embed(title="Tax", description=f"Taxes you have to pay: `{taxes[interaction.user.id]}$`\nTo pay your taxes use **/tax pay <amount/all>**", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if payorevade.value == 1:
            money[interaction.user.id] -= taxes[interaction.user.id]
            taxes[interaction.user.id] = 0
            embed = discord.Embed(title="Tax", description=f"You successfully paid `{taxes[interaction.user.id]}$` taxes", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        if payorevade.value == 2:
            if interaction.user.id in evadecl and time.time() - evadecl[interaction.user.id] < 84600:
                embed = discord.Embed(title="Tax-hacker", description="Okay i know im a hacker, but hey i need to rest too!", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
            else:
                global randomnum
                randomnum = random.randint(0, 100)
                global guess
                guess = random.randint(1, 99)
                embed = discord.Embed(title="Tax-hacker", description=f"I thinked a number between 0 and 100, try to guess if `{guess}` is higher or lower.", color=discord.Color.red())
                await interaction.response.send_message(embed = embed, view=Taxevade(), ephemeral=True)
                global taxgame
                taxgame = True 
                evadecl[interaction.user.id] = time.time()

class Taxevade(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label="Higher", style=discord.ButtonStyle.blurple)
    async def taxbtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if randomnum < guess:
            embed = discord.Embed(title="Tax-hacker", description=f"YES, YOU DID IT! You guessed it! I hacked into the government and set your tax to 0!", color=discord.Color.red())
            await interaction.response.send_message(embed = embed, ephemeral=True)
            taxes[interaction.user.id] = 0
            taxgame = False
            self.value = False
            self.stop()
        else:
            embed = discord.Embed(title="Tax-hacker", description=f"Well, that failed try next time...", color=discord.Color.red())
            await interaction.response.send_message(embed = embed, ephemeral=True)
            taxgame = False
            self.value = False
            self.stop()
    @discord.ui.button(label="Lower", style=discord.ButtonStyle.blurple)
    async def taxbtns(self, interaction: discord.Interaction, button: discord.ui.Button):
        if randomnum > guess:
            embed = discord.Embed(title="Tax-hacker", description=f"YES, YOU DID IT! You guessed it! I hacked into the government and set your tax to 0!", color=discord.Color.red())
            await interaction.response.send_message(embed = embed, ephemeral=True)
            taxes[interaction.user.id] = 0
            taxgame = False
            self.value = False
            self.stop()
        else:
            embed = discord.Embed(title="Tax-hacker", description=f"Well, that failed try next time...", color=discord.Color.red())
            await interaction.response.send_message(embed = embed, ephemeral=True)
            taxgame = False
            self.value = False
            self.stop()

@bot.tree.command(name="hunt")
async def hunt(interaction: discord.Interaction):
    """Go somewhere in a forest and shoot animals (you need a rifle)"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id in huntcl and time.time() - huntcl[interaction.user.id] < 30:
        embed = discord.Embed(title="Hunt", description=random.choice(cooldwnsays), color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if "Rifle" in inv[interaction.user.id]:
            if random.randint(0, 4) > 1:
                huntitems = ["Rabbit", "Deer", "Bear", "Cow", "Capybara", "Sheep"]
                currentitem = random.choice(huntitems)
                inv[interaction.user.id].append(currentitem)
                embed = discord.Embed(title="Hunt", description=f"You got into the woods and came back with a {currentitem}", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
            else:
                embed = discord.Embed(title="Hunt", description=f"You got to a cliff and waited for an animal, but they were on the other side", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed) 
        else:
            embed = discord.Embed(title="Hunt", description=f"You want a box fight with animals? First, get a rifle...", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    huntcl[interaction.user.id] = time.time()

@bot.tree.command(name="shop")
@app_commands.choices(buy=[discord.app_commands.Choice(name="Rifle", value=1),
    discord.app_commands.Choice(name="Gum", value=2),
    discord.app_commands.Choice(name="Shovel", value=3),
    discord.app_commands.Choice(name="Anti-rob pack", value=4),
    discord.app_commands.Choice(name="Fishing rod", value=5),
    discord.app_commands.Choice(name="Wallet expander", value=6),
    discord.app_commands.Choice(name="Phone", value=7),
    discord.app_commands.Choice(name="Pistol", value=8),
    discord.app_commands.Choice(name="Bread", value=9),
    discord.app_commands.Choice(name="Ammo", value=10),
    discord.app_commands.Choice(name="Monster", value=11),
    discord.app_commands.Choice(name="Pet food", value=12),
    discord.app_commands.Choice(name="Cheese", value=13),
    discord.app_commands.Choice(name="Hamburger", value=14),
    discord.app_commands.Choice(name="Pizza", value=15),
    discord.app_commands.Choice(name="Gyros", value=16),
    discord.app_commands.Choice(name="Taco", value=17),
    discord.app_commands.Choice(name="Pickaxe", value=18)])
async def shop(interaction: discord.Interaction, buy: typing.Optional[discord.app_commands.Choice[int]]):
    """View the shop, and buy items"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if not buy:
        itemsshop = "\n - ".join([f"{shopitem}: {price}" for shopitem, price in shopitems.items()])
        embed = discord.Embed(title="Shop", description=f"*You can buy these items (if you have money):* \n\n - {itemsshop}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if interaction.user.id not in money:
            embed = discord.Embed(title="Shop", description=f"What do you want to buy with no money? A life?", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            if buy.name in shopitems:
                price = shopitems[buy.name]
                if money[interaction.user.id] >= price:
                    if interaction.user.id not in inv:
                        inv[interaction.user.id] = []
                    inv[interaction.user.id].append(buy.name)
                    money[interaction.user.id] -= price
                    embed = discord.Embed(title="Shop", description=f"You bought a {buy.name} for `{price}$`", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                else:
                    embed = discord.Embed(title="Shop", description=f"At least get enough money to buy a {buy.name}", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
            else:
                embed = discord.Embed(title="Shop", description=f"What's '{buy.name}'? Cant really recognize... please type in again", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)  
@bot.tree.command(name="rob")
async def rob(interaction: discord.Interaction, user: discord.Member):
    """Rob a user, but you can get caught"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id in robcl and time.time() - robcl[interaction.user.id] < 3600:
        embed = discord.Embed(title="Rob", description=random.choice(cooldwnsays), color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if user:
            if user.id not in antirob or antirob[user.id] == False:      
                if random.randint(0, 2) > 1:
                    moneyget = random.randint(2000, 3000)
                    if interaction.user.id not in money:
                        money[interaction.user.id] = 0
                    if user not in money:
                        money[user] = 0
                    money[interaction.user.id] += moneyget
                    money[user] -= moneyget
                    embed = discord.Embed(title="Rob", description=f"{user.mention} Got robbed by {interaction.user.mention} for `{moneyget}$`, what a professional stealer!", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)  
                else:
                    if interaction.user.id not in money:
                        money[interaction.user.id] = 0
                    moneyget = random.randint(500, 1000)
                    money[interaction.user.id] -= moneyget
                    embed = discord.Embed(title="Rob", description=f"{interaction.user.mention} tried to rob {user.mention}, and what a surprise... he failed and lost `{moneyget}$`", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)  
            else:
                embed = discord.Embed(title="Rob", description=f"Sorry, but ur bro got an antirob on, try tomorrow", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)  
        else:
            embed = discord.Embed(title="Rob", description=f"Bro doesnt even know who he wants to rob 💀", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  
    robcl[interaction.user.id] = time.time()
@bot.tree.command(name="balance")
async def balance(interaction: discord.Interaction, user: typing.Optional[discord.Member]):
    """Check your balance, or others balance"""
    if user:
        if user.id in usersettings and usersettings[user.id]["Private Money"] == True:
            embed = discord.Embed(title="Balance", description=f"Sorry but i am not allowed to provide information about this user.", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            if user.id not in money:
                money[user.id] = 0
                embed = discord.Embed(title="Balance", description=f"{user.mention} is broke, he literally doesnt have a cent...", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)  
            else:
                embed = discord.Embed(title="Balance", description=f"{user.mention} has `{money[user.id]}$`", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)  
    else:
        if interaction.user.id not in money or money[interaction.user.id] == 0:
            money[interaction.user.id] = 0
            embed = discord.Embed(title="Balance", description=f"Why do you ask for something that doesnt exists? Ridiculous...", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  
        else:
            embed = discord.Embed(title="Balance", description=f"Sir, you have `{money[interaction.user.id]}$`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  

@bot.tree.command(name="settings")
@app_commands.choices(setting=[discord.app_commands.Choice(name="Private Money", value=1), discord.app_commands.Choice(name="Private Inv", value=2)])
async def balance(interaction: discord.Interaction, setting: typing.Optional[discord.app_commands.Choice[int]], setvalue: typing.Optional[bool]):
    """Check your settings and change them if you want"""
    if setting:
        if setvalue == None:
            if interaction.user.id in usersettings and setting.name in usersettings[interaction.user.id]:
                setvalue = usersettings[interaction.user.id][setting.name]
            embed = discord.Embed(title="Settings", description=f"The setting {setting.name} is {setvalue}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  
        else:
            if interaction.user.id not in usersettings:
                usersettings[interaction.user.id] = {}
            usersettings[interaction.user.id][setting.name] = setvalue
            embed = discord.Embed(title="Settings", description=f"Set `{setting.name}` to {setvalue} for {interaction.user.mention}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  
    else:
        embed = discord.Embed(title="Settings", description=f"", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
@bot.tree.command(name="donate")
async def donate(interaction: discord.Interaction, user: typing.Optional[discord.Member], amount: typing.Optional[int]):
    """Donate an amount to a user"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if not user and not amount:
        #donationslist = "".join([f"{interaction.user.name} to" + "".join([f" {user} for {amount}" for user, amount in donations.items()]) for user, donations in donations.items()])
        donationlist = ""
        for donor in donations:
            donationlist += f"\n -**{user}**"
            for donationed, donation in donations:
                donationlist += f"\n**\u00b7** {donationed}: {donation}"
        embed = discord.Embed(title="Donations", description=f"Last donations: \n - {donationlist}", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        if interaction.user.name not in donations:
            donations[interaction.user] = {}
            donations[interaction.user][user] = amount
        else:
            if user.name not in donations[interaction.user.name]:
                donations[interaction.user.name][user.name] = {}
            donations[interaction.user.name][user.name] += amount
        embed = discord.Embed(title="Donations", description=f"{interaction.user} donated to {user} for an amount of {amount}", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed, ephemeral=True)
@bot.tree.command(name="sell")
async def sell(interaction: discord.Interaction):
    """Sell items from your inventory"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id not in inv:
        inv[interaction.user.id] = []
        embed = discord.Embed(title="Sell", description=f"You cant sell 'nothing'", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed ,ephemeral=True)
    else:
        if inv[interaction.user.id] == []:
            embed = discord.Embed(title="Sell", description=f"You still cant sell 'nothing'", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed ,ephemeral=True)
        else:
            global moneyget
            moneyget = 0
            global sideinv
            sideinv = inv[interaction.user.id].copy()
            global saveinv
            saveinv = inv[interaction.user.id].copy()
            global itemsfound
            itemsfound = 0
            for i in inv[interaction.user.id]:
                if i in sellitems:
                    sideinv.remove(i)
                    itemsfound += 1
                    moneyget += sellitems[i]
            if itemsfound == 0:
                embed = discord.Embed(title="Sell", description=f"You have nothing to sell", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed ,ephemeral=True)
            else:
                embed = discord.Embed(title="Sell", description=f"You have **{itemsfound}** items to sell for `{moneyget}$`", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed, view=Sell() ,ephemeral=True)

class Sell(discord.ui.View):
    global sideinv
    global inv
    sideinv = None
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label="Sell", style=discord.ButtonStyle.blurple)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        global moneyget
        global sideinv
        global itemsfound
        global inv
        global saveinv
        if interaction.user.id not in money:
            money[interaction.user.id] = 0
        money[interaction.user.id] += moneyget
        inv[interaction.user.id] = sideinv
        sideinv = None
        embed = discord.Embed(title="Sell", description=f"You sold **{itemsfound}** items for `{moneyget}$`", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed, ephemeral=True)
        self.value = False
        self.stop()
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        global inv
        global sideinv
        sideinv = None
        self.value = False
        self.stop()
        embed = discord.Embed(title="Sell", description=f"You canceled the selling process.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed, ephemeral=True)
@bot.tree.command(name="crime")
async def crime(interaction: discord.Interaction):
    "Commit a very serious crime"
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id in crimecl and time.time() - crimecl[interaction.user.id] < COOLDOWN:
        embed = discord.Embed(title="Crime", description=random.choice(cooldwnsays), color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if random.randint(0, 4) > 1:
            moneygot = random.randint(800, 2000)
            if interaction.user.id not in money:
                money[interaction.user.id] = 0
            money[interaction.user.id] += moneygot
            embed = discord.Embed(title="Crime", description=f"You committed a very dangerous crime and made `{moneygot}$` from it", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            moneylose = random.randint(1500, 2000)
            if interaction.user.id not in money:
                    money[interaction.user.id] = 0
            money[interaction.user.id] -= moneylose
            embed = discord.Embed(title="Crime", description=f"You got caught and lost `{moneylose}$`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        crimecl[interaction.user.id] = time.time()
@bot.tree.command(name="mine")
async def mine(interaction: discord.Interaction):
    """Attempt to mine ores"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id in minecl and time.time() - minecl[interaction.user.id] < 30:
        embed = discord.Embed(title="Mine", description=random.choice(cooldwnsays), color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
            embed = discord.Embed(title="Mine", description=f"I think your hands aren't hard enough to break a stone... I recommend buying a pickaxe.", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            if "Pickaxe" in inv[interaction.user.id]:
                if random.randint(0, 6) > 1:
                    mineitems = ["Coal", "Ruby", "Iron", "Diamond", "Gold", "Silver", "Copper"]
                    amount = random.randint(1, 3)
                    item = random.choice(mineitems)
                    for x in range(amount):
                        inv[interaction.user.id].append(item)
                    embed = discord.Embed(title="Mine", description=f"You successfully found and mined `{item}x` `{item}`!", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                else:
                    embed = discord.Embed(title="Mine", description=f"Even a pickaxe could help on your problem, you still found nothing... Maybe get a flashlight or idk.", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
            else:
                embed = discord.Embed(title="Mine", description=f"You still dont have a pickaxe...", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed) 
    minecl[interaction.user.id] = time.time()
class Help(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Open ticket", custom_id="helpbtn", style=discord.ButtonStyle.blurple)
    async def helpbtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id not in usertickets:
            ticketnumber = random.randint(1,100)
            overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel = True),
            interaction.user.guild.get_role(1105572440874176582): discord.PermissionOverwrite(view_channel=True)
            }
            new_channel = await interaction.guild.create_text_channel(f"ticket-{ticketnumber}", overwrites=overwrites)
            embed = discord.Embed(title="Help", description=f"{interaction.user}, here you can request help, ask questions from the admin team.", color=discord.Color.blue())
            await new_channel.send(embed = embed)
            usertickets.append(interaction.user.id)
        else:
            await interaction.user.send("You have already opened a ticket")

@bot.tree.command(name="helpmessage")
async def helpmessage(interaction: discord.Interaction):
    """Just the help message"""
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title="Help", description=f'Click the button bellow to open a ticket, where moderators and admins try to answer/solve your question/problem.', color=discord.Color.blue())
        await interaction.channel.send(embed = embed, view=Help())
@bot.tree.command(name="dig")
async def dig(interaction: discord.Interaction):
    """Dig in the dirt"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id in digcl and time.time() - digcl[interaction.user.id] < 30:
        embed = discord.Embed(title="Dig", description=random.choice(cooldwnsays), color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
            embed = discord.Embed(title="Dig", description=f"The shovel isnt that expensive to buy...", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            if "Shovel" in inv[interaction.user.id]:
                if random.randint(0, 6) > 1:
                    digitems = ["Junk", "Stone", "Empty beer", "Treasure", "Steel", "Broken glass"]
                    amount = random.randint(1, 3)
                    item = random.choice(digitems)
                    for x in range(amount):
                        inv[interaction.user.id].append(item)
                    embed = discord.Embed(title="Dig", description=f"You digged very hard for an hour and found `{amount}` `{item}`.", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                else:
                    embed = discord.Embed(title="Dig", description=f"You literally thought that you can dig the asphalt", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
            else:
                embed = discord.Embed(title="Dig", description=f"You still dont have a shovel...", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed) 
    digcl[interaction.user.id] = time.time()

@bot.tree.command(name="use")
@app_commands.choices(item=[discord.app_commands.Choice(name="Treasure", value=1), discord.app_commands.Choice(name="Taco", value=2), discord.app_commands.Choice(name="Anti-rob pack", value=3),discord.app_commands.Choice(name="Redbull", value=4),discord.app_commands.Choice(name="Phone", value=5),discord.app_commands.Choice(name="Bread", value=6),discord.app_commands.Choice(name="Pistol", value=7),discord.app_commands.Choice(name="Gum", value=8),discord.app_commands.Choice(name="Monster", value=9),discord.app_commands.Choice(name="Cheese", value=10),discord.app_commands.Choice(name="Hamburger", value=11),discord.app_commands.Choice(name="Pizza", value=12),discord.app_commands.Choice(name="Gyros", value=13)])
async def use(interaction: discord.Interaction, item: discord.app_commands.Choice[int], user: typing.Optional[discord.Member]):
    """Use an item from your inventory"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if item.value == 1:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            tresitem = random.choice(shopitems)
            inv[interaction.user.id].append(tresitem)
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You unboxed your treasure and got a `{tresitem}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 2:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 3:
        if interaction.user.id not in antirob:
            antirob[interaction.user.id] = {}
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            antirob[interaction.user.id] = True
            embed = discord.Embed(title="Use", description=f"You activated your `{item.name}` for 24 hours", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            inv[interaction.user.id].remove(item.name)
            await asyncio.sleep(86400)
            antirob[interaction.user.id] = False
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 4:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have drinked a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 5:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            if not user:
                embed = discord.Embed(title="Use", description=f"You have to use the `user` parameter to specify the user", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
            else:
                embed = discord.Embed(title="Use", description=f"Calling {user}...", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
                for i in range(3):
                    await user.send(f"{user.mention}, {interaction.user.name} is calling you! Go to {interaction.channel.mention} in `{interaction.guild}`")
                    await asyncio.sleep(10)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 6:
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 7:
        if not user:
            embed = discord.Embed(title="Use", description=f"You have to use the `user` parameter to specify the user", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            if interaction.user.id in inv:
                if "Pistol" in inv[interaction.user.id]:
                    if random.randint(0, 3) > 1:
                        dead[user] = True
                        inv[interaction.user.id].remove(item.name)
                        embed = discord.Embed(title="Use", description=f"OMG, you just killed {user}! You bastard criminal! >:(", color=discord.Color.blue())
                        await interaction.response.send_message(embed = embed)
                    else:
                        embed = discord.Embed(title="Use", description=f"You successfully failed the assassination to {user}", color=discord.Color.blue())
                        await interaction.response.send_message(embed = embed)
                else:
                    embed = discord.Embed(title="Use", description=f"I dont think you could kill {user} without a pistol...", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
            else:
                embed = discord.Embed(title="Use", description=f"I dont think you could kill {user} without a pistol...", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
    if item.value == 8:                    
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 9:                    
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 10:                    
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 11:                    
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 12:                    
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    if item.value == 13:                    
        if interaction.user.id not in inv:
            inv[interaction.user.id] = []
        if item.name in inv[interaction.user.id]:
            inv[interaction.user.id].remove(item.name)
            embed = discord.Embed(title="Use", description=f"You have eaten a `{item.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Use", description=f"You dont have a {item.name}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)

class TradeDropdown(discord.ui.Select):
    def __init__(self, items):
        options=[
            discord.SelectOption(label=item) for item in items
        ]
        super().__init__(placeholder="Select an item...", options=options, min_values=1, max_values=1)
    async def callback(self, interaction: discord.Interaction):
        items2 = inv[usertotrade.id]
        global tradeitem1
        tradeitem1 = self.values[0]
        await interaction.response.send_message(f"Create trade offer... From {usertotrade}'s inventory: ", view=TradeView2(items2), ephemeral=True)

class TradeDropdown2(discord.ui.Select):
    def __init__(self, items):
        options=[
            discord.SelectOption(label=item) for item in items
        ]
        super().__init__(placeholder="Select an item...", options=options, min_values=1, max_values=1)
    async def callback(self, interaction: discord.Interaction):
        global tradeitem2
        tradeitem2 = self.values[0]
        await interaction.user.send(f"You've send a trade offer to {interaction.user}. You offered a trade with a {tradeitem1} for his {tradeitem2}")
        await usertotrade.send(f"{interaction.user} wants to trade with you. He wants to trade your {tradeitem2}, for his {tradeitem1}.", view=TradeView3())
class TradeView3(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
    @discord.ui.button(label="Accept",custom_id="tradebtn" + str(random.randint(0, 100)), style=discord.ButtonStyle.blurple)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        await trader.send(f"{usertotrade} **accepted** the trade offer you sent previously")
        await interaction.user.send(f"You **accepted** {trader}'s trade offer")
        inv[trader.id].append(tradeitem2)
        inv[trader.id].remove(tradeitem1)
        inv[interaction.user.id].append(tradeitem1)
        inv[interaction.user.id].remove(tradeitem2)
        self.value = False
        self.stop()
    @discord.ui.button(label="Decline",custom_id="tradebtn" + str(random.randint(0, 100)), style=discord.ButtonStyle.danger)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        await trader.send(f"{usertotrade} **canceled** the trade offer you sent previously")
        await interaction.user.send(f"You **canceled** {trader}'s trade offer")
        self.value = False
        self.stop()

class TradeView2(discord.ui.View):
    def __init__(self, items):
        super().__init__()
        self.add_item(TradeDropdown2(items))

class TradeView(discord.ui.View):
    def __init__(self, items):
        super().__init__()
        self.add_item(TradeDropdown(items))

@bot.tree.command(name="trade")
async def trade(interaction: discord.Interaction, user: discord.Member):
    """Trade with a user"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    items = inv[interaction.user.id]
    global trader
    trader = interaction.user
    global usertotrade
    usertotrade = user
    await interaction.response.send_message(f"Create trade offer... From your inventory: ", view=TradeView(items), ephemeral=True)

class PutOnMarket(discord.ui.Select):
    def __init__(self, items):
        options=[]
        i = 1
        for item in items:
            item += " (" + str(i) + ")"
            options.append(discord.SelectOption(label=item))
            i += 1
        super().__init__(placeholder="Select an item...", options=options, min_values=1, max_values=1)
    async def callback(self, interaction: discord.Interaction):
        selecteditem = self.values[0]
        splitted = selecteditem.split(" ")
        inv[interaction.user.id].remove(splitted[0])
        if interaction.user not in onmarket:
            onmarket[interaction.user] = {}
        onmarket[interaction.user][splitted[0]] = pricetosellfor
        await interaction.response.send_message(f"You put a `{splitted[0]}` on the market for `{pricetosellfor}$`", ephemeral=True)

class MarketView(discord.ui.View):
    def __init__(self, items):
        super().__init__()
        self.add_item(PutOnMarket(items))

@bot.tree.command(name="market")
@app_commands.choices(buyorsell=[discord.app_commands.Choice(name="Sell", value=1), discord.app_commands.Choice(name="Buy", value=2)])
async def market(interaction: discord.Interaction, buyorsell: typing.Optional[discord.app_commands.Choice[int]], price: typing.Optional[int]):
    """You can just simply view the community market, or buy/sell items"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if buyorsell:
        if buyorsell.value == 1:
            items = inv[interaction.user.id]
            global pricetosellfor
            pricetosellfor = price
            await interaction.response.send_message(f"What do you want to put on market?", view=MarketView(items), ephemeral=True)
    else:
        market_list = ""
        #market_list = "\n".join([f"- {seller}:" for seller in onmarket.items()])
        for seller, item in onmarket.items():
            market_list += f"\n -**{seller}**:"
            for item, price in item.items():
                market_list += f"\n**\u00b7** {item}: {price}$"
        embed = discord.Embed(title = "Market", description = f"Current market: \n {market_list}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed, ephemeral=True)
class Realestate(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
    @discord.ui.button(label="Yes, sell it", custom_id="randombtn" + str(random.randint(0, 100)), style=discord.ButtonStyle.blurple)
    async def yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        userproperty[interaction.user.id].remove(propertytosell)
        amount = realestates[propertytosell] / 100 * 75
        money[interaction.user.id] + amount
        embed = discord.Embed(title = "Real estate - Sell", description = f"You successfully sold `{propertytosell}` for `{amount}$`", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed, ephemeral=True)
    @discord.ui.button(label="No, i'll keep it", custom_id="randombtn" + str(random.randint(0, 100)), style=discord.ButtonStyle.danger)
    async def no(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(title = "Real estate - Sell", description = f"You canceled the selling of your `{propertytosell}`", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed, ephemeral=True)

@bot.tree.command(name="realestate")
@app_commands.choices(type=[discord.app_commands.Choice(name="Store", value=1), discord.app_commands.Choice(name="Property", value=2), discord.app_commands.Choice(name="Bank", value=3), discord.app_commands.Choice(name="Gas station", value=4), discord.app_commands.Choice(name="Pharmacy", value=5)])
@app_commands.choices(buyorsell=[discord.app_commands.Choice(name="Buy", value=1), discord.app_commands.Choice(name="Sell", value=2)])
async def property(interaction: discord.Interaction, buyorsell: typing.Optional[discord.app_commands.Choice[int]], type: typing.Optional[discord.app_commands.Choice[int]]):
    """Buy or sell propertys, houses, stores..."""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if buyorsell:
        if buyorsell.value == 1:
            if interaction.user.id not in money:
                money[interaction.user.id] = 0
            money[interaction.user.id] -= realestates[type.name]
            if interaction.user.id not in userproperty:
                userproperty[interaction.user.id] = []
            userproperty[interaction.user.id].append(type.name)
            embed = discord.Embed(title="Real estate - Buy", description=f"You successfully bought a `{type.name}` for `{realestates[type.name]}$`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            global propertytosell
            propertytosell = type.name
            embed = discord.Embed(title="Real estate - Buy", description=f"Are you sure you want to sell `{type.name}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed, view=Realestate(), ephemeral=True)  
    else:
        propertys = "\n - ".join(map(str, userproperty[interaction.user.id]))
        embed = discord.Embed(title="Real estate - View", description=f"**- {propertys}**", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)  
@bot.tree.command(name="addmoney")
async def addmoney(interaction: discord.Interaction, user: discord.Member, amount: int):
    """Add money to a user"""
    if interaction.user.guild_permissions.administrator:
        if user.id not in money:
            money[user.id] = 0
        money[user.id] += amount
        await interaction.response.send_message(f"Added `{amount}` to {user.mention}. Current money: {money[user.id]}")
@bot.tree.command(name="additem")
@app_commands.choices(item=[discord.app_commands.Choice(name="wood", value=1), discord.app_commands.Choice(name="cigar", value=2),discord.app_commands.Choice(name="cheese", value=3),discord.app_commands.Choice(name="tape", value=4),discord.app_commands.Choice(name="Treasure", value=5),discord.app_commands.Choice(name="Rifle", value=6),discord.app_commands.Choice(name="Ammo", value=7),discord.app_commands.Choice(name="Fishing rod", value=8),discord.app_commands.Choice(name="Phone", value=9),discord.app_commands.Choice(name="Pistol", value=10),discord.app_commands.Choice(name="Pickaxe", value=11),discord.app_commands.Choice(name="Shovel", value=12)])
async def additem(interaction: discord.Interaction, user: discord.Member, item: app_commands.Choice[int], amount: int):
    """Add item to a user"""
    if interaction.user.guild_permissions.administrator:
        if user.id not in inv:
            inv[user.id] = []
        for i in range(amount):
            inv[user.id].append(item.name)
        await interaction.response.send_message(f"Added `{item.name}` to {user.mention}. Current inventory: {inv[user.id]}")
@bot.tree.command(name="trash")
async def trash(interaction: discord.Interaction):
    """Search a trash can"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if interaction.user.id in trashcl and time.time() - trashcl[interaction.user.id] < COOLDOWN:
        embed = discord.Embed(title="Trash", description=random.choice(cooldwnsays), color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if random.randint(0, 5) > 1:
            trash = ["tape", "vape", "wood", "cigar", "cheese"]
            if interaction.user.id not in inv:
                inv[interaction.user.id] = []
            item = random.choice(trash)
            inv[interaction.user.id].append(item)
            embed = discord.Embed(title="Trash", description=f"You actually found a {item} in the trash can lmao", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title="Trash", description=f"Imagine failing a trash can search mission 💀", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    trashcl[interaction.user.id] = time.time()

@bot.tree.command(name="inventory")
async def inventory(interaction: discord.Interaction, user: typing.Optional[discord.Member]):
    """Request your, or others inventory"""
    if interaction.user.id in economybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Economy system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if user:
        if user.id in usersettings and usersettings[user.id]["Private Inv"] == True:
            embed = discord.Embed(title="Inventory", description=f"Sorry but i am not allowed to provide information about this user.", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            if user.id not in inv:
                inv[user.id] = []
                embed = discord.Embed(title="Inventory", description=f"This man doesnt even have a rotted gum...", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
            else:
                userinv = "\n - ".join(map(str, inv[user.id]))
                embed = discord.Embed(title="Inventory", description=f"{user.mention}'s inventory:\n - {userinv}", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
    else:
        if interaction.user.id in inv:
            userinv = "\n - ".join(map(str, inv[interaction.user.id]))
            embed = discord.Embed(title="Inventory", description=f"Your backpack is containing this:\n - {userinv}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            inv[interaction.user.id] = []
            embed = discord.Embed(title="Inventory", description=f"What you searching for? Its empty...", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed) 

@bot.tree.command(name="version")
async def version(interaction: discord.Interaction):
    """Shows the bot version, language, prog language"""
    cmdchannel = bot.get_channel(1105571851368927243)
    await cmdchannel.send(f"{interaction.user} requested the bots version")
    embed = discord.Embed(title="Version", description=f"Bot version: 1.4 | Language: English | Prog. Lang.: Python", color=discord.Color.blue())
    await interaction.response.send_message(embed = embed)
@bot.tree.command(name="activity")
async def activity(interaction: discord.Interaction, type: discord.ActivityType, name: str):
    """Change the activity of the bot"""
    premiumrole = interaction.user.guild.get_role(1105777909773373470)
    if interaction.user.id in activitybanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Activity change`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    if premiumrole not in interaction.user.roles:
        if interaction.user.id in activitycl and time.time() - activitycl[interaction.user.id] < 300:
            embed = discord.Embed(title="Activity", description=f"You have exceeded the time limit to use this command, time before you can use it again: **{300 - round(time.time() - activitycl[interaction.user.id])} seconds** ", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            activitycl[interaction.user.id] = time.time()
        else:
            try: 
                await bot.change_presence(activity=discord.Activity(name = name, type=type))
                cmdchannel = bot.get_channel(1105571851368927243)
                await cmdchannel.send(f"{interaction.user} changed the bots activity to type: `{type}` with a name of: `{name}`")
                embed = discord.Embed(title="Activity", description=f"Activity successfully changed to {type.name}, {name}", color=discord.Color.blue())
                await interaction.response.send_message(embed=embed)
            except Exception as error:
                embed = discord.Embed(title="Activity", description=f"An error occured: {error}", color=discord.Color.blue())
                await interaction.response.send_message(embed=embed) 
            activitycl[interaction.user.id] = time.time()
    else:
        try: 
            await bot.change_presence(activity=discord.Activity(name = name, type=type))
            cmdchannel = bot.get_channel(1105571851368927243)
            await cmdchannel.send(f"{interaction.user} changed the bots activity to type: `{type}` with a name of: `{name}`")
            embed = discord.Embed(title="Activity", description=f"Activity successfully changed to {type.name}, {name}", color=discord.Color.blue())
            await interaction.response.send_message(embed=embed)
        except Exception as error:
            embed = discord.Embed(title="Activity", description=f"An error occured: {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed=embed) 
@bot.tree.command(name="comban")
@app_commands.choices(type=[discord.app_commands.Choice(name="Report ban", value=1), discord.app_commands.Choice(name="Activity change ban", value=2), discord.app_commands.Choice(name="Economy ban", value=3), discord.app_commands.Choice(name="Voice ban", value=4)])
async def comban(interaction: discord.Interaction, type: discord.app_commands.Choice[int], user: discord.Member, reason: typing.Optional[str]):
    """Community ban a member"""
    if interaction.user.guild_permissions.ban_members:
        if type.value == 1:
            reportbanneds.append(user.id)
            embed = discord.Embed(title="Community ban", description=f'{user.mention} has been banned from reporting', color=discord.Color.blue())
            await interaction.channel.send(embed = embed)
        elif type.value == 2:
            activitybanneds.append(user.id)
            embed = discord.Embed(title="Community ban", description=f'{user.mention} has been banned from bot activity changing', color=discord.Color.blue())
            await interaction.channel.send(embed = embed)
        elif type.value == 3:
            economybanneds.append(user.id)
            embed = discord.Embed(title="Community ban", description=f'{user.mention} has been banned from the entire economy system', color=discord.Color.blue())
            await interaction.channel.send(embed = embed)
        elif type.value == 4:
            voicebanneds.append(user.id)
            embed = discord.Embed(title="Community ban", description=f'{user.mention} has been banned from voice', color=discord.Color.blue())
            await interaction.channel.send(embed = embed)
    else:
        embed = discord.Embed(title="Community ban", description=f'You dont have permission to use this command', color=discord.Color.blue())
        await interaction.channel.send(embed = embed)

class Giveaway(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Join", custom_id="giveawaybtn", style=discord.ButtonStyle.blurple)
    async def giveawaybtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        if gway == True:
            if interaction.user not in userentries:
                userentries.append(interaction.user)
                await interaction.response.send_message("You successfully joined the giveaway", ephemeral=True)
            else:
                await interaction.response.send_message("You already joined this giveaway", ephemeral=True)

@bot.tree.command(name="giveaway")
async def giveaway(interaction: discord.Interaction, item: str, time: int, winners: int):
    """Host a giveaway"""
    if interaction.guild.get_role(1105779115388305459) in interaction.user.roles or interaction.user.top_role > interaction.guild.get_role(1105779115388305459):
        embed = discord.Embed(title="Giveaway", description=f"**{item}**", color=discord.Color.blue())
        embed.add_field(name="Winners", value=f"Users who can win: {winners}")
        embed.add_field(name="Time before the giveaway ends", value=f"{time} minutes")
        await interaction.response.send_message(embed=embed, view=Giveaway())
        gway = True
        await asyncio.sleep(time * 60)
        gwinners = []
        for i in range(winners):
            gwinners.append(random.choice(userentries))        
        embed = discord.Embed(title="Giveaway", description=f"**The winners are:**", color=discord.Color.blue())
        gwinnersj = "\n - ".join(map(str, gwinners))
        embed.add_field(name="", value=f"\n - {gwinnersj}")
        await interaction.channel.send(embed=embed)
        gway = False
        userentries.clear()
@bot.tree.command(name="entries")
async def entries(interaction: discord.Interaction):
    """View the entires in the giveaway"""
    if giveaway:
        embed = discord.Embed(title="Giveaway", description=f"The entries in the giveaway: \n ", color=discord.Color.blue())
        embed.add_field(name="", value="\n".join(map(str, userentries)))
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="Giveaway", description=f"There aren't any giveaways right now, try again later", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
@bot.tree.command(name="clear")
async def clear(interaction: discord.Interaction, amount: int):
    """Clear chat messages"""
    if not interaction.user.guild_permissions.manage_messages:
        embed = discord.Embed(title="Clear", description=f"You dont have permission to do this.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        await interaction.channel.purge(limit=amount)
        embed = discord.Embed(title="Clear", description=f"{interaction.user.mention} just cleared the chat with {amount} messages.", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} cleard {amount} messages in {interaction.channel}")
@bot.tree.command(name="giveall")
async def giveall(interaction: discord.Interaction, role: discord.Role):
    """Give all users a specified role"""
    if interaction.user.guild_permissions.administrator:
        timesaddedtousers = 0
        for i in range(len(interaction.guild.members)):
            if role not in interaction.guild.members[i].roles:
                if interaction.guild.members[i] == bot.user:
                    pass
                else:
                    timesaddedtousers += 1
                    await interaction.guild.members[i].add_roles(role)
        embed = discord.Embed(title="Giveall", description=f"Successfully given the **{role}** role to **{timesaddedtousers}** users.", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="Giveall", description=f"You dont have permission to use this command", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
@bot.tree.command(name="fish")
async def fish(interaction: discord.Interaction):
    """Catch fishes and sell them"""
    if interaction.user.id not in inv:
        embed = discord.Embed(title="Fish", description=f"You are not a bear to catch fishes with your bare hands", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
    else:
        if "Fishing rod" not in inv[interaction.user.id]:
            embed = discord.Embed(title="Fish", description=f"You are not a bear to catch fishes with your bare hands", color=discord.Color.blue())
            await interaction.response.send_message(embed=embed)
        else:
            if random.randint(0, 6) > 1:
                inv[interaction.user.id].append("Fish")
                embed = discord.Embed(title="Fish", description=f"You were patient and catched a fish!", color=discord.Color.blue())
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(title="Fish", description=f"You tried waiting for anyone but no one came to the party... :(", color=discord.Color.blue())
                await interaction.response.send_message(embed=embed)
@bot.tree.command(name="saysomething")
async def saysomething(interaction: discord.Interaction):
    premiumrole = interaction.user.guild.get_role(1105777909773373470)
    if premiumrole not in interaction.user.roles:
        if interaction.user.id in randsentcl and time.time() - randsentcl[interaction.user.id] < 300:
            embed = discord.Embed(title="Activity", description=f"You have exceeded the time limit to use this command, time before you can use it again: **{300 - round(time.time() - randsentcl[interaction.user.id])} seconds** ", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            randsentcl[interaction.user.id] = time.time()
        else:
            response = requests.get("https://api.quotable.io/random")
            data = json.loads(response.text)
            embed = discord.Embed(title="Random sentences", description=f"{data['content']}", color=discord.Color.blue())
            await interaction.response.send_message(embed=embed)
            randsentcl[interaction.user.id] = time.time()
    else:
        response = requests.get("https://api.quotable.io/random")
        data = json.loads(response.text)
        embed = discord.Embed(title="Random sentences", description=f"{data['content']}", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
@bot.tree.command(name="report")
@app_commands.choices(type=[discord.app_commands.Choice(name="Harrassment", value=1), discord.app_commands.Choice(name="Bullying", value=2), discord.app_commands.Choice(name="Scamming", value=3), discord.app_commands.Choice(name="Promotion in private", value=4), discord.app_commands.Choice(name="Spamming", value=5), discord.app_commands.Choice(name="Pedophile behaviour", value=6)])
async def report(interaction: discord.Interaction, user: discord.Member, type: discord.app_commands.Choice[int], reason: str):
    """Report a user for breaking the roles"""
    if interaction.user.id in reportbanneds:
        embed = discord.Embed(title="Community ban", description=f"You have been banned from the `Report system`, if you want to submit an appeal, open a ticket.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        return
    reportnumber = random.randint(1,100)
    overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.guild.get_role(1105572440874176582): discord.PermissionOverwrite(view_channel = True)
    }
    reportchannel = await interaction.guild.create_text_channel(f"report_case-{reportnumber}", overwrites=overwrites)
    embed = discord.Embed(title="Report", description=f"You send a report to the admin team. The reported person: {user.mention} | The report type: `{str(type.name)}` | The reason: `{reason}`.", color=discord.Color.blue())
    await interaction.response.send_message(embed=embed)
    embed = discord.Embed(title="Report", description=f"{interaction.user.mention} reported {user.mention} for a type of `{str(type.name)}` with a reason of `{reason}`.", color=discord.Color.blue())
    await reportchannel.send(embed = embed)
@bot.tree.command(name="addrole")
@app_commands.choices(role=[discord.app_commands.Choice(name="Steam", value = 1), discord.app_commands.Choice(name="EA", value = 2), discord.app_commands.Choice(name="Supercell", value = 3), discord.app_commands.Choice(name="Facebook", value = 4), discord.app_commands.Choice(name="Instagram", value = 5), discord.app_commands.Choice(name="Tiktok", value = 6), discord.app_commands.Choice(name="Youtube", value = 7), discord.app_commands.Choice(name="Twitter", value = 8), discord.app_commands.Choice(name="Reddit", value = 9), discord.app_commands.Choice(name="Spotify", value = 10), discord.app_commands.Choice(name="OBS", value = 11), discord.app_commands.Choice(name="Riot Games", value = 12), discord.app_commands.Choice(name="Bethesda", value = 13), discord.app_commands.Choice(name="Unity", value = 14), discord.app_commands.Choice(name="Roblox", value = 15), discord.app_commands.Choice(name="Epic Games", value = 16), discord.app_commands.Choice(name="Mojang", value = 17), discord.app_commands.Choice(name="Rockstar Games", value = 18), discord.app_commands.Choice(name="Server Notification", value = 19), discord.app_commands.Choice(name="Script Notification", value = 20), discord.app_commands.Choice(name="Post Notification", value = 21) ])
async def addrole(interaction: discord.Interaction, role: discord.app_commands.Choice[int]):
    """Get a role for yourself"""
    try:
        await interaction.user.add_roles(interaction.user.guild.get_role(addroles[role.name]))
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} added the role {role} to himself")
        embed = discord.Embed(title="Addrole", description=f"You successfully added the `{str(role.name)}` role to yourself", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    except Exception as err:
        embed = discord.Embed(title="Addrole", description=f"There was an error adding a role to you: {err}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        raise err
@bot.tree.command(name="removerole")
@app_commands.choices(role=[discord.app_commands.Choice(name="Steam", value = 1), discord.app_commands.Choice(name="EA", value = 2), discord.app_commands.Choice(name="Supercell", value = 3), discord.app_commands.Choice(name="Facebook", value = 4), discord.app_commands.Choice(name="Instagram", value = 5), discord.app_commands.Choice(name="Tiktok", value = 6), discord.app_commands.Choice(name="Youtube", value = 7), discord.app_commands.Choice(name="Twitter", value = 8), discord.app_commands.Choice(name="Reddit", value = 9), discord.app_commands.Choice(name="Spotify", value = 10), discord.app_commands.Choice(name="OBS", value = 11), discord.app_commands.Choice(name="Riot Games", value = 12), discord.app_commands.Choice(name="Bethesda", value = 13), discord.app_commands.Choice(name="Unity", value = 14), discord.app_commands.Choice(name="Roblox", value = 15), discord.app_commands.Choice(name="Epic Games", value = 16), discord.app_commands.Choice(name="Mojang", value = 17), discord.app_commands.Choice(name="Rockstar Games", value = 18), discord.app_commands.Choice(name="Server Notification", value = 19), discord.app_commands.Choice(name="Script Notification", value = 20), discord.app_commands.Choice(name="Post Notification", value = 21) ])
async def addrole(interaction: discord.Interaction, role: discord.app_commands.Choice[int]):
    """Remove a role from yourself"""
    try:
        await interaction.user.remove_roles(interaction.user.guild.get_role(addroles[role.name]))
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} removed the role {role} from himself")
        embed = discord.Embed(title="Remove role", description=f"You successfully removed the `{str(role.name)}` role from yourself", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    except Exception as err:
        embed = discord.Embed(title="Remove role", description=f"There was an error removing a role from you: {err}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)  
        raise err
@bot.tree.command(name="math")
@app_commands.choices(type=[discord.app_commands.Choice(name="Summation", value=1), discord.app_commands.Choice(name="Subtraction", value=2), discord.app_commands.Choice(name="Multiplication", value=3), discord.app_commands.Choice(name="Root", value=4), discord.app_commands.Choice(name="Log", value=5), discord.app_commands.Choice(name="Percentage", value=6), discord.app_commands.Choice(name="Division", value=7)])
async def maths(interaction: discord.Interaction, type: discord.app_commands.Choice[int], number1: typing.Optional[float], number2: typing.Optional[float]):
    """Do any calculation"""
    result = None
    if type.value == 1:
        try:        
            result = number1 +  number2
            embed = discord.Embed(title="Math - Summation", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Summation", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif type.value == 2:
        try:        
            result = number1 - number2
            embed = discord.Embed(title="Math - Subtraction", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Subtraction", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif type.value == 3:
        try:        
            result = number1 * number2
            embed = discord.Embed(title="Math - Multiplication", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Multiplication", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif type.value == 4:
        try:        
            result = math.sqrt(number1)
            embed = discord.Embed(title="Math - Square root", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Square root", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif type.value == 5:
        try:        
            result = math.log10(number1)
            embed = discord.Embed(title="Math - Logarithm x 10", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Logarithm x 10", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif type.value == 6:
        try:        
            result = number1 * number2 / 100
            embed = discord.Embed(title="Math - Percentage", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Percentage", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif type.value == 7:
        try:        
            result = number1 / number2
            embed = discord.Embed(title="Math - Division", description=f"Your result is: `{result}`", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        except Exception as error:
            embed = discord.Embed(title="Math - Division", description=f"An error occured! {error}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            cmdchannel = bot.get_channel(1105571851368927243)
    await cmdchannel.send(f"{interaction.user} used the math command | type: {type.name}, first number: {number1}, second number: {number2}, result: {result}")
@bot.tree.command(name="encode")
@app_commands.choices(type=[discord.app_commands.Choice(name="Base64", value=1)])
async def encode(interaction: discord.Interaction, type: discord.app_commands.Choice[int], text: str):
    """Encode texts"""
    if type.value == 1:
        encodedms = base64.b64encode(text.encode('utf-8'))
        embed = discord.Embed(title = "Encode - Base64", description = f"Your encoded message from `utf-8` to `base64`: \n - {encodedms}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} encoded {text} to {type}")
@bot.tree.command(name="mute")
async def mute(interaction: discord.Interaction, user: discord.Member, timetomute: int):
    """Mute a user for a given time"""
    premiumrole = interaction.user.guild.get_role(1105777909773373470)
    if interaction.user.guild_permissions.mute_members:
        if interaction.user.top_role > user.top_role:
            await user.add_roles(user.guild.get_role(1105779570411569172))
            channel = interaction.channel
            embed = discord.Embed(title = "Mute", description = f"**{user} has been muted for {int(timetomute)} minutes by {interaction.user}.**", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
            print(f"Message sent to {Fore.LIGHTBLUE_EX}{interaction.channel}{Fore.RESET} | {Fore.LIGHTMAGENTA_EX}{current_time}{Fore.RESET}")
            cmdchannel = bot.get_channel(1105571851368927243)
            await cmdchannel.send(f"{interaction.user} muted {user} for {timetomute} minutes")
            await asyncio.sleep(timetomute * 60)
            await user.remove_roles(user.guild.get_role(1105779570411569172))
            embed = discord.Embed(title = "Mute", description = f"**{user} has been unmuted.**", color=discord.Color.blue())
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(title = "Mute", description = f"You dont have permission to mute this member", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    elif premiumrole in interaction.user.roles:
        if timetomute > 5:
            embed = discord.Embed(title = "Mute", description = f"You cannot mute someone over 5 minutes", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed, ephemeral=True)
        else:
            if interaction.user.top_role > user.top_role:
                if interaction.user.id in mutecl and time.time() - mutecl[interaction.user.id] < 1800:
                    embed = discord.Embed(title="Mute", description=f"You have exceeded the time limit to use this command, time before you can use it again: **{1800 - round(time.time() - mutecl[interaction.user.id])} seconds** ", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                    mutecl[interaction.user.id] = time.time()
                else:
                    mutecl[interaction.user.id] = time.time()
                    await user.add_roles(user.guild.get_role(1105779570411569172))
                    channel = interaction.channel
                    embed = discord.Embed(title = "Mute", description = f"**{user} has been muted for {int(timetomute)} minutes by {interaction.user}.**", color=discord.Color.blue())
                    await interaction.response.send_message(embed = embed)
                    print(f"Message sent to {Fore.LIGHTBLUE_EX}{interaction.channel}{Fore.RESET} | {Fore.LIGHTMAGENTA_EX}{current_time}{Fore.RESET}")
                    cmdchannel = bot.get_channel(1105571851368927243)
                    await cmdchannel.send(f"{interaction.user} muted {user} for {timetomute} minutes")
                    await asyncio.sleep(timetomute * 60)
                    await user.remove_roles(user.guild.get_role(1105779570411569172))
                    embed = discord.Embed(title = "Mute", description = f"**{user} has been unmuted.**", color=discord.Color.blue())
                    await channel.send(embed = embed)
            else:
                embed = discord.Embed(title = "Mute", description = f"You dont have permission to mute this member", color=discord.Color.blue())
                await interaction.response.send_message(embed = embed)
    else:
        # If the person does not have the "ban members" permission, send an error message
        await interaction.response.send_message('You do not have permission to use this command')
        log = open("botlog.txt", "a",  encoding="utf8")
        log.write(f"{interaction.user} attempted to use command 'mute' | {current_time} \n")
        log.close()
        print(f"Message sent to {Fore.LIGHTBLUE_EX}{interaction.channel}{Fore.RESET} | {Fore.LIGHTMAGENTA_EX}{current_time} {Fore.RESET}")
@bot.tree.command(name="whois")
async def whois(interaction: discord.Interaction, user: discord.Member):
    """Display every information about a user"""
    if interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message(f"All information about {user}: \n ** - Name: {user.name} \n - Nickname: {user.nick} \n - Discriminator: {user.discriminator} \n - Accent color: {user.accent_color} \n - Activity: {user.activities} \n - Avatar: {user.avatar} \n - Bot: {user.bot} \n - Banner: {user.banner} \n - Icon: {user.display_icon} \n - Status: {user.desktop_status} \n - Permissions: **https://discordapi.com/permissions.html#{user.guild_permissions.value} \n - On mobile: {user.is_on_mobile()} \n - Id: {user.id} \n - Joined at: {user.joined_at} \n - Is timed out: {user.is_timed_out()} \n - Mutual guilds: {user.mutual_guilds} \n - Pending: {user.pending} \n - Voice: {user.voice} \n - Guild avatar: {user.guild_avatar} \n - Mobile status: {user.mobile_status} \n - Premium since: {user.premium_since} \n - Roles: {user.roles}**")
@bot.tree.command(name="close")
async def close(interaction: discord.Interaction):
    """Delete ticket channels"""
    if interaction.channel.name.startswith("ticket"):
        await interaction.channel.delete()
        if interaction.user.id in usertickets:
            usertickets.remove(interaction.user.id)
@bot.tree.command(name="unmute")
async def unmute(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.guild_permissions.mute_members:
        await user.remove_roles(user.guild.get_role(1105779570411569172))
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} unmuted {user}")
        embed = discord.Embed(title = "Unmute", description = f"**{interaction.user} unmuted {user}**", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        # If the person does not have the "ban members" permission, send an error message
        await interaction.response.send_message('You do not have permission to use this command')
        log = open("botlog.txt", "a",  encoding="utf8")
        log.write(f"{interaction.user} attempted to use command 'mute' | {current_time} \n")
        log.close()
        print(f"Message sent to {Fore.LIGHTBLUE_EX}{interaction.channel}{Fore.RESET} | {Fore.LIGHTMAGENTA_EX}{current_time} {Fore.RESET}")
@bot.tree.command(name="rename")
async def rename(interaction: discord.Interaction, user: discord.Member, name: str):
    """Rename a user"""
    if interaction.user.guild_permissions.manage_nicknames:
        await user.edit(nick=name)
        await interaction.response.send_message(f"{user} has been renamed to {name}")
@bot.tree.command(name="send")
async def send(interaction: discord.Interaction, user: discord.Member, title: str, content: str):
    """Send an embed to a specified user"""
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title = title, description = content, color=discord.Color.blue())
        await user.send(embed=embed)
        embed = discord.Embed(title = "Send message", description = "Message send successfully!", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)
@bot.tree.command(name="decode")
@app_commands.choices(type=[discord.app_commands.Choice(name="Base64", value=1)])
async def encode(interaction: discord.Interaction, type: discord.app_commands.Choice[int], text: str):
    """Decode texts"""
    if type.value == 1:
        data = str(text)
        data_bytes = data.encode("utf-8")
        decodedms = base64.b64decode(data_bytes).decode('utf-8')
        embed = discord.Embed(title = "Decode - Base64", description = f"Your decoded message from `base64` to `utf-8`: \n - {decodedms}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"{interaction.user} decoded {text} from {type}")
@bot.tree.command(name="vc")
@app_commands.choices(operation=[
    discord.app_commands.Choice(name="Make private", value=1),
    discord.app_commands.Choice(name="Add user", value=2),
    discord.app_commands.Choice(name="Remove user", value=3),
    discord.app_commands.Choice(name="Kick user", value=4),
    discord.app_commands.Choice(name="Mute user", value=5),
    discord.app_commands.Choice(name="Make public", value=6),
    discord.app_commands.Choice(name="List voice channels", value=7),
    discord.app_commands.Choice(name="Rename", value=8)
])
async def vc(interaction: discord.Interaction, operation: discord.app_commands.Choice[int], user: typing.Optional[discord.Member]):
    """Manage your own voice channel"""
    channel = interaction.user.voice.channel
    if channel and channel.name == f"{interaction.user}'s voice channel":
        if operation.value == 1:
            await channel.set_permissions(
                interaction.guild.default_role, view_channel=False
            )
            await channel.set_permissions(
                interaction.user, view_channel=True
            )
            await interaction.response.send_message("Voice channel made private!")
        elif operation.value == 2:
            if not user:
                await interaction.response.send_message("Please mention a user to add to the channel!")
            elif user.voice:
                await interaction.response.send_message("User is already in a voice channel!")
            else:
                await channel.set_permissions(
                    user, view_channel=True, connect=True, speak=True
                )
                await interaction.response.send_message(f"{user.mention} has been added to the channel!")
        elif operation.value == 3:
            if not user:
                await interaction.response.send_message("Please mention a user to remove from the channel!")
            elif user == interaction.user:
                await interaction.response.send_message("You cannot remove yourself from the channel!")
            elif user not in channel.members:
                await interaction.response.send_message(f"{user.mention} is not in the channel!")
            else:
                await channel.set_permissions(
                    user, view_channel=None, connect=None, speak=None
                )
                await interaction.response.send_message(f"{user.mention} has been removed from the channel!")
        elif operation.value == 4:
            if not user:
                await interaction.response.send_message("Please mention a user to kick from the channel!")
            elif user == interaction.user:
                await interaction.response.send_message("You cannot kick yourself from the channel!")
            elif user not in channel.members:
                await interaction.response.send_message(f"{user.mention} is not in the channel!")
            else:
                await user.move_to(None)
                await interaction.response.send_message(f"{user.mention} has been kicked from the channel!")
        elif operation.value == 5:
            if not user:
                await interaction.response.send_message("Please mention a user to mute in the channel!")
            elif user not in channel.members:
                await interaction.response.send_message(f"{user.mention} is not in the channel!")
            else:
                await user.edit(mute=True)
                await interaction.response.send_message(f"{user.mention} has been muted!")
        elif operation.value == 6:
            await channel.set_permissions(
                interaction.guild.default_role, view_channel=True
            )
            await interaction.response.send_message("Voice channel made public!")
        elif operation.value == 7:
            # Get all voice channels on the server
            voice_channels = [c for c in interaction.guild.channels if isinstance(c, discord.VoiceChannel)]
            # Filter out channels that don't have the user's name in them
            voice_channels = [c for c in voice_channels if interaction.user.name in c.name]
            # Send a message with the list of channels
            if voice_channels:
                channel_list = "\n".join(f"- {c.name}" for c in voice_channels)
                await interaction.response.send_message(f"Your voice channels:\n{channel_list}")
            else:
                await interaction.response.send_message("You don't have any voice channels on this server.")
        elif operation.value == 8:
            # Prompt the user for a new name for their voice channel
            prompt = await interaction.response.send_message("What would you like to rename your voice channel to?")
            try:
                # Wait for the user's response
                response = await bot.wait_for(
                    "message",
                    check=lambda m: m.author == interaction.user and m.channel == interaction.channel,
                    timeout=30.0
                )
            except asyncio.TimeoutError:
                # If the user doesn't respond in time, delete the prompt message and send an error message
                await prompt.delete()
                await interaction.response.send_message("Timed out. Please try again.")
            else:
                # Update the voice channel's name and send a success message
                await interaction.user.voice.channel.edit(name=response.content)
                await interaction.response.send_message(f"Successfully renamed your voice channel to {response.content}.")
@bot.tree.command(name="xp")
async def xp(interaction: discord.Interaction, user: typing.Optional[discord.Member]):
    """Check your or others xp"""
    if interaction.user.id not in userxp:
        userxp[interaction.user.id] = 0
        embed = discord.Embed(title = "XP", description = f"You dont have any xp.", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
    else:
        if interaction.user.id not in userlevel:
            embed = discord.Embed(title = "XP", description = f"Level: None \n XP: {userxp[interaction.user.id]}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  
        else:
            embed = discord.Embed(title = "XP", description = f"Level: {userlevel[interaction.user.id]} \n XP: {userxp[interaction.user.id]}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)  
@bot.tree.command(name="watch")
async def watch(interaction: discord.Interaction, user: discord.Member):
    """Watch a suspicious user"""
    if interaction.user.guild_permissions.manage_messages:
        watchedusers.append(user.id)
    else:
        await interaction.response.send_message("You dont have enough permission to use this command")
@bot.tree.command(name="unwatch")
async def unwatch(interaction: discord.Interaction, user: discord.Member):
    """Remove users from watching"""
    if interaction.user.guild_permissions.manage_messages:
        if user.id in watchedusers:
            watchedusers.remove(user.id)
            await interaction.response.send_message(f"{user.name} is no longer watched.")
        else:
            await interaction.response.send_message(f"{user.name} is not watched.")
    else:
        await interaction.response.send_message("You dont have enough permission to use this command")
@bot.tree.command(name="level")
async def level(interaction: discord.Interaction, user: typing.Optional[discord.Member]):
    """Request your or others level"""
    if interaction.user.id not in userlevel:
        userlevel[interaction.user.id] = 0
        if interaction.user.id in userxp:
            embed = discord.Embed(title = "Level", description = f"Level: None \n XP: {userxp[interaction.user.id]}", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(title = "Level", description = f"You dont have level or xp", color=discord.Color.blue())
            await interaction.response.send_message(embed = embed)
    else:
        embed = discord.Embed(title = "Level", description = f"Level: {userlevel[interaction.user.id]} \n XP: {userxp[interaction.user.id]}", color=discord.Color.blue())
        await interaction.response.send_message(embed = embed)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.name.startswith("Mod essay"):
        return
    if message.author.name.startswith("Website"):
        return
    mscontent = message.content.split()
    if message.author.id not in taxes:
        taxes[message.author.id] = 0
    taxes[message.author.id] += len(message.content.split())
    if message.author.id in watchedusers:
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"**Watched user!** {message.author.mention} sent a message in {message.channel}. Content: {message.content}")
    if message.author.id not in userxp:
        userxp[message.author.id] = 0
    elif message.author.id not in userlevel:
        userlevel[message.author.id] = 0
    userxp[message.author.id] += len(message.content.split())
    if userxp[message.author.id] >= 100:
        if message.author.id in userxp:
            userlevel[message.author.id] += 1
            userxp[message.author.id] = 0
            await message.guild.get_channel(1105780222315479120).send(f"**{message.author} levelled up to {userlevel[message.author.id]}! Congratulations!**")
    if message.author.id in userlevel:
        if userlevel[message.author.id] == 5:
            await message.author.add_roles(message.guild.get_role(1105780316032991272))
    links = ("http://discord.gg", "https://discord.gg")
    if any(links in message.content.lower() for links in links):
            if message.author.guild_permissions.administrator:
                pass
            else:
                cmdchannel = bot.get_channel(1105571851368927243)
                await cmdchannel.send(f"Suspicious activity in {message.channel.mention} from {message.author.mention}")
                await message.delete()
                await message.author.send("We dont want links here!")
                await cmdchannel.send(f"{message.author} attempted to send links ({message.content})")
                await cmdchannel.send(f"")
    if "correct" in message.content.lower():
        corrected = message.content.split("correct")
        if lastmessage == "unhandled":
            await message.channel.send(f"Oh, okay. You corrected the my `{lastmessage}` help message for this: {corrected}. Thank you for your support ;)")
            sentences[0] = corrected
    if "am i right?" in message.content.lower():
        await message.channel.send("no")
    elif "stfu" in message.content.lower():
        await message.channel.send("stfu you")
    elif "im the boss" in message.content.lower():
        await message.channel.send("what colour is your purpleno bot role?")
    elif bot.user.mention in message.content.lower():
        if "help" in message.content.lower():
            if "unhandled error" in message.content.lower() or "unhandled exception" in message.content.lower() or "unhandled" in message.content.lower() or "unexcepted" in message.content.lower() or "unexpected" in message.content.lower() or "error" in message.content.lower():
                await message.channel.send(sentences[0])
                lastmessage = "unhandled"
            elif "config" in message.content.lower() or "cfg" in message.content.lower():
                await message.channel.send(sentences[1])
                lastmessage = "config"
            elif "sniper" in message.content.lower() and "scope" in message.content.lower() or "zoom" in message.content.lower():
                await message.channel.send(sentences[2])
                lastmessage = "zoom"
            elif "inject" in message.content.lower():
                await message.channel.send(sentences[3])
                lastmessage = "inject"
            elif "crash" in message.content.lower():
                await message.channel.send(sentences[4])
                lastmessage = "crash"
            elif "lua" in message.content.lower():
                await message.channel.send(sentences[5])
                lastmessage = "lua"
            elif "premium" in message.content.lower():
                await message.channel.send(sentences[6])
                lastmessage = "premium"
            elif "double" in message.content.lower():
                await message.channel.send(sentences[7])
                lastmessage = "doubletap"
            else:
                await message.channel.send("Sorry, i couldn't recognize your error. Please contact the support team for help, or/and report this error at **https://www.purpleno.epizy.com/report.html**")
        else:
            await message.channel.send("Im here to help!")
    elif "asked" in message.content.lower():
        await message.channel.send("tf cares lmao")
    elif "fuck you" in message.content.lower():
        await message.channel.send("want to paint your face?")
    elif "kill yourself" in message.content.lower() or "kys" in message.content.lower():
        await message.channel.send("stay mad")
    elif "beat you" in message.content.lower():
        await message.channel.send("dont wait for me to stand up!")
    elif "you shit" in message.content.lower() or "your shit" in message.content.lower() or "ur shit"  in message.content.lower() or "u shit"  in message.content.lower():
        await message.channel.send("says the garbage")
    bad_words = ("nigger", "niger", "n1ger", "n1gger", "neger", "negger", "nigga", "n1gga", 'n1ga', "niga", "nig@", "nigg@")
    if any(bad_word in message.content.lower() for bad_word in bad_words):
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"Suspicious activity in {message.channel.mention} from {message.author.mention}")
        await message.delete()
        await message.channel.send(f"{message.author.mention} dont swear!")
        log = open("botlog.txt", "a",  encoding="utf8")
        log.write(f"{message.author} tried to send blacklisted messages | {current_time} \n")
        log.close()
        if message.author.id not in warns:
            warns[message.author.id] = 0  # initialize warn count for new user
        warns[message.author.id] += 1  # increment warn count for user
        if warns[message.author.id] >= 5:
            await message.author.add_roles(message.author.guild.get_role(1105779570411569172))
            warns[message.author.id] = 0
            embed = discord.Embed(title="Warn threshold", description=f"**{message.author} has been muted due to warn threshold's. Ask an admin to remove it.**", color=discord.Color.blue())
            await message.channel.send(embed = embed)
            embed = discord.Embed(title="Warn threshold", description=f"**You have been muted in {message.guild}, to remove your mute, message any admin on the server. Remember, Harassing an admin to remove it, is strictly forbidden, and come with bad consequences!**", color=discord.Color.blue())
            await message.author.send(embed = embed)
            log = open("botlog.txt", "a",  encoding="utf8")
            log.write(f"{message.author} got muted due to warn thresholds | {current_time} \n")
            log.close()
    activatewords = ("spam", "kill", "fuck", "blow", "kys", "retard")
    if any(activateword in message.content.lower() for activateword in activatewords):
        cmdchannel = bot.get_channel(1105571851368927243)
        await cmdchannel.send(f"Suspicious activity in {message.channel.mention} from {message.author.mention}, vulgar item: {message.content}")
    if mscontent[0] == ("/additem"):
        if message.author.guild_permissions.manage_messages:
            if message.author.id not in inv:
                inv[message.author.id] = []
            trash = ["tape", "vape", "wood", "cigar", "cheese"]
            for i in range(3):
                inv[message.author.id].append(random.choice(trash))
#ANTISPAM
    if message.author not in message_counts:
            message_counts[message.author] = 1
    else:
            message_counts[message.author] += 1
            # If the user has exceeded the maximum number of messages allowed, delete their message and send them a warning
    if message_counts[message.author] > 3 and not message.author.guild_permissions.manage_messages:
            await message.delete()
            await message.author.send("You have exceeded the maximum number of messages allowed per second. Please slow down to prevent spam.")
            log = open("botlog.txt", "a",  encoding="utf8")
            log.write(f"{message.author} spammed in {message.channel} | {current_time} \n")
            log.close()
            if message.author not in warns:
                warns[message.author] = 0  # initialize warn count for new user
            warns[message.author] += 1  # increment warn count for user
            if warns[message.author] >= 5:
                await message.author.add_roles(message.author.guild.get_role(1105779570411569172))
                warns[message.author] = 0
                embed = discord.Embed(title="Warn threshold", description=f"**{message.author} has been muted due to warn threshold's.**", color=discord.Color.blue())
                await message.channel.send(embed = embed)
                embed = discord.Embed(title="Warn threshold", description=f"**You have been muted in {message.guild} for 20 minutes. If you message any admin to remove it earlier, your request will be instantly rejected, if you continue any harrasment/threat against the admin team, you will be kicked/banned**", color=discord.Color.blue())
                await message.author.send(embed = embed)
                log = open("botlog.txt", "a",  encoding="utf8")
                log.write(f"{message.author} got muted due to warn threshold. | {current_time} \n")
                log.close()
                await asyncio.sleep(3600)
                roletoremove = discord.utils.get(message.guild.roles, id=1105779570411569172)
                await message.author.remove_roles(roletoremove)
                embed = discord.Embed(title = "Mute", description = f"**{message.author} has been unmuted.**", color=discord.Color.blue())
                await message.channel.send(embed = embed)
    await asyncio.sleep(5)
    message_counts[message.author] = 0

TOKEN = "Your token here!"
bot.run(TOKEN)