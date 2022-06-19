import hikari
import lightbulb

plugin = lightbulb.Plugin("kick_command")


@plugin.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.option(
    "user",
    "The user to kick from the guild",
    type=hikari.OptionType.USER,
    required=True
)
@lightbulb.option(
    "reason",
    "The reason for the kick",
    type=hikari.OptionType.STRING,
    required=False
)
@lightbulb.command("kick", "Kicks a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick_command(ctx: lightbulb.Context) -> None:
    # Get the required parameters to kick the user
    user: hikari.User = ctx.options.user
    guild: hikari.Guild = ctx.get_guild()
    reason: str = ctx.options.reason or "No reason specified"

    try:
        # Kick the user from the guild
        await guild.kick(user=user.id, reason=reason)
        # Send a response as feedback
        await ctx.respond(f"User **{user.username}#{user.discriminator}** has been kicked for reason"
                          f" **{reason}**",
                          delete_after=10)
    except hikari.errors.ForbiddenError:
        await ctx.respond(
            "Could not kick the user due to missing permissions. Check that the "
            "bot's role is above the role you're trying to kick, or that the bot "
            "has kick permissions.",
            flags=hikari.MessageFlag.EPHEMERAL
        )

    # @TODO: Set up logging


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)
