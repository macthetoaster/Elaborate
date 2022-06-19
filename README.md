# Elaborate
A multipurpose Discord bot written in Python

## Libraries
This bot is written using some lovely libraries made by the community. Please check them out for any documentation on
how to use them properly! Here are their links if you're interested:
* [Hikari](https://github.com/hikari-py/hikari)
* [Lightbulb](https://github.com/tandemdude/hikari-lightbulb)

## Running the bot
Assuming you already have a bot account on the [Discord Developer Portal](https://discord.com/developers/docs/intro),
all you need to do is create a new file called `.env` in the main project folder, and add the following to it, and
replace the text with the respective tokens or variables to your liking:
```
DISCORD_TOKEN="Your_Discord_Token_Here"
DEBUG_MODE="true"
TESTING_GUILD_ID="Testing_Guild_ID_Here"
```

After that, we need to create a Python virtual environment for the bot to run in. This can easily be done by going to
the project folder within a terminal window and executing the following commands.

### Windows
```commandline
python -3 -m venv venv
venv/Scripts/activate
```

### Linux
```commandline
python3 -m venv venv
source venv/bin/activate
```

Once you have your virtual environment running (you'll also see a new folder appears called `venv`), you can just run
the `python main.py` command to start up the bot. Make sure you're using the correct Python version, which should be
3.8 or higher.

Once that is all done and dusted, the bot should be logged into the bot account that you set the token for, and the
commands should register within 1-5 hours if they're set globally or instantly if they're set per-guild. Keep in mind
you can set this up by going to the Lightbulb docs and using the decorator for guild on top of the commands.
