import os

import lightbulb
from dotenv import load_dotenv

# Load the environment variables from .env and get the token from there
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = lightbulb.BotApp(
    token=token
)

bot.load_extensions_from("commands")
bot.run()
