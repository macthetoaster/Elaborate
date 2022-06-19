import hikari
import lightbulb

plugin = lightbulb.Plugin("ban_command")

# Set the choices for the delete_messages parameter
no_messages = hikari.CommandChoice(
    value=0,
    name="Don't delete any"
)
one_day = hikari.CommandChoice(
    value=1,
    name="Previous 24 hours"
)
seven_days = hikari.CommandChoice(
    value=7,
    name="Previous 7 days"
)
delete_message_choices = [no_messages, one_day, seven_days]


@plugin.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.option(
    "user",
    "The user to ban from the guild",
    type=hikari.OptionType.USER,
    required=True
)
@lightbulb.option(
    "reason",
    "The reason for the ban",
    type=hikari.OptionType.STRING,
    required=False
)
@lightbulb.option(
    "delete_messages",
    "The amount of messages to delete, defaults to 7 days",
    choices=delete_message_choices,
    type=hikari.OptionType.INTEGER,
    required=False
)
@lightbulb.command("ban", "Bans a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban_command(ctx: lightbulb.Context) -> None:
    # Get the required parameters to ban the user
    user: hikari.User = ctx.options.user
    guild: hikari.Guild = ctx.get_guild()
    reason: str = ctx.options.reason or "No reason provided"
    delete_days = ctx.options.delete_messages or 7

    try:
        # Ban the user from the guild
        await guild.ban(user=user, reason=reason, delete_message_days=delete_days)
        # Send a response as feedback
        await ctx.respond(f"User **{user.username}#{user.discriminator}** has been banned for reason"
                          f" **{reason}**",
                          delete_after=10)
    except hikari.errors.ForbiddenError:
        await ctx.respond(
            "Could not ban the user due to missing permissions. Check that the "
            "bot's role is above the role you're trying to ban, or that the bot "
            "has kick permissions.",
            flags=hikari.MessageFlag.EPHEMERAL
        )

    # @TODO: Set up logging


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)
