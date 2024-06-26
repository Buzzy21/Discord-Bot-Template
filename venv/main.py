from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, app_commands
from random import randint

# Load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# Setup
intents = Intents.default()
client = Client(intents=intents)
tree = app_commands.CommandTree(client)

# Startup
@client.event
async def on_ready() -> None:
    await tree.sync()
    print(f'{client.user} is now running')

# Slash command
@tree.command(name="roll_dice", description="Rolls a dice")
async def roll_dice(interaction: discord.Interaction):
    result = randint(1, 6)
    await interaction.response.send_message(f'You rolled {result}.')

# Entry point
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()
