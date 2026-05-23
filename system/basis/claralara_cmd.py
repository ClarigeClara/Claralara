# Claralara-Befehle | Claralara Commands
# Cog-ID: 001

# Importlisten | Import lists
import sys
import os
import asyncio
import claralara_config
import aiomysql
import discord
import random
import datetime
from claralara_config import Database, AdminaDatabase
from discord.commands import OptionChoice, SlashCommandGroup, option
from discord.ext import commands
from discord.ui import View

# Klasse für die Befehle von Claralara, die in diesem Cog definiert werden.
# Class for the commands of Claralara that are defined in this Cog.
class claralara_cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Befehlszähler-Funktion, die die Anzahl der Aufrufe eines Befehls in der Datenbank speichert.
    # Command-Name function that counts the number of times a command is called and stores it in the database.
    async def command_counter(self, command_name):
        # Claralara hat ihre eigene Datenbank, um Daten zu speichern.
        # Claralara has its own database to store data.
        clara = await aiomysql.connect(**Database)
        # Clara sucht in der Tabelle "command_counter" nach dem Befehl, um die aktuelle Anzahl zu erhalten.
        # Clara looks in the "command_counter" table for the command to get the current count.
        async with clara.cursor() as forefinger:
            await forefinger.execute('SELECT * FROM command_counter WHERE command = %s', (command_name,))
            command = await forefinger.fetchone()

            if command:
                # Clara aktualisiert die Anzahl um 1, wenn der Befehl bereits in der Tabelle vorhanden ist.
                # Clara updates the count by 1 if the command is already in the table.
                await forefinger.execute('UPDATE command_counter SET count = count + 1 WHERE command = %s', (command_name,))
            else:
                # Clara fügt den Befehl mit der Anzahl 1 hinzu, wenn er noch nicht in der Tabelle vorhanden ist.
                # Clara adds the command with the count of 1 if it is not already in the table.
                await forefinger.execute('INSERT INTO command_counter (command, count) VALUES (%s, 1)', (command_name,))

            # Clara speichert die Änderungen in der Datenbank und schließt die Verbindung.
            # Clara saves the changes to the database and closes the connection.
            await clara.commit()
        clara.close()

    # Claralara überprüft, ob der Benutzer oder die Server-ID gebannt ist.
    # Claralara checks if the user or server ID is banned.
    async def banned_check(self, Table, Columnname, Value):
        # Da Claralara zu Codestube gehört, wird die zentrale Datenbank von Codestube verwendet, die von "Codestube Admina" verwaltet wird.
        # Since Claralara belongs to Codestube, the central database of Codestube is used, which is managed by "Codestube Admina".
        clara = await aiomysql.connect(**AdminaDatabase)

        # Clara sucht in der angegebenen Tabelle nach dem Wert, um zu überprüfen, ob er gebannt ist.
        # Clara looks in the specified table for the value to check if it is banned.
        async with clara.cursor() as forefinger:
            query = f"SELECT {Columnname} FROM {Table} WHERE {Columnname} = %s"
            await forefinger.execute(query, (Value,))
            eintrag = await forefinger.fetchone()
            return eintrag is not None
        
    def command_requested(self, command, user, server):
        ConsolTimeStamp = datetime.datetime.now().strftime(claralara_config.konsole_date_format)
        Serverinformation = f"{server.name} ({server.id})" if server else "DM / No Guild"

        # In der Konsole wird angezeigt, welcher Befehl von welchem Benutzer auf welchem Server angefordert wurde.
        # In the console, it is displayed which command was requested by which user on which server.
        print(
            f"{ConsolTimeStamp} | Info » Command requested!\n"
            f"» {command}\n"
            f"» User: @{user} ({user.id})\n"
            f"» Guild: {Serverinformation}\n")
        
    def command_successful(self, command, user, server):
        ConsolTimeStamp = datetime.datetime.now().strftime(claralara_config.konsole_date_format)
        Serverinformation = f"{server.name} ({server.id})" if server else "DM / No Guild"

        print(
            f"{ConsolTimeStamp} | Info » Command successful!\n"
            f"» {command}\n"
            f"» User: @{user} ({user.id})\n"
            f"» Guild: {Serverinformation}\n")

    clara= SlashCommandGroup(name="claralara", 
                             description="Main commands for your digital best friend c:",
                             description_localizations={
                                 "de": "Hauptbefehle für deine digitale beste Freundin c:",
                                 "en-US": "Main commands for your digital best friend c:"
                             })
    system = SlashCommandGroup(name="devsystem", 
                               description="Top Secret: For Codestube developers only! 🛠️",
                               description_localizations={
                                   "de": "Top Secret: Nur für Entwickler der Codestube! 🛠️",
                                   "en-US": "Top Secret: For Codestube developers only! 🛠️"
                               },
                               guild_ids=[1464037346986168401],
                               has_role=[1484572551673020536, 1507738224871735437])


# /claralara about - Command: 001 - 01
    @clara.command(name="about",
                   name_localizations={
                       "de": "info",
                       "en-US": "about"
                   },
                   description="Erfahre mehr über mich.",
                   description_localizations={
                       "de": "Erfahre mehr über mich.",
                       "en-US": "Learn more about me."
                   })
    async def info(self, ctx):
        Command = "/claralara about"  # ⇽ This variable is also for a database entry. 
        Commandtext = "/claralara about"

        # Set default value for the Direct-Message-Command
        guild_id = ctx.guild.id if ctx.guild else 0
        guild_name = "Kein Server // No Server (DM-Command)"
        embed_colour = int("E67E22", 16)

        # Check if ctx.guild exits
        if ctx.guild:
            embed_colour = ctx.guild.me.top_role.colour
            guild_id = ctx.guild.id
            guild_name = ctx.guild.name

        # It is counted and documented that a user wants to use the command.
        await self.command_counter(Command)
        self.command_requested(Command, ctx.author, ctx.guild)

        # It is checked if the user is banned.
        if await self.ist_banned('banned_users', 'user_id', ctx.author.id):
            # Servicecode: 000-01-99 - This user is currently banned from using the bot.
            view = View()
            view.add_item(claralara_config.doku)
            view.add_item(claralara_config.server)
            view.add_item(claralara_config.invite_claralara)
            view.add_item(claralara_config.GitHub_Repo)
            embed = discord.Embed(color=0x7F0000)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            if ctx.interaction.locale.startswith("de"):
                embed.add_field(name=claralara_config.Error_title_DE,
                value="Du warst in der vergangenheit nicht wirklich lieb zu mir, deswegen scheiß ich auf deine Befehle!"
                inline=False)
            elif ctx.interaction.locale.startswith("en"):
                embed.add_field(name=claralara_config.Error_title_EN,
                value="You haven't been really nice to me in the past, so I don't care about your commands!"
                inline=False)
            else:
                embed.add_field(name=claralara_config.Error_title_EN,
                value="You haven't been really nice to me in the past, so I don't care about your commands!"
                inline=False)
            embed.set_footer(text=f"{claralara_config.Clientname} • {Command} • {claralara_config.EmbedVersion}")
            await ctx.respond(embed=embed, view=view, ephemeral=True)
            print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | ERROR\n» The User @{ctx.author.name} ({ctx.author.id}) cannot execute the command {Commandtext}!\n» Servicecode: 000-01-99 - This user is currently banned!\n")
            return

def setup(bot):
    bot.add_cog(claralara_cmd(bot))