# Nextcord Imports
import nextcord
from nextcord import Interaction, SlashOption, ChannelType, Embed
from nextcord.abc import GuildChannel
from nextcord.ext import commands, tasks
from nextcord.ui import View, Button, Select, Modal, TextInput
from typing import List

# andere Imports
import requests
import asyncio
import aiohttp
import datetime
import humanfriendly
import time
import json
import supabase
from dotenv import load_dotenv
from datetime import timedelta

import logging

import os
from supabase import create_client, Client


intents = nextcord.Intents.default()
intents = nextcord.Intents().all()

bot = commands.Bot(intents=intents)

logger = logging.getLogger("bot")

logger.info(f"Imports Loaded, Bot created, Intents defined")

load_dotenv()

logger.info(f"Loaded Dotenv")

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

logger.info(f"Initialized Supabase Client")


ticket_message = 1211711545055248455
ticket_category = 1205186820640342057
ticket_channel = 1205110316573261864
reactemoji = "🎟️"

logger.info(f"Bot wird gestartet")




        
logging.basicConfig(
        filename='UserActions.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
        )

# Server ID
serverID = 1099017150703861842

# Die spezifische Benutzer-ID, die überprüft werden soll
bossa_id = 793446132126580766

perplexity_api_key = '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'

TOKEN = os.getenv("DISCORD_BOT_TOKEN")


@bot.event
async def on_ready():
    message = await bot.get_channel(ticket_channel).fetch_message(ticket_message)
    if not "🎟️" not in [reaction.emoji for reaction in message.reactions]:
        await message.add_reaction("🎟️")
        
    logger.info(f"🔴 - {bot.user.name} Uploading Slash commands")
    time.sleep(1.3)
    logger.info(f"🟡 - {bot.user.name} Uploading Complete")
    time.sleep(0.8)
    logger.info(f"🟢 - {bot.user.name} is Online")

    while True:
        await bot.change_presence(activity=nextcord.Game("InProd By Bøssa & Nova"), status=nextcord.Status.idle)
        await asyncio.sleep(30)
        await bot.change_presence(activity=nextcord.Game("/msg um Dmˋs zu senden"), status=nextcord.Status.idle)
        await asyncio.sleep(30)
        await bot.change_presence(activity=nextcord.Game("/info für Informationen"), status=nextcord.Status.idle)
        await asyncio.sleep(30)
        await bot.change_presence(activity=nextcord.Game("/ping für Bot-Ping"), status=nextcord.Status.idle)
        await asyncio.sleep(30)                
        
        
                
        
@bot.event
async def on_message(message): # Nachrichten Loggen
    bossa = await bot.fetch_user(bossa_id)
    channel_id = 1209869720241578045
    
    if message.author == bot.user:  
        return
    
    if message.author.bot:
        return
    
    
    
    
    # Nachrichtenzähler für den Benutzer aktualisieren
    user_id = str(f"{message.author.id}")
    user_name = str(f"{message.author.name}")
    data = supabase.table("achevments").select("*").eq("user_id", user_id).execute()
    new_count = 1
    if data.data:
        # Nachrichtenzähler erhöhen
        new_count = data.data[0]["message_count"] + 1
        supabase.table("achevments").update({"message_count": new_count, "guild_name": message.guild.name, "last_message": message.content}).eq("user_id", user_id).execute()
    else:
        # Neuer Eintrag für den Benutzer
        supabase.table("achevments").insert({"user_id": user_id, "user_name": user_name, "message_count": new_count, "guild_name": message.guild.name}).execute()

    # Überprüfen, ob ein Achievement erreicht wurde
    achievements = [5000, 10000, 100000, 500000, 1000000]
    if new_count == 1:
        await message.channel.send(f"🏆 Glückwunsch {message.author.mention}, du hast deine Erste nachricht geschrieben!")
    if new_count == 5:
        neuling_role = nextcord.utils.get(message.guild.roles, name="Neuling")
        if neuling_role:
            await message.author.add_roles(neuling_role)
            await message.channel.send(f"🎉 {message.author.mention}, du hast die Rolle <@&1211687487366234232> für das Erreichen von 5 Nachrichten erhalten!")
            supabase.table("achevments").update({"achevet_role": "Neuling"}).eq("user_id", user_id).execute()
    if new_count == 100:
        veteran_role = nextcord.utils.get(message.guild.roles, name="Veteran")
        neuling_role = nextcord.utils.get(message.guild.roles, name="Neuling")
        if veteran_role:
            await message.author.add_roles(veteran_role)
            await message.author.remove_roles(neuling_role)
            await message.channel.send(f"🎉 {message.author.mention}, du hast die Rolle <@&1211687743265054840> für das Erreichen von 100 Nachrichten erhalten!")
            supabase.table("achevments").update({"achevet_role": "Veteran"}).eq("user_id", user_id).execute()
    if new_count == 500:
        legend_role = nextcord.utils.get(message.guild.roles, name="Legende")
        veteran_role = nextcord.utils.get(message.guild.roles, name="Veteran")
        if legend_role:
            await message.author.add_roles(legend_role)
            await message.author.remove_roles(veteran_role)
            await message.channel.send(f"🎉 {message.author.mention}, du hast die Rolle <@&1211688325304549407> für das Erreichen von 500 Nachrichten erhalten!")
            supabase.table("achevments").update({"achevet_role": "Legende"}).eq("user_id", user_id).execute()
    if new_count == 1000:
        elite_role = nextcord.utils.get(message.guild.roles, name="Elite")
        legend_role = nextcord.utils.get(message.guild.roles, name="Legende")
        if elite_role:
            await message.author.add_roles(elite_role)
            await message.author.remove_roles(legend_role)
            await message.channel.send(f"🎉 {message.author.mention}, du hast die Rolle <@&1211688822853730365> für das Erreichen von 1000 Nachrichten erhalten!")
            supabase.table("achevments").update({"achevet_role": "Elite"}).eq("user_id", user_id).execute()
    
    
    
    
    
    
    
    if new_count in achievements:
        await message.channel.send(f"🎉 Glückwunsch {message.author.mention}, du hast das Achievement für das Erreichen von {new_count} Nachrichten erreicht!")

    if bot.user.mentioned_in(message):
        embed = nextcord.Embed(
        title=f"",
        description=f"Danke, dass du mich gepinngt hast. Ich befinde mich derzeit in einer Testphase, also falls Probleme auftreten, melde sie bitte im Ticket-Kanal <#1205110316573261864>. \nDu kannst auch einige meiner Befehle ausprobieren, schreibe einfach in Chat ein [ / ] und siehe dir die Befehel an die zurzeit zur Verfügung stehen.",
        color=nextcord.Color.blue()
        )
        embed.set_author(name=(f"Hey {message.author}!"), icon_url=message.author.avatar)
        embed.set_footer(text=f"BossNetwork | Powered by BossNet")
        await message.channel.send(embed=embed)
        return
    
    elif message.author.mention == bossa_id:
        embed = nextcord.Embed(
        title=f"",
        description=f"Bitte erwähnen nicht den Owner \nBei wiederholten erwähnen kannst du gemuted werden!",
        color=nextcord.Color.blue()
        )
        embed.set_author(name=(f"Hey {message.author}!"), icon_url=message.author.avatar)
        embed.set_footer(text=f"Auto Mod | Powered by BossNet")
        await message.channel.send(embed=embed)
        last_message = await message.channel.history(limit=2).flatten()
        await last_message[1].delete()
        await message.author.edit(timeout=datetime.timedelta(minutes=1))
        return
    
    if message.channel.id == channel_id:
        # Hier würden Sie die Anfrage an die Perplexity API senden
        
        async def ask_perplexity(message_content):
            url = 'https://api.perplexity.ai/chat/completions'
            params = {
                'api_key': perplexity_api_key,
                'query': message_content
            }
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data['antwort']
                    else:
                        return f':x: Fehler bei der Anfrage: Statuscode {response.status}'
        
        
    
        response = await ask_perplexity(message.content)
        await message.reply(response)
        
        # await message.reply(f"Hey {message.author.mention}, \n\nDie BossNet-Ai wird gerade eingerichtet und ist bald für VIP's verfügbar.")
        # und die Antwort im Kanal posten
        return      
    
    else:
        logger.info(f'{message.author.display_name} - {message.content} - {message.channel} - {message.guild}')               
                
                
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1204839091561308271)
    if channel:
        
        role_id = 1099017150703861845
        embed = nextcord.Embed(
        title=f"",
        description=f"Wir freuen uns, dich in unserer Community zu begrüßen.",
        color=nextcord.Color.blue()
        )
        embed.set_author(name=(f"Willkommen {member}!"), icon_url=member.avatar)
        embed.set_footer(text=f"")
        await channel.send(embed=embed)
    
        # await member.edit(timeout=datetime.timedelta(minutes=10))
        
        try:
            await member.send(f"Willkommen {member.mention} auf **{member.guild.name}**! \n\nWir freuen uns dich begrüßen zu dürfen, da dieser Server zurzeit noch im Aufbau musst du dich noch etwas gedulden. \n\nSchaue dich trotzdem schoneinmal um in <#1099017151412699228> oder schreibe <@793446132126580766> an um dich schon früher zu Verifizieren")
        except nextcord.Forbidden:
            logger.warning("Nachricht konnte nicht an Member gesendet werden!")

    else:
        logger.warning(f'Willkommem Kanal konnte nicht gefunden. Stelle sicher, dass die Kanal-ID korrekt ist.')                
                
@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(1099017151672754224)  # Ersetze YOUR_CHANNEL_ID durch die tatsächliche ID des Zielkanals
    if channel:
        await channel.send(f':bluearrow: {member.mention} hat den server verlassen')
    else:
        logger.warning(f'Kanal konnte nicht gefunden. Stelle sicher, dass die Kanal-ID korrekt ist.') 
                




            
            
            
@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)

    if payload.message_id == ticket_message and str(payload.emoji) == reactemoji and not user.bot:
        message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        if reactemoji not in [reaction.emoji for reaction in message.reactions]:
            await message.add_reaction
        else:
            await message.remove_reaction(payload.emoji, user)
        category = bot.get_channel(ticket_category)
        channel_name = f"ticket-{user.display_name}"

        for channel in category.text_channels:
            if channel.name.lower() == channel_name.lower():
                logger.warning(f"Ticket Already Open - {user.name}#{user.discriminator} ({user.id})")
                return
       
        overwrites = {
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            user: nextcord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True)
        }

        channel = await category.create_text_channel(name=channel_name, overwrites=overwrites)
        embed = nextcord.Embed(
        title=f"Neues Ticket",
        description=f"Hallo {user.mention}, unser Team wird sich gleich um dich kümmern! \nBitte beschreibe in der Zwischenzeit dein Problem!",
        color=nextcord.Color.blue()
        )
        embed.set_footer(text=(f"Support System powered by BossNet"))
        message = await channel.send(user.mention,embed=embed)
        logger.info(f"Ticket created - {user.name}#{user.discriminator} ({user.id})")
        
        
        
        
@bot.slash_command(
    name="kick",
    description="Kickt ein Mitglied vom Server",
    guild_ids=[serverID]
)
async def kick(interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "Kicked by an Admin"):
    if interaction.user.guild_permissions.kick_members:
        if reason == f"Kicked by an Admin":
            reason = f"{member.global_name} Kicked by {interaction.user.global_name}  |  Powered by 🌐・Boss Network"
        
        await member.kick(reason=reason)
        
        embed = nextcord.Embed(
        title=f"",
        description=f"{member} wurde vom Server gekickt.",
        color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=(f"Grund: {reason}"))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.info(f"{interaction.user.display_name} - commited /kick to {member} - Reason: {reason}")
        try:
            embed = nextcord.Embed(
            title=f"Du wurdest von **{interaction.guild.name} Gekicked**",
            description=f"",
            color=nextcord.Color.red()
            )
            embed.set_author(name=(f"Tut uns leid {member.global_name}"), icon_url=member.avatar)
            embed.set_footer(text=(f"Grund: {reason}"))
            embed.add_field(name="Warum wurde ich gekicked?", value="Du hast gegen die Server Regeln verstoßen oder bereits **3** Warnungen erhalten.", inline=False)
            embed.add_field(name="Wie kann ich wieder auf den Server?", value="Gehe auf **https://discord.gg/f3JCDnrR** um wieder dem Server beizutreten und halte dich dieses mal an die Regeln Bitte!", inline=False)
            await member.send(embed=embed)
        except nextcord.Forbidden:
            logger.info(f"Nachricht konnte nicht an {member} gesendet werden. {nextcord.Forbidden}")
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Mitglieder zu kicken.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
@bot.slash_command(
    name="ban",
    description="bannt ein Mitglied vom Server",
    guild_ids=[serverID]
)
async def ban(interaction: nextcord.Interaction, member: nextcord.Member, reason=(f"Banned by an Admin")):
    if interaction.user.guild_permissions.ban_members:
        if reason == f"Banned by an Admin":
            reason = f"{member.global_name} Banned by {interaction.user.global_name}  |  Powered by 🌐・Boss Network"

        await member.ban(reason=reason)
        
        embed = nextcord.Embed(
        title=f"",
        description=f"{member} wurde vom Server gebannt.",
        color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user.global_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=(f"Grund: {reason}"))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.info(f"{interaction.user.display_name} - commited [ /ban ] to {member} - Reason: {reason}")
        try:
            embed = nextcord.Embed(
            title=f"Du wurdest **Gebannt** von {interaction.user.global_name}",
            description=f"",
            color=nextcord.Color.red()
            )
            embed.set_author(name=(f"Tut uns leid {member.global_name}"), icon_url=member.avatar)
            embed.set_footer(text=(f"Grund: {reason}"))
            embed.add_field(name="Warum wurde ich gebannt?", value="Du hast gegen die Server Regeln verstoßen oder bereits **3** Warnungen erhalten.", inline=False)
            embed.add_field(name="Wie kann ich wieder auf den Server?", value="Du musst einen Entbannungsantrag stellen und wir prüfen nochmal ob wir dich wieder auf den Server lassen", inline=False)
            await member.send(embed=embed)
        except nextcord.Forbidden:
            logger.info(f"Nachricht konnte nicht an {member.global_name} gesendet werden. {nextcord.Forbidden}")
        
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Mitglieder zu bannen.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)   
                
                
                
@bot.slash_command(
    name="info",
    description="Zeigt die Bot-Info",
    # guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def info(interaction: nextcord.Interaction, about: str = nextcord.SlashOption(
    name="about",
    description="Wähle eine Kategorie",
    choices={"Bot": "bot", "BossNetwork": "bossnet", "Developer": "developers"})):
    supabase.table("logs").insert({"issuer": interaction.user.id, "issuer_name": interaction.user.name, "command": "/info"}).execute()
    
    if about == "bot":
        embed = nextcord.Embed(
        title=f"",
        description=f"Der Bot ist zurzeit noch in einer Testphase und auf 🌐・Boss Network verfügbar",
        color=nextcord.Color.blue()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"2024 ・ v1.0 ・ Luca Klemme, Junes Zayed | Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    elif about == "bossnet":
        embed = nextcord.Embed(
        title=f"Wir sind **🌐・Boss Network**",
        description=f"In einer Zeit voller Wandlungen und Veränderungen in der Tech-Branche bieten wir ihrem Unternehmen Halt und Beistand, indem wir die neusten Software-lösungen im Bereich der Server-Software und Backend-Entwicklung leifern.",
        color=nextcord.Color.blue()
        )
        embed.set_author(name=(f"Hey {interaction.user.global_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"2024 ・ BossNetwork ・ Luca Klemme, Junes Zayed | Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    elif about == "developers":
        embed = nextcord.Embed(
        title=f"Wir sind Nova und Bossa",
        description=f"",
        color=nextcord.Color.blue()
        )
        # About Junes
        embed.add_field(name="Über Junes", value="", inline=False)

        # About Luca
        embed.add_field(name="Über Luca", value="Hallo, ich bin Luca der Lead-Developer von **🌐・Boss Network** und Entwickle rund um Discord-Bots bis hin zu Micro-Services Anwendungen.", inline=False)
        embed.set_author(name=(f"Hey {interaction.user.global_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"2024 ・ Luca Klemme, Junes Zayed | Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    logger.info(f"{interaction.user.display_name} - commited [ /info ]")
    
    
                
        
        
@bot.slash_command(
    name="msg",
    description="schreibt einem Discord User deine Nachricht",
    guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def msg(interaction: nextcord.Interaction, member: nextcord.Member, message):
    user_embed = nextcord.Embed(
        title=f"",
        description=f"Du hast {member} — **{message}** geschriben",
        color=nextcord.Color.green()
    )
    user_embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=user_embed, ephemeral=True)
    
    
    member_embed = nextcord.Embed(
        title=f"{interaction.user} schreibt dir!",
        description=f"||{message}||",
        color=nextcord.Color.blue()
    )
    member_embed.set_author(name=(f"Hey {member}!"), icon_url=interaction.user.avatar.url)
    member_embed.set_footer(text="Powered by 🌐・Boss Network")
    await member.send(embed=member_embed)
   
    logger.info(f"{interaction.user.display_name} - commited [ /msg ] to {member}")



@bot.slash_command(
    name="achevments",
    description="schreibt einem Discord User deine Nachricht",
    guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def achevments(interaction: nextcord.Interaction, member: nextcord.Member):
    user_id = interaction.user.id

    data = supabase.table("achevments").select("*").eq("user_id", user_id).execute()

    if data.data == None:
        messages = supabase.table('achevments').select('message_count').execute()
        achevet_role = supabase.table('achevments').select('achevet_role').execute()

        messages_data = messages.model_dump_json()
        achevet_role_data = achevet_role.model_dump_json()

        print(messages_data)
        print(achevet_role_data)

        embed = nextcord.Embed(
            title=f"Deine Achievements",
            description=f"**Total Messages**: {messages_data[0]['message_count']} \n\n**Dein Rang**: {achevet_role_data[0]['achevet_role']}",
            color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)
    else:
        embed = nextcord.Embed(
            title=f"",
            description=f":x: Es wurden keine Achievements gefunden.",
            color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
   
    logger.info(f"")        
        
                
                



@bot.slash_command(
    name="ping",
    description="Zeigt den Bot-Ping",
    # guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def ping(interaction: nextcord.Interaction):
    supabase.table("logs").insert({"issuer": interaction.user.id, "issuer_name": interaction.user.name, "command": "/ping"}).execute()
    
    latency = bot.latency
    embed = nextcord.Embed(
        title=f"",
        description=f":hourglass: Bot Latency: {round(latency * 1000)}ms",
        color=nextcord.Color.blue()
    )
    embed.set_author(name=(f"Hey {interaction.user.global_name}!"), icon_url=interaction.user.avatar.url)
    embed.set_footer(text="Powered by 🌐・Boss Network")
    
    await interaction.response.send_message(embed=embed, ephemeral=True)
    logger.info(f"{interaction.user.display_name} - commited [ /ping ]")


@bot.slash_command(
    name="role",
    description="Gibt einem [User] eine [Rolle]",
    guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def role(interaction: Interaction):
    pass  # Dieser Hauptbefehl wird nie direkt aufgerufen, da er Subcommands hat

@role.subcommand(
    name="add",
    description="Fügt einem Mitglied eine Rolle hinzu."
)
async def add(interaction: nextcord.Interaction, member: nextcord.Member, role: nextcord.Role):
    if interaction.user.guild_permissions.manage_roles:
        await member.add_roles(role)
        
        embed = nextcord.Embed(
        title=f"",
        description=f"{member} wurde {role} gegeben",
        color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
       
        logger.info(f"{interaction.user.display_name}-  commited [ /role add ] to {member} - added [ #{role} ]")
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Rollen zu verwalten.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
        
        
@role.subcommand(
    name="remove",
    description="Entfernt einem Mitglied eine Rolle."
)        
async def remove(interaction: nextcord.Interaction, member: nextcord.Member, role: nextcord.Role):
    if interaction.user.guild_permissions.manage_roles:
        await member.remove_roles(role)
        
        embed = nextcord.Embed(
        title=f"",
        description=f"{member} wurde {role} entfernt",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.info(f"{interaction.user.display_name} - commited [ /role remove ] to {member} - removed [ #{role} ]")
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Rollen zu verwalten.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)



@bot.slash_command(
    name="clear",
    description="Löscht eine Anzahl von Nachrichten",
    guild_ids=[serverID]
    
)
async def clear(interaction: nextcord.Interaction, anzahl: int, member: nextcord.Member=None): # Clear command
    if interaction.user.guild_permissions.manage_messages:
        supabase.table("logs").insert({"issuer": interaction.user.id, "issuer_name": interaction.user.name, "command": "/clear", "guild": interaction.guild.name}).execute()
        def check(message):
            return message.author == member if member else True
        
        deleted = await interaction.channel.purge(limit=anzahl, check=check)
         
        if not deleted:
            # Senden Sie eine Nachricht, wenn keine Nachrichten gelöscht wurden
            embed = nextcord.Embed(
            title=f"",
            description=f":x: Es existieren **keine** Nachrichten zum löschen",
            color=nextcord.Color.red()
            )
            embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
            embed.set_footer(text=f"Powered by 🌐・Boss Network")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        else:
            if member:
                embed = nextcord.Embed(
                title=f"",
                description=f":hourglass: **{len(deleted)}** Nachrichten werden gelöscht",
                color=nextcord.Color.green()
                )
                embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
                embed.set_footer(text=f"Nachrichten von {member} werden gelöscht | Powered by 🌐・Boss Network")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                logger.info(f"{interaction.user.display_name} commited [ /clear ] -- löscht {len(deleted)} nachrichten von {member}")
            else:
                embed = nextcord.Embed(
                title=f"",
                description=f":hourglass: **{len(deleted)}** Nachrichten werden gelöscht",
                color=nextcord.Color.green()
                )
                embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
                embed.set_footer(text="Powered by 🌐・Boss Network")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                logger.info(f"{interaction.user.display_name} - commited [ /clear ] -löscht {len(deleted)} nachrichten")
    else:
        
        embed = nextcord.Embed(
        title=f"",
        description=f":x: du hast nicht die Berechtigung, Nachrichten zu löschen.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user.display_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text="Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
                

            
@bot.slash_command(
    name="warn",
    description="Powered by BossNet",
    guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def warn(interaction: Interaction):
    pass  # Dieser Hauptbefehl wird nie direkt aufgerufen, da er Subcommands hat                   


@warn.subcommand(
    name="add",
    description="Warnt einen Member",
)
async def add(interaction: nextcord.Interaction, member: nextcord.Member, grund=("Warned by an Admin")):
    if interaction.user.guild_permissions.kick_members:
        data = supabase.table("infraction").select("*").eq("member_id", member.id).execute()
        num_warnings = sum(record['warnings'] for record in data.data)
        
        if num_warnings >= 3:
            timeout_duration = timedelta(minutes=10)
            await member.edit(timeout=timeout_duration)
            embed = nextcord.Embed(
            title=f"",
            description=f"{member} wurde gemuted | Anzahl der warnungen {num_warnings}",
            color=nextcord.Color.green()  
            )
            embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
            embed.add_field(name=f"", value=f"{member.global_name} wurde für 10 Minuten temporär gemuted wegen zu vielen Warnungen")
            embed.set_footer(text=(f"Grund: {grund} | Powered by 🌐・Boss Network"))
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif num_warnings < 3:
            if data.data:
                # Mitglied bereits gewarnt, Warnzähler erhöhen
                warn_count = data.data[0]["warnings"] + 1
                supabase.table("infraction").update({"warnings": warn_count, "reason": grund}).eq("member_id", member.id).execute()   
            else:
                # Neuer Eintrag für Mitglied
                supabase.table("infraction").insert({"member_name": member.name, "member_id": member.id, "warnings": 1, "reason": grund, "issuer": interaction.user.name, "infraction_type": "Warning"}).execute()
            
                logger.info(f"{interaction.user.display_name} - commited [ /warn ] to @{member} - Reason: {grund}")
            user_embed = nextcord.Embed(
            title=f"",
            description=f"{member} wurde gewarnt | Anzahl der warnungen {warn_count if data.data else 1}",
            color=nextcord.Color.green()  
            )
            user_embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
            user_embed.set_footer(text=(f"Grund: {grund} | Powered by 🌐・Boss Network"))
            await interaction.response.send_message(embed=user_embed, ephemeral=True)
             
            member_embed = nextcord.Embed(
            title=f"",
            description=f"Du wurdest auf **{interaction.guild.name}** gewarnt | Anzahl deiner Warnungen {warn_count if data.data else 1}",
            color=nextcord.Color.red() 
            )
            member_embed.set_author(name=(f"Hey {member}!"), icon_url=member.avatar)
            member_embed.set_footer(text=(f"Grund: {grund} | Powered by 🌐・Boss Network"))
            await member.send(embed=member_embed)    
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Mitglieder zu Warnen.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text="Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)           
            
  
@warn.subcommand(
    name="delete",
    description="löscht alle warnungen des members",
)
async def delete(interaction: nextcord.Interaction, member: nextcord.Member):
    # Überprüfen, ob das Mitglied Warnungen hat
    data = supabase.table("warnings").select("*").eq("member_id", member.id).execute()
    
    if data.data:
        # Warnungen des Mitglieds löschen
        supabase.table("warnings").delete().eq("member_id", member.id).execute()
        
        embed = nextcord.Embed(
        title=f"",
        description=f"Alle Warnungen für {member.display_name} wurden gelöscht.",
        color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text="Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        # Keine Warnungen gefunden
        embed = nextcord.Embed(
        title=f"",
        description=f"{member.display_name} hat zurzeit noch keine Warnungen zum Löschen.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text="Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)

@warn.subcommand(
    name="show", 
    description="Zeigt die Warnungen eines Members an."
)
async def show_warnings(interaction: nextcord.Interaction, member: nextcord.Member):
    # Aufzeichnungen aus Supabase holen
    response = supabase.table("warnings").select("*").eq("member_name", member.name).execute()
    warnings = []

    for record in response.data or []:
        warning = {"Member": record['member_name'], "Warnungen": record['warnings'], "Grund": record['reason']}
        warnings.append(warning)

    embed = nextcord.Embed(
        title=f"Warnungsbericht für {member}", 
        color=nextcord.Color.blue()
    )
    if len(warnings) == 0:
        embed.description = "Keine Warnungen für diesen Member gefunden."
    else:
        embed.add_field(name="", value='\n'.join([json.dumps(warning, indent=2) for warning in warnings]))

    await interaction.response.send_message(embed=embed, ephemeral=True)        

@bot.slash_command(
    name="mute",
    description="Muted einen Member für eine bestimmte Zeit",
    guild_ids=[serverID]
)
async def mute(interaction: nextcord.Interaction, member: nextcord.Member, time: str = nextcord.SlashOption(
    name="time",
    description="Wähle wie lang der User gemuted wird. eg. 10h, 10m, 10s",
    ), *, reason=(f"Muted by an Admin")):
    if interaction.user.guild_permissions.kick_members:

        if reason == f"Muted by an Admin":
            reason = f"On {interaction.guild.name} | {member.global_name} muted by {interaction.user.global_name}"
        
        data = supabase.table("infraction").select("*").eq("member_id", member.id).execute()
        
        if data.data:
            # Mitglied bereits gewarnt, Warnzähler erhöhen
            warn_count = data.data[0]["warnings"] + 1
            supabase.table("infraction").update({"warnings": warn_count, "reason": reason, "infraction_type": "Mute", "other": time}).eq("member_id", member.id).execute()   
        else:
            # Neuer Eintrag für Mitglied
            supabase.table("infraction").insert({"warnings": "1", "member_name": member.global_name, "member_id": member.id, "reason": reason, "issuer": interaction.user.global_name, "infraction_type": "Mute", "other": f"{time} h : m : s"}).execute()
            
            logger.info(f"{interaction.user.display_name} - commited [ /warn ] to @{member} - Reason: {reason}")
        
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        
        embed = nextcord.Embed(
        title=f"",
        description=f"{member} wurde gemutet für {datetime.timedelta(seconds=time)}",
        color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user}"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=(f"Grund: {reason}"))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.info(f"{interaction.user.display_name} - commited /mute to {member.global_name} for {datetime.timedelta(seconds=time)} —— Reason: {reason}")
        try:
            embed = nextcord.Embed(
            title=f"Du wurdest auf {interaction.guild.name} **Gemuted**",
            description=f"Gemuted für {datetime.timedelta(seconds=time)} h : m : s",
            color=nextcord.Color.red()
            )
            embed.set_author(name=(f"Tut uns leid {member.global_name}"), icon_url=member.avatar)
            embed.set_footer(text=(f"Grund: {reason} | Powered by 🌐・Boss Network"))
            embed.add_field(name="Warum wurde ich gemuted?", value="Du hast gegen die Server Regeln verstoßen oder bereits **3** Warnungen erhalten.", inline=False)
            embed.add_field(name="Wie kann ich wieder Schreiben/Reden", value="Du musst einen Entbannungsantrag stellen und wir prüfen nochmal ob wir dich vorzeitig freigeben", inline=False)
            await member.send(embed=embed)
        except Exception as e:
            logger.warning(f"Fehler: {e}")
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Mitglieder zu muten.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text="Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True) 
        
        
@bot.slash_command(
    name="unmute",
    description="Unmuted einen Member",
    guild_ids=[serverID]
)
async def unmute(interaction: nextcord.Interaction, member: nextcord.Member, reason=(f"Unmuted by an Admin")):
    if interaction.user.guild_permissions.kick_members:
        if reason == f"Unmuted by an Admin":
            reason = f"On {interaction.guild.name} | {member.global_name} unmuted by {interaction.user.global_name}"

        await member.edit(timeout=None)
        embed = nextcord.Embed(
        title=f"",
        description=f"{member.global_name} wurde unmuted",
        color=nextcord.Color.green()
        )
        embed.set_author(name=(f"Hey {interaction.user.global_name}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=f"Reason: {reason} | Powered by 🌐・Boss Network")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.info(f"{interaction.user.display_name} - commited /unmute ] {member.global_name}")

        try:
            embed = nextcord.Embed(
            title=f"Du wurdest **Unmuted** auf **{interaction.guild.name}**",
            description=f"",
            color=nextcord.Color.green()
            )
            embed.set_author(name=(f"Glückwunsch {member.global_name}"), icon_url=member.avatar)
            embed.set_footer(text=(f"Grund: {reason} | Powered by 🌐・Boss Network"))
            await member.send(embed=embed)
        except Exception as e:
            logger.warning(f"Fehler: {e}")
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Mitglieder zu muten.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
        embed.set_footer(text=(f"Powered by 🌐・Boss Network"))
        await interaction.response.send_message(embed=embed, ephemeral=True) 

        
@bot.slash_command(
    name="channel",
    description="Powered by BossNet",
    guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def channel(interaction: Interaction):
    pass  # Dieser Hauptbefehl wird nie direkt aufgerufen, da er Subcommands hat        
   
@channel.subcommand(
    name="lock",
    description="Sperrt den aktuellen Kanal",
)
async def lock(
    interaction: Interaction,
    nachricht: str = SlashOption(
        name="nachricht",
        description="Eine optionale Nachricht, die beim Sperren des Kanals angezeigt wird",
        required=False
    )
):
    if interaction.user.guild_permissions.manage_channels:
        # Setzen Sie die Berechtigungen für @everyone so, dass sie keine Nachrichten mehr senden können
        everyone_role = interaction.guild.default_role
        await interaction.channel.set_permissions(everyone_role, send_messages=False)
    
        # Senden Sie eine Bestätigungsnachricht im Kanal
        if nachricht:
            embed = nextcord.Embed(
            title=f"Channel Locked",
            description=f"🔒 {nachricht}",
            color=nextcord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
        
        else:
            embed = nextcord.Embed(
            title=f"Channel Locked",
            description=f"🔒 Dieser Kanal wurde gesperrt von {interaction.user}.",
            color=nextcord.Color.red()
            )
            await interaction.response.send_message(embed=embed)             
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Channel zu verwalten.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)               
        await interaction.response.send_message(embed=embed, ephemeral=True)
            
            
            
@channel.subcommand(
    name="unlock",
    description="Entsperrt den aktuellen Kanal",
)
async def channel(
    interaction: Interaction,
    nachricht: str = SlashOption(
        name="nachricht",
        description="Eine optionale Nachricht, die beim Entsperren des Kanals angezeigt wird",
        required=False
    )
):
    if interaction.user.guild_permissions.manage_channels:
        # Setzen Sie die Berechtigungen für @everyone so, dass sie keine Nachrichten mehr senden können
        everyone_role = interaction.guild.default_role
        await interaction.channel.set_permissions(everyone_role, send_messages=True)

        # Senden Sie eine Bestätigungsnachricht im Kanal
        if nachricht:
            embed = nextcord.Embed(
            title=f"Channel Unlocked",
            description=f"🔓 {nachricht}",
            color=nextcord.Color.green()
            )
            await interaction.response.send_message(embed=embed)
        
        else:
            embed = nextcord.Embed(
            title=f"Channel Locked",
            description=f"🔓 Dieser Kanal wurde entsperrt von {interaction.user}.",
            color=nextcord.Color.green()
            )
            await interaction.response.send_message(embed=embed)
    else:
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Channel zu verwalten.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)               
        await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.slash_command(
    name="verify",
    description="verifiziert einen Member",
    guild_ids=[serverID]
    # brief="| shows Latency",
    # enabled=False
    # hidden=True
)
async def verify(interaction: nextcord.Interaction, member: nextcord.Member, reason):
    if interaction.user.guild_permissions.manage_roles:
        role = nextcord.utils.get(interaction.guild.roles, name="Members")
        await member.add_roles(role)

        user_embed = nextcord.Embed(
        title=f"",
        description=f"{member} wurde verifiziert",
        color=nextcord.Color.green()
        )
        user_embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)
        user_embed.set_footer(text=(f"Grund: {reason}"))
        await interaction.response.send_message(embed=user_embed, ephemeral=True)
        
        
        member_embed = nextcord.Embed(
        title=f"",
        description=f"Du wurdest **Verifiziert** von {interaction.user}",
        color=nextcord.Color.green()
        )
        member_embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)               
        await member.send(embed=member_embed)
        logger.info(f"{interaction.user.display_name} - verified @{member} - reason: [ {reason} ]")
    else:
        
        embed = nextcord.Embed(
        title=f"",
        description=f":x: Du hast nicht die Berechtigung, Mitglieder zu Verifiziern.",
        color=nextcord.Color.red()
        )
        embed.set_author(name=(f"Hey {interaction.user}!"), icon_url=interaction.user.avatar.url)               
        await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run(TOKEN)