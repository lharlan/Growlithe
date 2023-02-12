from discord.ext import commands
import datetime
import pytz

def CheckTime():
    # get time for time check
    now = datetime.datetime.now(tz = pytz.timezone('America/Denver'))
    current_hour = int(now.strftime("%H"))
    current_minute = int(now.strftime("%M"))

    if (current_hour > 23 or (current_hour == 23 and current_minute > 30)) or (current_hour < 8 or (current_hour == 8 and current_minute < 30)):
        TimeResponse = 'Logan is currently sleeping. You shouldn\'t be pinging not helpers anyway so wait for someone else to help you.'
    else:
        TimeResponse = 'Do not ping staff or bot helpers in this channel. Logan, or another helper, will help you when they are free. *Be patient*.'

    return TimeResponse


class PingReplyCogV2(commands.Cog, name='Ping Replies'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        command_ch = 711862338382463067 
        pkhexuals_ch = 738917733915295774
        staff_ch = 764475971272704020
        gami_ch = 767842299958132806
        gami_manage_ch = 988601695032442980
        vouch_ch = 711875414825631744
        bothelp_ch = 711870218904928276
        spam_ch = 732792223162433646

        sv_chat_ch = 981546503699042304
        svtourney_ch = 711860459325882409

        logs_category = 711875828455178291

        zera_bot = 711864261952929814
        mew_bot = 778329754642022460
        muk_bot = 906881436622159952
        osha_bot = 771894077364764712
        amphy_bot = 914994177543143484
        belle_bot = 907705727647363092

        mod_role = 711901391555264514
        admin_role = 711901311234474054
        helper_role = 808269965589217300

        if message.guild == None:
            return

        # ignore bots, self, and logging channels
        elif (message.author == self.bot.user or
            message.author.bot or
            message.channel.category.id == logs_category):

            return
        
        if message.content.lower() == '>nice photoshop':
            await message.channel.send('https://cdn.discordapp.com/attachments/711862338382463067/1055625822549065828/FakeAssScreenshotLMAO.jpg')

        # ignore staff in sysbot channels for pinging owners
        elif (message.channel.id == zera_bot or
              message.channel.id == mew_bot or
              message.channel.id == muk_bot or
              message.channel.id == osha_bot or
              message.channel.id == amphy_bot or
              message.channel.id == belle_bot):

            if (message.author._roles.has(mod_role) or
                message.author._roles.has(admin_role) or
                message.author._roles.has(helper_role)):

                return

            else:
                pass

        # ignore staff channels, and other various ones where pinging is important
        elif (message.guild.id == 709788621896417370 and
              (message.channel.id != command_ch and
              message.channel.id != pkhexuals_ch and
              message.channel.id != staff_ch and
              message.channel.id != gami_ch and
              message.channel.id != gami_manage_ch and
              message.channel.id != svtourney_ch and
              message.channel.id != vouch_ch)):

            # Logan
            if ('<@!462273017284919326>' in message.content) or ('@462273017284919326' in message.content):
                if (message.author._roles.has(mod_role) or
                    message.author._roles.has(admin_role) or
                    message.author._roles.has(helper_role)):

                    await message.channel.send('<:slowshine:727863525007163452>')
                    return

                elif message.channel.id == bothelp_ch or message.channel.id == spam_ch:

                    await message.channel.send(CheckTime())
                    return

                else:
                    await message.channel.send('<:PepePingANGRY:812374407635796028>')
                    return

            # Simon
            if ('<@!686166019802136602>' in message.content or '@686166019802136602' in message.content) and message.channel.id != sv_chat_ch:
                await message.channel.send('You pinged Sentinel, he will teleport to you shortly.')
                return

            # Zac
            if '<@!243664830592974848>' in message.content or '@243664830592974848' in message.content:
                await message.channel.send('Why did you ping the Master Lurker? He aint lurking here, so go lurk your way to someone else.')
                await message.channel.send('<:SquirtleLurk:716251571998031902>')
                return

            # Cody
            if '<@!715239456839565416>' in message.content or '@715239456839565416' in message.content:
                await message.channel.send('<:Codyannoyed:883905727910019132>')
                return

            # K8
            if ('<@!664243806882889798>' in message.content or '@664243806882889798' in message.content):
                if message.author.id == 654910940629958656: # Solex
                    await message.channel.send('Hi Solex! K8 will be with you in a moment.')
                    return

                elif message.author.id == 388966638965489665: # DJ
                    await message.channel.send('https://tenor.com/view/venom-lick-creepy-tongue-out-gif-16647618')
                    return

                elif message.author.id == 462273017284919326: # Logan
                    await message.channel.send('<:grapekait:764571906740977764> ilu k8')
                    return

                else:
                    await message.channel.send('https://cdn.discordapp.com/attachments/821606367646580799/1048417327575740536/tinkaton_smash.gif')
                    return

            # Sec
            if ('<@!571475470940504065>' in message.content or '@571475470940504065' in message.content) and message.channel.id != sv_chat_ch:
                await message.channel.send('You\'re not supposed to ping staff. You\'re lucky Sec doesn\'t care or you\'d be sleeping with the fishes.')
                return

            # Igor
            if '<@!829091955333922826>' in message.content or '@829091955333922826' in message.content:
                await message.channel.send('Unless you are sitting with me gaming, beer in hand and chatting I can\'t be any use to you.')
                await message.channel.send('<:LucaPing:719619275836620841>')
                return

            # Snake
            if '<@!647221346170044514>' in message.content or '@647221346170044514' in message.content:
                await message.channel.send('Snake? Snake?! SNAAAAAKE!')
                return

            # Steve
            if '<@!710957723050836099>' in message.content or '@710957723050836099' in message.content:
                await message.channel.send('Steve\'s watching the super android 13 movie he will be with you in a moment.')
                return

            # Kenji
            if '<@!372050875570585601>' in message.content or '@372050875570585601' in message.content:
                await message.channel.send('<:RaichuBruh:873931531633192960>')
                return

            # Azula
            if '<@!352735435014930433>' in message.content or '@352735435014930433' in message.content:
                await message.channel.send('<a:Anezulurk:734145380849025044>')
                return

            # Viv
            if '<@!386801593535692811>' in message.content or '@386801593535692811' in message.content:
                await message.channel.send('<:harold:783526444336283688>')
                return

            # Kad
            if '<@!662067494332268544>' in message.content or '@662067494332268544' in message.content:
                await message.channel.send('<:bozjudge:1057057108106936401>')
                return

            # DJ
            if '<@!388966638965489665>' in message.content or '@388966638965489665' in message.content:
                await message.channel.send('https://cdn.discordapp.com/attachments/764475971272704020/1054590120298287235/eat_your_face.gif')
                return

            # Froggi
            if '<@!348292921163776020>' in message.content or '@348292921163776020' in message.content:
                await message.channel.send('Froggi\'s a hop and a croak away!')
                return

            # Shae
            if '<@!691433780438630401>' in message.content or '@691433780438630401' in message.content:
                if (message.author._roles.has(mod_role) or
                    message.author._roles.has(admin_role)):

                    await message.channel.send('<:grapeshae:855282710012755968>')
                    return
                else:
                    return

            # Omar
            if '<@!631166736322002978>' in message.content or '@631166736322002978' in message.content:
                await message.channel.send('')

        else:
            return

async def setup(bot):
    await bot.add_cog(PingReplyCogV2(bot))
