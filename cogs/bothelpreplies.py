import discord
from discord.ext import commands

class BotHelpCogV2(commands.Cog, name='Bot Help Replies'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        bot_help_ch = 711870218904928276

        if message.content == '>welcome':
            embedVar = discord.Embed(title="<:squirtlewave:847736706433941534>  Welcome to Zeraora\'s Emporium!", color=0xe74c3c)
            embedVar.add_field(name="Our Website:", value="https://zeraorasemporium.com/", inline=False)
            embedVar.add_field(name="Instruction Video (Skip to `1:38`)", value="https://www.youtube.com/watch?v=4Acz6oHSjQ8", inline=False)
            await message.channel.send(embed=embedVar)

        if message.channel.id == bot_help_ch and '$trade' not in message.content.lower():

            channel = self.bot.get_channel(bot_help_ch) # set this to whatever channel you want it to read, should be "bot_help_ch" for normal usage

            if (((message.author._roles.has(719622176634044577) or message.author._roles.has(711901391555264514) 
            or message.author._roles.has(711901311234474054) or message.author._roles.has(896746951733805066)) 
            and '!' not in message.content) or message.author == self.bot.user or message.author.bot): # bot helper, mod, admin, and founder roles
                return

            # Actual Replies Begin Here

            if ('notrainerfound' in message.content.lower() or (('cant' in message.content.lower() or 'can\'t' in message.content.lower() 
            or 'wont' in message.content.lower() or 'won\'t' in message.content.lower()) and 'trade' in message.content.lower() 
            or 'connect' in message.content.lower())):
                if 'lan' in message.content.lower():

                    lan_reply = '''
**01)** Make sure you have the **lan-play-win64.exe** file running __AS ADMINISTRATOR__ and connect to **emporium.ddns.net:11451.**\n
**02)** Make sure you have your Switch's current WiFi modified with a random IP between **10.13.0.1 - 10.13.255.254.**\n
**03)** Make sure your Switch's WiFi's __Subnet Mask__ is set to **255.255.0.0.**\n
**04)** Make sure your Switch's WiFi __Gateway__ is set to **10.13.37.1.**\n
**05)** You can set your __Primary DNS__ to **1.1.1.1** and __Secondary DNS__ to **1.0.0.1.**
-- or choose any DNS you'd like, including 90DNS, which blocks connecting to Nintendo's servers, but may cause connection issues.\n
**06)** In the Switch, go to *System Settings > Internet > Test Connection* to make sure you have 3 green checks.\n
**07)** Enter Sword/Shield, press **X**, then enter **Options**, then simultaneously push **R-Shoulder + L-Shoulder + L-Stick.**\n
**08)** Now that you're in LAN Mode, test your connection again like in Step 06.\n
**09)** You should now see a bunch of text in the **lan-play-win64.exe** window.\n
**10)** If you see **IConnection::IConnection** in the window in Step 09, you're connected and can begin trading.
'''

                    embedVar = discord.Embed(title="**__LAN TROUBLESHOOTING__**", description=lan_reply, color=0xe74c3c)
                    await message.channel.send(embed=embedVar)
                    return
                else:
                    await message.channel.send('Make sure you\'re connected to the internet, and restart your switch')
                    await message.channel.send('It may also be worth doing a NAT test, Nintendo recommends Type A or B\nhttps://en-americas-support.nintendo.com/app/answers/detail/a_id/22462/~/how-to-use-the-internet-connection-test')
                    return

            if (('find' in message.content.lower() or 'know' in message.content.lower()) and ("tid" in message.content.lower() or "sid" in message.content.lower())) and 'pkhex' not in message.content.lower() and 'SID:' not in message.content:

                sid_desc = '''1) Type "$trade <Pokemon>" into one of the bots.
                2) Wait for your DM from the bot with a Link Trade Code.
                3) Once received, enter Link Trade Code in Switch.
                4) Trade a Pokemon you caught yourself in-game to the bot.
                5) Receive the trade request until it's finished.
                6) Upon finishing, the bot will send you a PKM file of what you traded it.
                7) Download the PKM and use PKHeX to view SID (Windows only) or upload the PKM file in one of the bot channels without any commands.'''

                embedVar = discord.Embed(title="HOW TO OBTAIN YOUR SID", description=sid_desc, color=0xe74c3c)
                await message.channel.send(embed=embedVar)

                return

            if "how" in message.content.lower():
                if "ribbons" in message.content.lower() or "ribbon" in message.content.lower():
                    await message.channel.send('Hello! This is an example of adding ribbons to your showdown format. See this link for all ribbons: https://pastebin.com/EwtkQYrx')
                    embedVar = discord.Embed(title="Advanced Customization", description="Ribbon Batch Commands Example", color=0xe74c3c)
                    embedVar.add_field(name="Ribbon Customization", value="Aerodactyl (M) @ Life Orb \nLevel: 100 \nAdamant Nature \nBall: Moon\n.RibbonEffort=true\n.RibbonBestFriends=true")
                    embedVar.add_field(name="Or you can add all the legal ones!", value="Aerodactyl (M) @ Life Orb \nLevel: 100 \nAdamant Nature \nBall: Moon\n.Ribbons=$SuggestAll")
                    await message.channel.send(embed=embedVar)
                    return
                elif ("to make" in message.content.lower() or 'i make' in message.content.lower() or 'make it' in message.content.lower()) and 'alpha' in message.content.lower():
                    await message.channel.send('The formatting for making a pokemon alpha is `Alpha: Yes`. Please note that capitalization does matter. Please note that certain pokemon have to have a minimum level to be alpha')
                    return
                elif ((' do ' in message.content.lower()) or ' can ' in message.content.lower()) and 'lan' not in message.content.lower() and 'acnh' not in message.content.lower() and 'masterball' not in message.content.lower(): 
                    if "belle" in message.content.lower() or "acnh" in message.content.lower():
                        await message.channel.send('This is how Belle works: https://zeraorasemporium.com/#acnh')
                        return

                    elif 'trade' in message.content.lower() and 'bdsp' in message.content.lower():
                        await message.channel.send('This is how you trade in BDSP')
                        await message.channel.send('https://cdn.discordapp.com/attachments/711870218904928276/915333900128112640/ze-pokemon-diamond-pearl-bot-info.png')
                        return

                    #elif 'egg' in message.content.lower():
                        #await message.channel.send('Ahoy! You can trade an egg using the format posted on our website https://zeraorasemporium.com/#egg\nThe BDSP bots will trade eggs in BDSP now using the same format, and you can include egg moves!')
                        #return
                elif ('how' in message.content.lower() or 'where' in message.content.lower) and ('pins' in message.content.lower() or 'pinnned' in message.content.lower()):
                    await message.channel.send('To find the pins on the PC/Web client look to the top right near the search bar for a icon that looks like a pushpin. To find them on mobile tap the icon that looks like two people at the top right, then the icon that looks like a pushpin')
                    return
                
                else:
                    pass

            if (("access" in message.content.lower() or "permission" in message.content.lower() or "type" in message.content.lower()) 
                 and "bot" in message.content.lower() or "read only" in message.content.lower()):
                await message.channel.send('If you cannot type in a bot channel, please ensure I have not sent a message saying the bot is broken.')
                return

            if (("lets go" in message.content.lower() or "let\'s go" in message.content.lower()) or "lgpe" in message.content.lower()) and 'bot' in message.content.lower():
                await message.channel.send('There are no Pokémon: Let\'s Go, Pikachu/Eevee sysbots, maybe google can help you search!')
                return

            if (('cancel' in message.content.lower() or 'stop' in message.content.lower() or 'leave' in message.content.lower()) and 
                ('trade' in message.content.lower() or 'queue' in message.content.lower())):
                await message.channel.send('Howdy! The command to leave the queue is `$qc` You can find the bot commands on our website https://zeraorasemporium.com/#bot')
                return

            if ('nso ' in message.content.lower() or 'online' in message.content.lower()) and 'need' in message.content.lower():
                await message.channel.send(message.author.mention +' You do need Nintendo Switch Online to trade with the bots, but not for the LAN bot')
                return

            if 'add' in message.content.lower() and ('pokerus' in message.content.lower() or 'pokérus' in message.content.lower()):
                await message.channel.send('Add this text to your format above the moves:\n```\n.PKRS_Infected=true\n.PKRS_Cured=false\n```')
                return

            if "ball" in message.content.lower() and ("change" in message.content.lower() or "pick" in message.content.lower()):
                await message.channel.send(message.author.mention +' <:squirtlewave:847736706433941534> Hello! This is how you customize the ball.')
                embedVar = discord.Embed(title="Custom Ball", description="Ball: Moon", color=0xe74c3c)
                embedVar.add_field(name="Example for SwSh and BDSP", value="Aerodactyl (M) @ Life Orb \nLevel: 100 \nAdamant Nature \nBall: Moon")
                embedVar.add_field(name="Example for PLA", value="Growlithe-Hisui (M)\nLevel: 100 \nAdamant Nature \nBall: LAUltra")
                await message.channel.send(embed=embedVar)
                return

            if "Ball: Poké" in message.content:
                await message.channel.send('Use `Ball: Poke` instead! The bots do not read that as the name as the ball.')
                return

            if "Ball: LAPoké" in message.content:
                await message.channel.send('Use `Ball: LAPoke` instead! The bots do not read that as the name as the ball.')
                return

            if (("help me" in message.content.lower()) or "i need help" in message.content.lower()) and len(message.content) < 11:
                await message.channel.send('Hello! Here is the help menu, if what you need is not listed below please wait for one of our bot helpers to assist you')
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
                await message.channel.send(embed=embedVar)
                await message.channel.send("Note: zeraoraermproium website links will not work currently. Please ask a more specific question so a bot helper can answer.")
                return

            if "list" in message.content.lower() and ("acnh" in message.content.lower() or "items" in message.content.lower()):
                embedVar = discord.Embed(title="ACNH Items", description="All items in Animal Crossing", color=0xe74c3c)
                embedVar.add_field(name="Animal Crossing New Horizon item", value="[Item list](https://mpql.net/tools/acnh/codes/item-list)")
                await message.channel.send(embed=embedVar)
                return

            #if "qs" in message.content.lower() or "ts" in message.content.lower():
            #    await message.channel.send("The $qs and $ts commands have been blocked from being sent in this server because the channels are getting too cluttered. You can use the $qs and $ts commands in the bot's DMs.")

async def setup(bot):
    await bot.add_cog(BotHelpCogV2(bot))  
