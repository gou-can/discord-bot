from discord.ext import commands
import DiscordUtils
from cmds.classes import CogExtension
from business import account_business


class Listener(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tracker = DiscordUtils.InviteTracker(self.bot)

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        pass
        # if interaction.custom_id == account_itmes.GenesisCodeItemCustomId:
        #     await account_business.send_genesis_code(interaction)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        await account_business.listen_alpha_role_add(self.guild, payload)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        await account_business.listen_alpha_role_remove(self.guild, payload)

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