import os

import lightbulb
from dotenv import load_dotenv

# Load the environment variables from .env and get the token from there
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
debug = os.getenv("DEBUG_MODE")

# Create a new bot instance
bot = lightbulb.BotApp(
    token=token
)

# If we're in debug mode, only register commands to the testing guild to save on time
if debug == "true":
    # Get the testing guild ID from the config
    testing_guild_id = os.getenv("TESTING_GUILD_ID")
    print(f"Elaborate is in Debug Mode! Current testing guild: {int(testing_guild_id)}")

    # Enable the registration of commands only in the testing guild
    bot.default_enabled_guilds = [int(testing_guild_id)]

# Load extensions from the different folders
bot.load_extensions_from("commands", must_exist=True, recursive=True)
bot.load_extensions_from("events", must_exist=True, recursive=True)

# Run the bot
bot.run()
