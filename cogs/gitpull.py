from discord.ext import commands
from cogs.utils import checks
import requests
from requests.structures import CaseInsensitiveDict

# https://stackoverflow.com/questions/14120502/how-to-download-and-write-a-file-from-github-using-requests

def setURL(fileName):

    #example of fileName: "cogs/botaltfinder.py"
    repoURL = "https://raw.githubusercontent.com/lharlan/Growlithe/" + fileName

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "token TOKEN"

    return repoURL

class GitPullCog(commands.Cog, name='Growlithe Source Control'):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(checks.is_logan())
    @commands.command(name='')

async def setup(bot):
    await bot.add_cog(GitPullCog(bot))