from discord.ext import commands
# import DiscordUtils
from cmds.classes import CogExtension
from business import account_business


class Listener(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.tracker = DiscordUtils.InviteTracker(self.bot)

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)
        result = await self.tracker.fetch_inviter(member)
        print("inviter.id", result.id)
        print("member.id", member.id)
        print("inviter.id", result)
        print("member.id", member)


async def setup(bot: commands.Bot):
    await bot.add_cog(Listener(bot))