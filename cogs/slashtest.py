import discord
from discord import app_commands
from discord.ext import commands

from typing import Literal, Optional
from discord.ext.commands import Greedy, Context

class SlashTestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('SlashTest Cog Ready')

    @commands.command(hidden=True)
    async def synchelp(self, ctx):
        await ctx.send('''`!sync` -> global sync
`!sync ~` -> sync current guild
`!sync *` -> copies all global app commands to current guild and syncs
`!sync ^` -> clears all commands from the current guild target and syncs (removes guild commands)
`!sync id_1 id_2` -> syncs guilds with id 1 and 2''')

    @commands.command(hidden=True)
    async def sync(
      ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        await ctx.message.add_reaction('\u2705')
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

    @app_commands.command(name='test', description='Test for slash commands.')
    async def test(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message('Test Worked! Inputted text was: {}'.format(question))

async def setup(bot):
    await bot.add_cog(SlashTestCog(bot), guilds=[discord.Object(id=821606210574614530)])