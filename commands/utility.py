import datetime

import hikari
import lightbulb

plugin = lightbulb.Plugin("Utility")


@plugin.command
@lightbulb.command("ping", "Returns the latency from the bot to the Discord API")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    latency = ctx.bot.heartbeat_latency * 1000
    embed = hikari.Embed(
        title="🏓 Pong!",
        description=f"The current latency to the Discord API is `{latency:,.2f}ms`",
        colour=(151, 129, 225),
        timestamp=datetime.datetime.now().astimezone()
    )

    await ctx.respond(embed=embed)


@plugin.command
@lightbulb.option("text", "The text for the bot to repeat")
@lightbulb.command("echo", "Repeats the given text")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)
