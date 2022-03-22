#importing everything in the world that exists
import random
import discord
import time
import json
import datetime
from discord import Game
from discord.ext import commands
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from moneyy import add_money
from moneyy import remove_money
from moneyy import find_money
from fish import add_member
from fish import change_rod
from fish import add_fish
from fish import remove_fish
from fish import find_fish
from forage import add_forage_member
from forage import add_forageable
from forage import remove_forageable
from forage import find_forageable
from location import add_location_member
from location import change_location
from location import find_location
from tools import add_tool_member
from tools import change_tool
from tools import find_tool
from unlocked import add_unlocked_member
from unlocked import unlock_location
from unlocked import find_location_lock

#setting prefix and other sh*t
client = commands.Bot(command_prefix = '$', case_insensitive = True)
client.remove_command('help')

#wtf is this
epoch = datetime.datetime.utcfromtimestamp(0)

#some arrays for random.choice later on
giveornot = ['yes', 'no']
nophrases = [': no', ': i lost all my coins by gambling all', ": i'm not letting you gamble all", ": hahahaA no", ": well yes but actually no", ": I need coins to buy more stardew valley assets"]
rarepeople = ['Abathur', 'Kerrigan']
veryrarepeople = ['Unacorn', 'Art3mis', 'Cinnamon', 'Bubs', 'Fireboard']
kindararepeople = ['Bouncer', 'Gil', 'Governer', 'Grandpa', 'Gunther', 'Henchman', 'Marlon', 'Morris', 'Mr. Qi']
uncommonpeople = ['Alex', 'Elliott', 'Harvey', 'Sam', 'Sebastian', 'Abagail', 'Emily', 'Haley', 'Leah', 'Maru', 'Penny']
commonpeople = ['Caroline', 'Clint', 'Demetrius', 'Dwarf', 'Evelyn', 'George', 'Gus', 'Jas', 'Jodi', 'Kent', 'Krobus', 'Lewis', 'Linus', 'Marnie', 'Pam', 'Pierre', 'Robin', 'Sandy', 'Vincent', 'Willy', 'Wizard']

coinplaces = ["Xel'Naga", "Bunker", "Warp Prism", "Overlord"]
nocoinplaces = ["Medivac", "Planetary Fortress", "Photon Cannon", "Spine Crawler", "Mineral Fields"]
allplaces = ['coinplaces', 'nocoinplaces']

commonfish = {"carp": "<:Carp:749446750703452180> `Carp`", 'chub': '<:Chub:749446750426628137> `Chub`', 'anchovy': '<:Anchovy:749446750678286397> `Anchovy`', 'sardine': '<:Sardine:749446752351944714> `Sardine`', 'herring': '<:Herring:749446751051579402> `Herring`', 'smallmouth bass': '<:Smallmouth_Bass:749446752528236554> `Smallmouth Bass`', 'sunfish': '<:Sunfish:749446752482099231> `Sunfish`', 'seaweed': '<:Seaweed:749449308528574494> `Seaweed`', 'green algae': '<:Green_Algae:749449290459512933> `Green Algae`'}
rarefish = {'shad': '<:Shad:749446752226246689> `Shad`', 'halibut': '<:Halibut:749446751005704192> `Halibut`', 'flounder': '<:Flounder:749446751303368814> `Flounder`', 'Bullhead': '<:Bullhead:749446513255776287> `Bullhead`', 'largemouth bass': '<:Largemouth_Bass:749438072499863663> `Largemouth Bass`'}
epicfish = {'eel': '<:Eel:749446750925750333> `Eel`', 'catfish': '<:catfish:745567855038169108> `Catfish`'}
legfish = {'legend': '<:Legend:749446751181865020> `Legend`', 'mutant carp': '<:Mutant_Carp:749446751349506119> `Mutant Carp`'}

commonfishocean = ["seaweed", "anchovy", "sardine", "herring"]
commonfishlake = ["green algae", "chub", "carp"]
commonfishriver = ["green algae", "chub", "smallmouth bass", "sunfish"]
commonfishsewer = ["carp"]

rarefishocean = ["halibut", "flounder"]
rarefishlake = ["bullhead", "largemouth bass"]
rarefishriver = ["bream", "shad"]

epicfishocean = ['eel']
epicfishriver = ['catfish']

legfishlake = ['legend']
legfishsewer = ['mutant carp']

locations = ["lonely stone", "farm", "farmhouse", "backwoods", "bus stop", "town square", "sewers", "blacksmith", "community center", "clinic", "jojamart", "museum", "general store", "saloon", "beach", "fish shop", "tide pools", "forest", "secret woods", "ranch", "wizard's tower", "mountain", "carpenter", "railroad", "spa", "mines", "quarry", "adventurer's guild", "desert", "oasis", "casino", "skull cavern", "mutant bug lair", "witch's hut"]
locationmap = {"farm": ["farmhouse", "backwoods", "bus stop", "forest"], "farmhouse": ["farm"], "backwoods": ["farm", "mountain"], "bus stop": ["farm", "town square", "desert"], "town square": ["bus stop", "sewers", "blacksmith", "community center", "clinic", "jojamart", "museum", "general store", "saloon", "beach", "forest", "mountain"], "sewers": ["mutant bug lair", "forest", "town square"], "blacksmith": ["town square"], "community center": ["town square"], "clinic": ["town square"], "jojamart": ["town square"], "museum": ["town square"], "general store": ["town square"], "saloon": ["town square"], "beach": ["town square", "fish shop", "tide pools", "lonely stone"], "lonely stone": ["beach"], "fish shop": ["beach"], "tide pools": ["beach"], "forest": ["secret woods", "ranch", "wizard's tower", "farm", "town square"], "secret woods": ["forest"], "ranch": ["forest"], "wizard's tower": ["forest", "witch's hut"], "mountain": ["carpenter", "railroad", "backwoods", "mines", "quarry", "adventurer's guild", "town square"], "carpenter": ["mountain"], "railroad": ["mountain", "witch's hut", "spa"], "spa": ["railroad"], "mines": ["mountain"], "quarry": ["mountain"], "adventurer's guild": ["mountain"], "desert": ["oasis", "skull cavern", "bus stop"], "oasis": ["desert", "casino"], "casino": ["oasis"], "skull cavern": ["desert"], "mutant bug lair": ["sewers"], "witch's hut": ["railroad", "wizard's hut"]}

forageables = {'wild horseradish': '<:Wild_Horseradish:749493001532997784> `Wild Horseradish`', 'daffodil': '<:Daffodil:749493000719302667> `Daffodil`', 'leek': '<:Leek:749493001012904006> `Leek`', 'dandelion': '<:Dandelion:749493000761245696> `Dandelion`', 'spring onion': '<:Spring_Onion:749493001604300850> `Spring Onion`', 'salmonberry': '<:Salmonberry:749493001318957066> `Salmonberry`', 'morel': '<:Morel:749493001142796378> `Morel`', 'common mushroom': '<:Common_Mushroom:749493000509325343> `Common Mushroom`'}

forageables2 = ['wild horseradish', 'daffodil', 'leek', 'dandelion', 'spring onion', 'salmonberry', 'morel', 'common mushroom']

lockedlocations = ["tide pools", "secret woods", "sewers", "quarry", "desert", "casino", "skull cavern", "mutant bug lair", "witch's hut"]

sellprices = json.load(open('sellprices.txt', 'r'))

#each message
@client.event
async def on_message(message):
    #do not respond to ourselves
    if message.author == client.user:
        return

    #do not respond to another bot
    if message.author.bot:
        return

    content = message.content.lower()

    writer = message.author.id

    #checking if users are in the database, and adding them if not
    coins = json.load(open('money.txt', 'r'))

    if str(writer) not in coins:
        coins[str(writer)] = '0'
        json.dump(coins, open('money.txt', 'w'))

    fish = json.load(open('fish.txt', 'r'))

    if str(writer) not in fish:
        add_member(str(writer))

    forage = json.load(open('forage.txt', 'r'))

    if str(writer) not in forage:
        add_forage_member(str(writer))

    location = json.load(open('location.txt', 'r'))

    if str(writer) not in location:
        add_location_member(str(writer))

    location = json.load(open('tools.txt', 'r'))

    if str(writer) not in location:
        add_tool_member(str(writer))

    location = json.load(open('unlocked.txt', 'r'))

    if str(writer) not in location:
        add_unlocked_member(str(writer))

    await client.process_commands(message)

@client.command(pass_context=True)
async def avatar(ctx):
    #sending a user's avatar
    await ctx.send(ctx.message.author.avatar_url)

@client.command(pass_context=True)
async def shop(ctx):
    content = str(ctx.message.content).lower()
    writer = str(ctx.message.author.id)
    #if they said $shop rod
    if "rods" in content:
        if find_location(writer) == 'fish shop':
            embed = discord.Embed(title="Fish Shop", colour=discord.Colour(0x44a4d4), description="⠀")
            embed.set_thumbnail(url="https://stardewvalleywiki.com/mediawiki/images/thumb/2/2b/Fish_Shop.png/405px-Fish_Shop.png")
            embed.add_field(name="<:Training_Rod:759431888540008468> __Training Rod__ - 100 <:junicoin:758953277437509652>", value="Can only catch the most basic of fish, but a great starting rod!", inline = False)
            embed.add_field(name="<:Bamboo_Pole:759431888498065438> __Bamboo Pole__ - 500 <:junicoin:758953277437509652>", value="Made from supple bamboo, this rod allows you to catch rare fish!", inline = False)
            embed.add_field(name="<:Fiberglass_Rod:759431888002613310> __Fiberglass Rod__ - 2000 <:junicoin:758953277437509652>", value="Made with flexible fiberglass, this rod allows you to catch epic fish!", inline = False)
            embed.add_field(name="<:Iridium_Rod:759431888430956574> __Iridium Rod__ -  7500 <:junicoin:758953277437509652>", value="Crafted from iridium, this rod allows you to catch legendary fish!", inline = False)
        else:
            await ctx.send("You can't browse rods without being in the fish shop -_-")
    elif "upgrades" in content:
        if find_location(writer) == 'blacksmith':
            embed = discord.Embed(title="Blacksmith - Tool Upgrades", colour=discord.Colour(0xf1ae1d), description="Upgrade your tools to make them stronger! While your tools are being upgraded, you can't use them.\n\nStart an upgrade with `$upgrade <tool>`")

            embed.set_thumbnail(url="https://media.discordapp.net/attachments/650613336047878144/759710679120347136/160119946999045407.png")

            embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)

            embed.set_footer(text="By ||Art3mis||#0001, Cinnamon「シナモン」 #2020 and Unacorn#2250", icon_url="https://cdn.discordapp.com/emojis/759019733722071070.gif?v=1")

            if find_tool("pickaxe", writer) == "basic":
                pickaxeheader = "<:Copper_Pickaxe:759706578864701470> __Copper Pickaxe__"
                pickaxebody = "<:Copper_Bar:759706578789203978>"
            elif find_tool("pickaxe", writer) == "copper":
                pickaxeheader = "<:Steel_Pickaxe:759706579158827028>__Steel Pickaxe__"
                pickaxebody = "<:Iron_Bar:759706578969690122>"
            else:
                pickaxeheader = "<:Gold_Pickaxe:759706578906644500> __Gold Pickaxe__"
                pickaxebody = "<:Gold_Bar:759706578831802399>"
            if find_tool("axe", writer) == "basic":
                axeheader = "<:Copper_Axe:759712103765377046> __Copper Axe__"
                axebody = "<:Copper_Bar:759706578789203978>"
            elif find_tool("axe", writer) == "copper":
                axeheader = "<:Steel_Axe:759712104076410891> __Steel Axe__"
                axebody = "<:Iron_Bar:759706578969690122>"
            else:
                axeheader = "<:Gold_Axe:759712103656587285> 5__Gold Axe__"
                axebody = "<:Gold_Bar:759706578831802399>"
            embed.add_field(name=pickaxeheader, value=f"Upgrade your Pickaxe to make it stronger! \n\nRequires **5×**{pickaxebody} and **2000**<:junicoin:758953277437509652>\n<:Time_Icon:759708232720580639> Takes **1 hour**.\n ")

            embed.add_field(name=axeheader, value=f"Upgrade your Axe to make it stronger! \n\nRequires **5×**{axebody} and **2000**<:junicoin:758953277437509652>\n<:Time_Icon:759708232720580639> Takes 1 hour.")
        else:
            await ctx.send("You can't browse upgrades without being in the blacksmith -_-")
    #if they just said $shop
    else:
        embed=discord.Embed(title="Shop", description="Please include a category that you would like to buy from.")
        embed.add_field(name="$shop Rods",value="Choose various different rods to buy!", inline=False)
        embed.add_field(name="$shop Crops",value="Choose various different crops to buy!", inline=False)
        embed.add_field(name="$shop Upgrades",value="Choose various different crops to buy!", inline=False)
    embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)

    embed.set_footer(text="By ||Art3mis||#0001, Cinnamon「シナモン」 #2020 and Unacorn#2250", icon_url="https://cdn.discordapp.com/emojis/759019733722071070.gif?v=1")
    await ctx.send(embed=embed)


@client.command(pass_context = True)
async def buy(ctx):
    content = str(ctx.message.content).lower()
    writer = str(ctx.message.author.id)
    #if they said $buy bamboo pole and they have no rod (so you cannot buy a bamboo pole when you already have one)
    if 'bamboo pole' in content:
        if find_location(writer) == 'fish shop':
            if find_fish("rod", writer).lower() == 'training rod':
                #checking if they have enough money
                balance = int(find_money(writer))
                payment = int(500)
                if balance >= payment:
                    #exchange the money for the bamboo pole
                    change_rod("bamboo pole", writer)
                    remove_money(payment, writer)
                    await ctx.send("wow u can now fish hororahy")
                else:
                    await ctx.send("You don't have enough coins for that.")
            else:
                await ctx.send("You don't have the required items for that.")
        else:
            await ctx.send("You can't buy rods without being in the fish shop -_-")
    elif 'training rod' in content:
        if find_location(writer) == 'fish shop':
            if find_fish("rod", writer).lower() == 'no rod':
                #checking if they have enough money
                balance = int(find_money(writer))
                payment = int(100)
                if balance >= payment:
                    #exchange the money for the bamboo pole
                    change_rod("training rod", writer)
                    remove_money(payment, writer)
                    await ctx.send("wow u can kinda fish afodshifsdajfl")
                else:
                    await ctx.send("You don't have enough coins for that.")
            else:
                await ctx.send("You don't have the required items for that.")
        else:
            await ctx.send("You can't buy rods without being in the fish shop -_-")
    elif 'fibreglass rod' in content:
        if find_location(writer) == 'fish shop':
            if find_fish("rod", writer).lower() == 'bamboo pole':
                #checking if they have enough money
                balance = int(find_money(writer))
                payment = int(2000)
                if balance >= payment:
                    #exchange the money for the bamboo pole
                    change_rod("fibreglass rod", writer)
                    remove_money(payment, writer)
                    await ctx.send("wow u can very much fish hfiaosdjfa")
                else:
                    await ctx.send("You don't have enough coins for that.")
            else:
                await ctx.send("You don't have the required items for that.")
        else:
            await ctx.send("You can't buy rods without being in the fish shop -_-")
    elif 'iridium rod' in content:
        if find_location(writer) == 'fish shop':
            if find_fish("rod", writer).lower() == 'fibreglass rod':
                #checking if they have enough money
                balance = int(find_money(writer))
                payment = int(7500)
                if balance >= payment:
                    #exchange the money for the bamboo pole
                    change_rod("iridium rod", writer)
                    remove_money(payment, writer)
                    await ctx.send("omgomg iridium so rich .o.")
                else:
                    await ctx.send("You don't have enough coins for that.")
            else:
                await ctx.send("You don't have the required items for that.")
        else:
            await ctx.send("You can't buy rods without being in the fish shop -_-")

@client.command(pass_context=True)
async def sell(ctx):
    content = str(ctx.message.content.lower())
    writer = str(ctx.message.author.id)
    solditem = content[6:]
    if solditem in sellprices:
        money = sellprices[solditem]
        fish = json.load(open('fish.txt', 'r'))
        forage = json.load(open('forage.txt', 'r'))
        if solditem in fish[writer]:
            if find_fish(solditem, writer) == 0:
                await ctx.send("You trying to scam me, selling something you don't own?")
            else:
                remove_fish(solditem, 1, writer)
                add_money(money, writer)
                money = str(money)
                if solditem[0] == 'a' or solditem[0] == 'e' or solditem[0] == 'i' or solditem[0] == 'o' or solditem[0] == 'u':
                    await ctx.send(f"You successfully sold an {solditem} for {money} coins!")
                else:
                    await ctx.send(f"You successfully sold a {solditem} for {money} coins!")
        elif solditem in forage[writer]:
            if find_forageable(solditem, writer) == 0:
                await ctx.send("You trying to scam me, selling something you don't own?")
            else:
                remove_forageable(solditem, 1, writer)
                add_money(money, writer)
                money = str(money)
                if solditem[0] == 'a' or solditem[0] == 'e' or solditem[0] == 'i' or solditem[0] == 'o' or solditem[0] == 'u':
                    await ctx.send(f"You successfully sold an {solditem} for {money} coins!")
                else:
                    await ctx.send(f"You successfully sold a {solditem} for {money} coins!")
    else:
        await ctx.send("What the fuk are you trying to sell-")

@client.command(pass_context=True)
async def help(ctx):
    #just an embed lol
    embed=discord.Embed(title="Help", description="This embed contains the link to the support server and a list of the commands.")
    embed.set_author(name=ctx.author, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="__Support Server__", value="Go to https://tinyurl.com/help-server for the help server, where you can submit your questions directly to the devs.", inline = True)
    embed.add_field(name="__Command List__", value="Go to https://tinyurl.com/eco-list for the command list.", inline = True)
    embed.set_footer(text='By: ||Art3mis||#0001 and Cinnamon「シナモン」 #2020')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title="Invite Junibot!", colour=discord.Colour(0xc482f6), url="https://discord.com/api/oauth2/authorize?client_id=726644591411068951&permissions=384064&scope=bot", description="Click [here](https://discord.com/api/oauth2/authorize?client_id=726644591411068951&permissions=384064&scope=bot) to add **Junibot** to your own server!\n\nThanks for playing Junibot <3")
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/758953277437509652.png?v=1")

    embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)

    embed.set_footer(text="By ||Art3mis||#0001, Cinnamon「シナモン」 #2020 and Unacorn#2250", icon_url="https://cdn.discordapp.com/emojis/759019733722071070.gif?v=1")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def bal(ctx):
    writer = str(ctx.message.author.id)
    embed = discord.Embed(title= "Your Balance", description="", color=0xefd7fc)
    embed.set_author(name=ctx.author, icon_url=ctx.message.author.avatar_url)
    #finding the money to display in embed
    oof = find_money(writer)
    embed.add_field(name="Junicoins", value=str(oof), inline=False)
    #because ur poor
    embed.set_footer(text='hahahaha poor')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def inventory(ctx):
    writer = str(ctx.message.author.id)
    content = str(ctx.message.content).lower()
    #if they said $inv fish
    if "fish" in content:
        data = json.load(open("fish.txt", "r"))
        embed=discord.Embed(title="Fish you own", description="hjafkldsfodjflsadfj")
        #if they said $inv fish 2
        if "2" in content:
            #to start the page at the correct item, as to not have one item be on two pages of the inventory
            pagetwo = False
            for fish in data[writer]:
                if fish == 'tiger trout':
                    pagetwo = True
                if pagetwo == True:
                    embed.add_field(name=str(fish).title(), value=str(find_fish(fish, writer)), inline = True)
            embed.set_footer(text='Page 2/3')
        elif "3" in content:
            #copypasted shit
            pagethree = False
            for fish in data[writer]:
                if fish == 'mutant carp':
                    pagethree = True
                if pagethree == True:
                    embed.add_field(name=str(fish).title(), value=str(find_fish(fish, writer)), inline = True)
            embed.set_footer(text='Page 3/3')
        else:
            pageone = False
            for fish in data[writer]:
                if fish == 'carp':
                    pageone = True
                if pageone == True:
                    embed.add_field(name=str(fish).title(), value=str(find_fish(fish, writer)), inline = True)
            embed.set_footer(text='Page 1/3')
        await ctx.send(embed=embed)
    elif "forage" in content:
        embed=discord.Embed(title="Forageables you own", description="owehfwoiafafjdlas")
        data = json.load(open("forage.txt", "r"))
        if "2" in content:
            pagetwo = False
            for forageable in data[writer]:
                if forageable == 'sea urchin':
                    pagetwo = True
                if pagetwo == True:
                    embed.add_field(name=str(forageable).title(), value=str(find_forageable(forageable, writer)), inline = True)
            embed.set_footer(text='Page 2/2')
        else:
            pageone = False
            for forageable in data[writer]:
                if forageable == 'wild horseradish':
                    pageone = True
                if pageone == True:
                    embed.add_field(name=str(forageable).title(), value=str(find_forageable(forageable, writer)), inline = True)
            embed.set_footer(text='Page 1/2')
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def inv(ctx):
    await inventory.invoke(ctx)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    writer = str(ctx.message.author.id)
    hmm = random.choice(giveornot)
    if hmm == 'yes':
        num = random.randint(100, 500)
        add_money(num, writer)
        end = ' has donated '+str(num)+' coins to you!'
    else:
        end = random.choice(nophrases)
    rng = random.randint(1, 1000)
    if rng <= 600:
        person = random.choice(commonpeople)
    elif rng <= 850:
        person = random.choice(uncommonpeople)
    elif rng <= 950:
        person = random.choice(kindararepeople)
    elif rng <= 995:
        person = random.choice(rarepeople)
    else:
        person = random.choice(veryrarepeople)
    msg = '**'+person+'**'+end
    await ctx.send(msg)

@client.command(pass_context=True)
#@commands.cooldown(1, 30, commands.BucketType.user)
async def fish(ctx):
    writer = str(ctx.message.author.id)
    if find_fish("rod", writer) == "no rod":
        await ctx.send("You need a rod to fish, you bald man >:(.")

    else:
        if find_location(writer) == 'mountain':
            commonfishlist = commonfishlake
            rarefishlist = rarefishlake
            epicfishlist = []
            legfishlist = legfishlake
            if find_fish("rod", writer) == "training rod":
                commonchance = 100
                rarechance = 0
                epicchance = 0
            elif find_fish("rod", writer) == "bamboo pole":
                commonchance = 73
                rarechance = 100
                epicchance = 0
            elif find_fish("rod", writer) == "fibreglass rod":
                commonchance = 69
                rarechance = 100
                epicchance = 0
            elif find_fish("rod", writer) == "iridium rod":
                commonchance = 67
                rarechance = 98
                epicchance = 0
        elif find_location(writer) == 'town square' or find_location(writer) == 'forest':
            commonfishlist = commonfishriver
            rarefishlist = rarefishriver
            epicfishlist = epicfishriver
            legfishlist = []
            if find_fish("rod", writer) == "training rod":
                commonchance = 100
                rarechance = 0
                epicchance = 0
            elif find_fish("rod", writer) == "bamboo pole":
                commonchance = 70
                rarechance = 100
                epicchance = 0
            elif find_fish("rod", writer) == "fibreglass rod":
                commonchance = 66
                rarechance = 91
                epicchance = 100
            elif find_fish("rod", writer) == "iridium rod":
                commonchance = 65
                rarechance = 90
                epicchance = 100
        elif find_location(writer) == 'beach' or find_location(writer) == 'tide pools':
            commonfishlist = commonfishocean
            rarefishlist = rarefishocean
            epicfishlist = epicfishocean
            legfishlist = []
            if find_fish("rod", writer) == "training rod":
                commonchance = 100
                rarechance = 0
                epicchance = 0
            elif find_fish("rod", writer) == "bamboo pole":
                commonchance = 70
                rarechance = 100
                epicchance = 0
            elif find_fish("rod", writer) == "fibreglass rod":
                commonchance = 66
                rarechance = 91
                epicchance = 100
            elif find_fish("rod", writer) == "iridium rod":
                commonchance = 65
                rarechance = 90
                epicchance = 100
        elif find_location(writer) == 'sewer':
            commonfishlist = commonfishsewer
            rarefishlist = []
            epicfishlist = []
            legfishlist = legfishsewer
            if find_fish("rod", writer) == "training rod":
                commonchance = 100
                rarechance = 0
                epicchance = 0
            elif find_fish("rod", writer) == "bamboo pole":
                commonchance = 100
                rarechance = 0
                epicchance = 0
            elif find_fish("rod", writer) == "fibreglass rod":
                commonchance = 100
                rarechance = 0
                epicchance = 0
            elif find_fish("rod", writer) == "iridium rod":
                commonchance = 97
                rarechance = 0
                epicchance = 100
        else:
            commonchance = 0
            rarechance = 0
            epicchance = 0
            legfishlist = []
            await ctx.send("your location does not have fish ;c")

    if find_fish("rod", writer) != "no rod":
        rng = random.randint(1,100)
        if rng <= commonchance:
            fishtype = random.choice(commonfishlist)
            fish = commonfish[fishtype]

        elif rng <= rarechance:

            fishtype = random.choice(rarefishlist)
            fish = rarefish[fishtype]

        elif rng <= epicchance:

            fishtype = random.choice(epicfishlist)
            fish = epicfish[fishtype]

        else:

            fishtype = random.choice(legfishlist)
            fish = legfish[fishtype]

        add_fish(fishtype, 1, writer)

        await ctx.send(f"You reeled in a {fish}!")

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def forage(ctx):
    writer = str(ctx.message.author.id)
    place = str(find_location(writer))
    rng = random.randint(1,100)
    if place == "town square" or place == "mountain" or place == "backwoods" or place == "bus stop":
        if rng <= 20:
            item = 'wild horseradish'
        elif rng <= 35:
            item = 'daffodil'
        elif rng <= 50:
            item = 'leek'
        elif rng <= 65:
            item = 'dandelion'
        elif rng <= 75:
            item = 'salmonberry'
        elif rng <= 80:
            item = 'fibre'
        else:
            item = 'nothing'
    elif place == 'forest':
        if rng <=15:
            item = 'wild horseradish'
        elif rng <= 30:
            item = 'dandelion'
        elif rng <= 50:
            item = 'spring onion'
        elif rng <= 65:
            item = 'salmonberry'
        elif rng <= 85:
            item = 'fibre'
        else:
            item = 'nothing'
    elif place == 'secret woods':
        if rng <= 25:
            item = 'wild horseradish'
        elif rng <= 45:
            item = 'salmonberry'
        elif rng <= 60:
            item = 'fibre'
        elif rng <= 65:
            item = 'morel'
        elif rng <= 80:
            item = 'common mushroom'
        else:
            item = 'nothing'
    elif place == 'beach':
        if rng <= 28:
            item = 'clam'
        elif rng <= 41:
            item = 'cockle'
        elif rng <= 59:
            item = 'mussel'
        elif rng <= 77:
            item = 'oyster'
        else:
            item = 'nothing'
    elif place == 'tide pools':
        if rng <= 20:
            item = 'clam'
        elif rng <= 25:
            item = 'cockle'
        elif rng <= 35:
            item = 'mussel'
        elif rng <= 45:
            item = 'oyster'
        elif rng <= 70:
            item = 'coral'
        elif rng <= 80:
            item = 'sea urchin'
        elif rng <= 85:
            item = 'seaweed'
        else:
            item = 'nothing'
    else:
        item = 'bald place'
    foraged = False
    if item == 'seaweed':
        add_fish('seaweed', 1, writer)
        itemstring = commonfish['seaweed']
        foraged = True
    elif item != 'nothing' and item != 'bald place':
        itemstring = forageables[item]
        add_forageable(item, 1, writer)
    if foraged == True:
        msg = f"You have foraged a {itemstring}!"
    else:
        msg = "You haven't foraged anything.... ;;"

    await ctx.send(msg)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def scavenge(ctx):
    writer = str(ctx.message.author.id)
    place = random.choice(allplaces)
    if place == 'coinplaces':
        place = random.choice(coinplaces)
        num = random.randint(100, 500)
        add_money(num, writer)
        if place == "Xel'Naga":
            end = 'Wow you got vision and '+str(num)+' coins.'
        elif place == "Warp Prism":
            end = 'You went into the Warp Prism and a zealot donated '+str(num)+' coins to you.'
        elif place == "Bunker":
            end = 'You went into the Bunker and a marine donated '+str(num)+' coins to you.'
        elif place == "Overlord":
            end = "You went into the Overlord's ventral sacs and a zergling donated "+str(num)+' coins to you.'
    elif place == 'nocoinplaces':
        place = random.choice(nocoinplaces)
        if place == "Medivac":
            end = 'You got smashed by an ultralisk.'
        elif place == "Planetary Fortress":
            fine = random.randint(10, 100)
            if find_money(writer) < fine:
                end = "The Planetary Fortress blasted you to pieces. You spent "+str(fine)+" coins conscripting an SCV to repair you, but you didn't have enough money and had to surrender."
                bbb = find_money(writer)
                remove_money(bbb, writer)
            else:
                remove_money(fine, writer)
                end = "The Planetary Fortress blasted you to pieces. You spent "+str(fine)+" coins conscripting an SCV to repair you."
        elif place == "Photon Cannon":
            end = 'You got blasted by the photon cannon.'
        elif place == "Spine Crawler":
            end = 'You got squashed by the spine crawler.'
        elif place == "Mineral Fields":
            end = 'You go mining, but then you realise you are in SCII instead of SDV. However, you cannot escape and an oracle flies by. It activates its pulsar beam...'
    base = '**Area scavenged: **`'+place+'`.'
    msg = base + ' ' + end
    await ctx.send(msg)

@client.command(pass_context=True)
async def travel(ctx):
    content = str(ctx.message.content)
    writer = str(ctx.message.author.id)
    place = str(content[8:].lower())
    playerplace = find_location(writer)
    if place in locations:
        if place in lockedlocations:
            if find_location_lock(place, writer) == False:
                await ctx.send("You cannot travel there right now.")
            else:
                if place in locationmap[playerplace]:
                    change_location(place, writer)
                    place = place.title()
                    await ctx.send(f"You have successfully travelled to the **{place}**!")
                else:
                    #bfs go here afisjdafodaso
                    #jokes i steal a friend's
                    await ctx.send("what bfs")
        else:
            if place in locationmap[playerplace]:
                change_location(place, writer)
                place = place.title()
                await ctx.send(f"You have successfully travelled to the **{place}**!")
            else:
                #bfs go here afisjdafodaso
                #jokes i steal a friend's
                await ctx.send("what bfs")
    else:
        await ctx.send("That is not a valid location.")

@client.command(pass_context=True)
async def location(ctx):
    writer = str(ctx.message.author.id)
    place = find_location(writer)
    adjacent = locationmap[place]
    adjacent = ", ".join(adjacent)
    place = place.title()
    embed = discord.Embed(title="Map", colour=discord.Colour(0x61cf23), description="")



    embed.set_image(url="https://media.discordapp.net/attachments/679118327410589716/759985881162973254/unknown.png")

    embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)

    embed.set_footer(text="By ||Art3mis||#0001, Cinnamon「シナモン」#2020 and Unacorn#2250", icon_url="https://cdn.discordapp.com/emojis/759019733722071070.gif?v=1")



    embed.add_field(name="Current Location", value=f"{place}\n\nYou can travel to **{adjacent}**.\n\nTravel with `$travel <location>`. You can only travel to adjacent locations.")


    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def map(ctx):
    await location.invoke(ctx)

@client.command(pass_context=True)
async def gamble(ctx):
    content = str(ctx.message.content)
    writer = str(ctx.message.author.id)
    running = content.split()
    if len(running) == 1:
        await ctx.send("Include an amount to gamble >.<")
    else:
        aye = str(ctx.message.author)
        if running[1] == 'all' or running[1] == 'max':
            betamount = find_money(writer)
        else:
            betamount = int(running[1])
        if betamount > find_money(writer):
            await ctx.send('u r too broke to gambel that amount >:(')
        else:
            cinnaroll = random.randint(1,11)
            yourroll = random.randint(1,11)
            if cinnaroll == yourroll:
                embed = discord.Embed(title=aye+"'s gambling game", description="gambling bad", color=0xf7d4ab)
                embed.add_field(name="Outcome", value="Tie", inline=True)
                embed.add_field(name="Winnings", value="0", inline=True)
                embed.add_field(name="Losses", value="0", inline=True)
                embed.add_field(name="Bot's Roll", value=str(cinnaroll), inline=True)
                embed.add_field(name="Your Roll", value=str(yourroll), inline=True)
            elif cinnaroll > yourroll:
                embed = discord.Embed(title=aye+"'s gambling game", description="gambling bad", color=0xf57f87)
                remove_money(betamount, writer)
                embed.add_field(name="Outcome", value="Loss", inline=True)
                embed.add_field(name="Winnings", value="0", inline=True)
                embed.add_field(name="Losses", value=str(betamount), inline=True)
                embed.add_field(name="Bot's Roll", value=str(cinnaroll), inline=True)
                embed.add_field(name="Your Roll", value=str(yourroll), inline=True)
            elif cinnaroll < yourroll:
                embed = discord.Embed(title=aye+"'s gambling game", description="gambling bad", color=0xb1f5b0)
                add_money(betamount, writer)
                embed.add_field(name="Outcome", value="Win", inline=True)
                embed.add_field(name="Winnings", value=str(betamount), inline=True)
                embed.add_field(name="Losses", value="0", inline=True)
                embed.add_field(name="Bot's Roll", value=str(cinnaroll), inline=True)
                embed.add_field(name="Your Roll", value=str(yourroll), inline=True)
            await ctx.send(embed=embed)

@client.command(pass_context=True)
async def bet(ctx):
    await gamble.invoke(ctx)




@client.command(pass_context=True)
async def abathur(ctx):
    msg = "abathur from starcraft 2 is hot"
    await ctx.send(msg)

@client.command(pass_context=True)
async def toxic3mis(ctx):
    msg = 'omgomgomg art3mis is being toxic again'
    await ctx.send(msg)

@client.command(pass_context=True)
async def kill(ctx):
    content = str(ctx.message.content)
    if 'art3mis' in content.lower():
        msg = 'art3mis is now dead, sir wilmer'
    elif 'myself' in content.lower():
        msg = "nooo don't die <3"
    elif '@everyone' in content.lower() or '@here' in content.lower() or '<@' in content.lower():
        msg = 'stop being a bald man and trying to ping'
    else:
        person = content[6:]
        msg = f'ok i go kill {person} bai'
    await ctx.send(msg)

#this is the beginning of art3mis' easter egg tangent

@client.command(pass_context=True)
async def Art3mis(ctx):
    msg = 'When I look at him, I see everything I want to be in this world, hes smart, handsome, funny, kind, nice, empathetic, humble, and all around, a very gentle soul.'
    await ctx.send(msg)

@client.command(pass_context=True)
async def lol(ctx):
    msg = 'yuck, why plays league, play stardew valley instead :D (or not if ur broke lol)'
    await ctx.send(msg)

@client.command(pass_context=True)
async def league(ctx):
    await lol.invoke(ctx)

@client.command(pass_context=True)
async def essay(ctx):
    msg = "how did you find this command? anyhow, this is basically a link to my zelda essay, dming me feedback would be appreciated, anyhow, here's the link ||https://tinyurl.com/zelda-essay|| -Art3mis"
    await ctx.send(msg)

@client.command(pass_context=True)
async def raid(ctx):
    msg = 'Starting Raid..... ||sike, you thought this would actually be a raid||'
    await ctx.send(msg)

@client.command(pass_context=True)
async def easteregg(ctx):
    msg = '**EASTER EGG TIME**, wow, you found this, to complete the next step of this hunt, go to this link, ||https://docs.google.com/document/d/1z7lmZEYHYuRSMHZL___cVqEaWMaDF5sx-T9zBGeEXMg/edit?usp=sharing||'
    await ctx.send(msg)

#and this is the end of it

@client.event
async def on_ready():
    print('onlineeeeE')
    await client.change_presence(activity=discord.Game(name='$help | v0.5.1'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Slow down <.<", description=f"This command can be used again in **{error.retry_after:.2f}**s.", color=0xdcf0b1)
        await ctx.send(embed=embed)

tokenfile = open("token.txt")
token = str(tokenfile.readline())
client.run(token)
