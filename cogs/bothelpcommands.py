import discord
from discord.ext import commands

class BotHelpCommandCog(commands.Cog, name='Bot Help Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='notice')
    async def notice(self, ctx, arg=None):
        await ctx.message.delete()

        if arg == 'questions' or arg == 'q':
            await ctx.send('Questions are not to be asked in this channel. \n<#711870218904928276> is the proper channel for questions.')
        elif arg == 'showdown' or arg == 'sd':
            await ctx.send('This channel is not for posting showdown sets that can be used directly with the bots. Use $trade followed by your showdown format to trade with the bot. If there are no bots open, requesting a pkm file will not get you your pokemon any faster as you will still have to wait for the bot to open.')
        else:
            await ctx.send('Please use this channel for making requests only. File edits are to be posted in <#711870218904928276>. \nQuestions about the SysBots/PKHeX belong in <#711870218904928276>. \nThis is to keep this channel clean to make it easy for people to find their requests. You may include a \"Thank you\" in your request messages, or use <#711875414825631744> to give bot helpers your thanks')

    # encounter database command
    @commands.command(name='ecdb', help='encounter database help')
    async def ecdb(self, ctx):
        await ctx.send('''Use the encounter database in PKHeX (Tools > Data > Encounter Database, or press ctrl + n) enter your search options, then right click > view to send to the main window
It will give you a legal blank slate of a Pokemon that you can use to edit how you want''')

    # mystery gift database
    @commands.command(name='mgdb', help='mystery gift database help')
    async def mgdb(self, ctx):
        await ctx.send('''Use the mystery gift database in PKHeX (Tools > Data > Mystery Gift Database, or press ctrl + g) enter your search options, then right click > view to send to the main window
It will give you all the event pokemon. You can also add new events that have released after a PKHeX update by adding a 
folder in the same folder as your `PKHeX.exe` called `mgdb` and adding `.wc8` files, and restarting PKHeX''')

    # quick link to batch command list, might be useful for helpers
    @commands.command(name='bc', help='Gives a link to the batch command pastebin, say ribbon for the ribbons and command for all commands')
    async def batchcommand(self, ctx, arg):
        if arg == 'command' or arg == 'c':
            await ctx.send('All batch commands: https://pastebin.com/HixDtDxc')
        elif arg == 'ribbon' or arg == 'r':
            await ctx.send('All ribbons/game version values: https://pastebin.com/EwtkQYrx')
        elif arg == 'bdspmet':
            await ctx.send('BDSP Met Location Values: https://pastebin.com/Fk77w1NR\nThis')
        elif arg == 'plamet':
            await ctx.send('PLA Met Location Values: https://pastebin.com/3pTsquW1')
        elif arg == 'svmet':
            await ctx.send('SV Met Location Values: https://pastebin.com/UNE9brU7')
        else:
            await ctx.send('Enter a valid argument: `c/command`, `r/ribbon`, `bdspmet`, `plamet`, `svmet`')

    # nat test command
    @commands.command(name='nat', help='displays the nat test link and informatio')
    async def nat(self, ctx):
        await ctx.send('Nintendo recommends NAT type A or B for the best trading experience\nhttps://en-americas-support.nintendo.com/app/answers/detail/a_id/22462/~/how-to-use-the-internet-connection-test')

    @commands.command(name='tryandsee')
    async def tryandsee(self, ctx):
        await ctx.send('https://tenor.com/view/try-it-and-see-give-it-a-try-try-try-and-see-try-it-yourself-gif-24095805')

    # website linker command
    @commands.command(name='web', help='will link a page on our website given a proper argument\npk8, acnh, egg, lan, lanfaq, intructions, and showdown')
    async def web(self, ctx, arg):
        if arg == 'pk8':
            await ctx.send('https://zeraorasemporium.com/#pk8')
            return
        elif arg == 'acnh' or arg == 'ac':
            await ctx.send('https://zeraorasemporium.com/#acnh')
            return
        elif arg == 'egg':
            await ctx.send('https://zeraorasemporium.com/#egg')
            return
        elif arg == 'lan':
            await ctx.send('https://zeraorasemporium.com/#laninfo')
            return
        elif arg == 'lanfaq' or arg == 'lf':
            await ctx.send('https://zeraorasemporium.com/#lanfaq')
            return
        elif arg == 'instructions' or arg == 'ins':
            await ctx.send('https://zeraorasemporium.com/#instructions')
            return
        elif arg == 'sd' or arg == 'showdown':
            await ctx.send('https://zeraorasemporium.com/#showdown')
            return
        elif arg == 'batch' or arg == 'bc':
            await ctx.send('https://zeraorasemporium.com/#batch')
            return
        elif arg == 'mobile':
            await ctx.send('http://zeraorasemporium.com/#mobile')
            return
        elif arg == 'pkhex':
            await ctx.send('https://projectpokemon.org/home/files/file/1-pkhex/')
            return
        elif arg == 'alm':
            await ctx.send('https://github.com/architdate/PKHeX-Plugins/releases')
            return
        elif arg == 'bdsp':
            await ctx.send('https://zeraorasemporium.com/#bdsp')
            return
        elif arg == 'acnhcodes':
            await ctx.send('https://mpql.net/tools/acnh/codes/item-list/')
            return
        elif arg == 'lanswitch':
            await ctx.send('http://lan-play.com/install-switch')
            return
        elif arg == 'teambuilder' or arg == 'tb':
            await ctx.send('https://play.pokemonshowdown.com/teambuilder')
            return
        elif arg == 'sid' or arg == 'SID':
            await ctx.send('https://zeraorasemporium.com/#sid')
            return
        elif arg == 'plalocations' or arg == 'plal':
            await ctx.send('https://pastebin.com/3pTsquW1')
            return
        elif arg == 'sysbot' or arg == 'sb':
            await ctx.send('https://github.com/kwsch/SysBot.NET')
            return
        else:
            await ctx.send('''https://zeraorasemporium.com\nIf you\'re looking for what agruments I accept: `pk8`, `acnh`, `egg`, 
`lan`, `lanfaq`, `intructions`, `showdown`, `batch`, `mobile`, `pkhex`, `alm`, `bdsp`, `acnhcodes`, `lanswitch`, `teambuilder`, `plalocations`, `sysbot`, and `sid`''')

    @commands.command(name='helpmenu', help='displays the help menu')
    async def helpmenu(self, ctx):
        embedVar = discord.Embed(title="Help Menu", description="Instructions", color=0xe74c3c)
        embedVar.add_field(name="Instruction Video", value="[Video](https://zeraorasemporium.com/#start)")
        embedVar.add_field(name="Showdown Format", value="[Formatting](https://zeraorasemporium.com/#showdown)")
        embedVar.add_field(name="Egg Creation", value="[Eggs](https://zeraorasemporium.com/#egg)")
        embedVar.add_field(name="Create PKM Files", value="[with PKHeX](https://zeraorasemporium.com/#create)")
        embedVar.add_field(name="How to obtain your SID/TID", value="[Secret and Trainer ID](https://zeraorasemporium.com/#sid)")
        embedVar.add_field(name="#Requests", value="[PKM File Requests](https://zeraorasemporium.com/#request)")
        embedVar.add_field(name="Batch Commands", value="[More customization](https://zeraorasemporium.com/#batch)")
        embedVar.add_field(name="Bot Commands", value="[All the bot commands you need](https://zeraorasemporium.com/#bot)")
        embedVar.add_field(name="Locked Pokèmon", value="[Shiny locked and blocked](https://zeraorasemporium.com/#blocked)")
        embedVar.add_field(name="Uploading PKM files using iOS/Android", value="[Mobile device support](https://zeraorasemporium.com/#mobile)")
        await ctx.send(embed=embedVar)

    @commands.command(name='bothelp', help='lets the user know the channel is bothelp and not anything else')
    async def bothelp(self, ctx):
        await ctx.message.delete()
        await ctx.send('This channel is for help and discussion regarding the SysBots/PKHeX. Please refrain from using this channel for other topics.')

    @commands.command(name='plaformat')
    async def hisuiforms(self, ctx):
        embedVar = discord.Embed(title="PLA Specific Showdown Formatting", color=0xe74c3c)
        embedVar.add_field(name='For Basculin and Basculegion', value='  Basculin-White\n  Basculegion-M or Basculegion-F', inline=False)
        embedVar.add_field(name='For Hisui Regional Variants', value='  Species-Hisui, Example: Samurott-Hisui', inline=False)
        embedVar.add_field(name='For New Pokemon', value='  Just use their name like normal, Example: Kleavor', inline=False)
        embedVar.add_field(name='For Alpha Pokemon', value='  Alpha: Yes', inline=False)
        embedVar.add_field(name='To Meet Evolution Requirements', value='Certain Pokemon have evolution requirements, such as Basculin-White needing 294 damage, you can add `.FormArgument=XX` to the format, whether it\'s 294 for Basculin-White, or 20 for Stantler\'s Psyshield Bash requirement', inline=False)

        await ctx.send(embed=embedVar)

    @commands.command(name='gvcalc')
    async def gvcalc(self, ctx, IVint=0, GVint=-1):
        # checks there are values
        if IVint == 0 or GVint == -1:
            await ctx.send('You must input values for the IVs and/or GVs, format for this command is `&gvcalc <IV> <GV>`')
            return

        # check values are valid
        if (IVint < 0 or IVint > 31) or (GVint < 0 or GVint > 10):
            await ctx.send('IVs are between 0 and 31, GVs are between 0 and 10')
            return

        if IVint == 31:
            GVdiff = 3
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

        if IVint <= 30 and IVint >= 26:
            GVdiff = 2
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

        if IVint <= 25 and IVint >= 20:
            GVdiff = 1
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

        if IVint <= 19 and IVint >= 0:
            GVdiff = 0
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

    @commands.command(name='examplepla')
    async def examplepla(self, ctx):
        embedVar = discord.Embed(title="Showdown PLA Format", color=0xe74c3c)
        embedVar.add_field(name="Example:", value="""$trade Growlithe-Hisui
        Adamant Nature
        Alpha: Yes
        Shiny: Yes
        Ball: LAGigaton
        OT: Logan
        OTGender: Female
        TID: 015775
        SID: 2161
        IVs: 0 SpA
        Level: 85
        - Rock Slide
        - Crunch
        - Aerial Ace
        - Iron Tail""")

        await ctx.send(embed=embedVar)

    @commands.command(name='filetype')
    async def filetype(self, ctx):

        embedVar = discord.Embed(title="PKM File Types And Their Supported Games", color=0xe74c3c)
        embedVar.add_field(name='.pk8', value='Sword and Shield', inline=False)
        embedVar.add_field(name='.pb8', value='Brilliant Diamond and Shining Pearl', inline=False)
        embedVar.add_field(name='.pa8', value='Pokemon Legends: Arceus', inline=False)
        embedVar.add_field(name='.pk9', value='Scarlet and Violet', inline=False)
        embedVar.set_footer(text='Applies only to the games supported by our SysBots, other games have different file types')

        await ctx.send(embed=embedVar)

    @commands.command(name='shinylock')
    async def shinylock(self, ctx, gamearg=None):

        if gamearg == None:
            await ctx.send('Argument missing, valid arguments are `swsh`, `bdsp`, or `pla`')
        elif gamearg == 'swsh':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/973760116602064926/ze-pokemon-sword-shield-shiny-locked.jpg')
        elif gamearg == 'bdsp':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/973760116602064926/ze-pokemon-sword-shield-shiny-locked.jpg')
        elif gamearg == 'pla':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/973760116157448322/ze-pokemon-legends-arceus-shiny-locked.jpg')
        elif gamearg == 'sv':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/1053514583043739678/SHINY__LOCK_SV.jpg')
        else:
            await ctx.send('Invalid argument, valid arguments are `swsh`, `bdsp`, `pla`, or `sv`')
            return

    @commands.command(name='gamelang')
    async def gamelang(self, ctx):
        lang_desc = "This goes below the species and above the moves.\nPut any of these in the place of `LanguageHere`:\nJapanese\nEnglish\nFrench\nItalian\nGerman\nSpanish\nKorean\nChineseS\nChineseT"
        embedVar = discord.Embed(title="Languages for the showdown format:", color=0xe74c3c)
        embedVar.add_field(name='`Language: LanguageHere`', value=lang_desc, inline=False)

        await ctx.send(embed=embedVar)

    @commands.command(name='susact')
    async def susact(self, ctx):
        await ctx.send('Getting a Suspicious Activity message means you\'re trading between two different in-game characters/saves too quickly, intentional or not. The time to wait is 2 hours due to increased accounts trading to mutliple saves.')

    @commands.command(name='levelformat')
    async def levelformat(self, ctx):
        await ctx.send('`.CurrentLevel=` should only be used for level 50, and requires the period before hand, any other level needs to use the regular `Level: ` formatting, otherwise the level may be defaulted to 100')

    @commands.command(name='botsbeback')
    async def botsbeback(self, ctx):
        await ctx.send('The bots will be back when the owner can fix them, whenever that may be. *I* also sent a message in the bot channel stating the same thing') 

    @commands.command(name='whoaredevs')
    async def whoaredevs(self, ctx, link=None):
        await ctx.send('No one in this server is responsible for the development of PKHeX, The Pokemon SysBots, or the Animal Crossing Sysbots, no one here can comment on \'When will there be support for this game\' or \'When will this get fixed/changed\'. The devs work on their own time for free, and never provide an ETA on updates/fixes.')

        if link == 'link':
            await ctx.send('https://discord.gg/tDMvSRv')
        else:
            pass
        
    @commands.command(name='sid', aliases=['tid'])
    async def sid(self, ctx):

        sid_desc = '''1) Type "$trade <Pokemon>" into one of the bots.
        2) Wait for your DM from the bot with a Link Trade Code.
        3) Once received, enter Link Trade Code in Switch.
        4) Trade a Pokemon you caught yourself in-game to the bot.
        5) Receive the trade request until it's finished.
        6) Upon finishing, the bot will send you a PKM file of what you traded it.
        7) Download the PKM and use PKHeX to view TID/SID (Windows only) or upload the PKM file in one of the bot channels without any commands.
        *if the bot does not print out your trainer information upload the pkm file to <#711870218904928276> and a bot helper will tell you your TID/SID'''

        embedVar = discord.Embed(title="HOW TO OBTAIN YOUR TID/SID", description=sid_desc, color=0xe74c3c)
        await ctx.send(embed=embedVar)

    @commands.command(name='lantroubleshoot', aliases=["lants", "lantrouble"])
    async def lantroubleshoot(self, ctx):

        faq1_desc = "The bot is online but you are not able to find it, likely because of a problem on your end. Make sure you followed all steps from the instructions carefully."
        faq2_desc = "Make sure you have WinPcap installed (restart if you\'ve just installed it too), then open lan-play-win64.exe (As Administrator for Windows) and connect to `emporium.ddns.net:11451`, then connect to the network in your switch."
        faq3_desc = "`client err: -14` means you have multiple instances of the lan program running at the same time. Use `ctrl` + `c` to close lan play when you\'re done using it and not the X at the top. You'll either have to fully restart your PC or manually kill the instances of lan play."

        embedVar = discord.Embed(title="LAN Trading Troubleshooting", color=0xe74c3c)
        embedVar.add_field(name="I can\'t connect to the bot! It said \"NoTrainerFound\".", value=faq1_desc, inline=False)
        embedVar.add_field(name="When I test my network settings after I configured the IP on my Switch, I get a DNS error or some other connection error.", value=faq2_desc, inline=False)
        embedVar.add_field(name="I see `client err: -14` in the lan play program and I cannot connect to the bot.", value=faq3_desc, inline=False)
        await ctx.send(embed=embedVar)

    @commands.command(name='dittoformat')
    async def dittoformat(self, ctx):

        embedVar = discord.Embed(title="Ditto Formatting for 6 IVs", description="Other formatting can be used such as `Shiny: Yes`.", color=0xe74c3c)
        embedVar.add_field(name="SwSh:", value="$trade Ditto\n=Generation=7", inline=False)
        embedVar.add_field(name="BDSP:", value="$trade Ditto\n=IVTotal=186", inline=False)
        embedVar.add_field(name="PLA:", value="Ditto is not in the game", inline=False)
        embedVar.add_field(name="SV:", value="$trade Ditto\n.Met_Location=28", inline=False)
        await ctx.send(embed=embedVar)

    @commands.command(name='lanvid')
    async def lanvid(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=5PH2LZzUVfQ")

    @commands.command(name='botbug')
    async def botbug(self, ctx):
        await ctx.send('These bots are experimental (as per mentioned in our announcement) so there will be issues occasionally and that is a risk you must take. If you want a more stable bot wait till the bot devs improve the bot.')

async def setup(bot):
    await bot.add_cog(BotHelpCommandCog(bot))
