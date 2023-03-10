import discord
from discord.ext import commands
from cmds.classes import CogExtension
from business import dice


class Listener(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.tracker = DiscordUtils.InviteTracker(self.bot)

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        try:
            await dice.listen_steal_choice(interaction)
        except Exception as e:
            print("listen_steal_choice err", e)
        try:
            await dice.listen_steal_start(interaction)
        except Exception as e:
            print("listen_steal_start err", e)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)



async def setup(bot: commands.Bot):
    await bot.add_cog(Listener(bot))