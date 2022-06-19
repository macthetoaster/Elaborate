import hikari
import lightbulb

plugin = lightbulb.Plugin("on_command_error")


@plugin.listener(lightbulb.events.SlashCommandErrorEvent)
async def on_command_error(event: lightbulb.events.SlashCommandErrorEvent):
    # Check for a MissingRequiredPermissions error
    if isinstance(event.exception, lightbulb.errors.MissingRequiredPermission):
        await event.context.respond(
            "You do not have the required permissions to execute this command. If you believe this "
            "to be an error, contact the server's owner.",
            flags=hikari.MessageFlag.EPHEMERAL
        )
    # Any other error will be thrown back to this else statement
    else:
        await event.context.respond(
            "There was an error while trying to run this command. Please check the stack trace or "
            "the logs for any further information. Current exception message is:"
            f" ```{event.exception}```",
            flags=hikari.MessageFlag.EPHEMERAL
        )


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)
