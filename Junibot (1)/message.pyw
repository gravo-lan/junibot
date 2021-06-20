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
from sword import find_sword
from sword import change_sword
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

#setting prefix and other shit
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

locations = ["farm", "farmhouse", "backwoods", "bus stop", "town square", "sewers", "blacksmith", "community center", "clinic", "jojamart", "museum", "supermarket", "saloon", "beach", "fish shop", "tide pools", "forest", "secret woods", "ranch", "wizard's tower", "mountain", "carpenter", "railroad", "spa", "mines", "quarry", "adventurer's guild", "desert", "oasis", "casino", "skull cavern", "mutant bug lair", "witch's hut"]

commonforageables = {'wild horseradish': '<:Wild_Horseradish:749493001532997784> `Wild Horseradish`', 'daffodil': '<:Daffodil:749493000719302667> `Daffodil`', 'leek': '<:Leek:749493001012904006> `Leek`', 'dandelion': '<:Dandelion:749493000761245696> `Dandelion`', 'spring onion': '<:Spring_Onion:749493001604300850> `Spring Onion`', 'salmonberry': '<:Salmonberry:749493001318957066> `Salmonberry`'}
rareforageables = {'morel': '<:Morel:749493001142796378> `Morel`', 'common mushroom': '<:Common_Mushroom:749493000509325343> `Common Mushroom`'}

commonforageables2 = ['wild horseradish', 'daffodil', 'leek', 'dandelion', 'spring onion', 'salmonberry']
rareforageables2 = ['morel', 'common mushroom']

sellprices = json.load(open('sellprices.txt', 'r'))

#we keep this for uh archival purposes
def user_add_xp(user_id, coins):
    with open('money.txt', 'r') as fp:
        money = json.load(fp)
        cooldown = json.load(open("cooldown.txt", "r"))

        time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - cooldown[user_id]
        if time_diff >= 120:
            try:
                moneyy = int(money[user_id])
                moneyy += coins
                money[user_id] = str(moneyy)
                cooldown[user_id] = (datetime.datetime.utcnow() - epoch).total_seconds()
                json.dump(money, open('money.txt', 'w'))
                json.dump(cooldown, open('cooldown.txt', 'w'))
            except KeyError:
                with open('cooldown.txt', 'r') as fp:
                    cooldown = json.load(fp)
                    cooldown[user_id] = 0
                    json.dump(cooldown, open('cooldown.txt', 'w'))
        else:
            with open('cooldown.txt', 'r') as fp:
                cooldown = json.load(fp)
                cooldown[user_id] = 120 - (datetime.datetime.utcnow() - epoch).total_seconds()
                if cooldown[user_id] < 0:
                    cooldown[user_id] = 0
                with open('cooldown.txt', 'w') as fp:
                    json.dump(cooldown, fp)

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

    sword = json.load(open('sword.txt', 'r'))

    if str(writer) not in sword:
        sword[str(writer)] = 'no sword'
        json.dump(sword, open('sword.txt', 'w'))

    cooldown = json.load(open('cooldown.txt', 'r'))

    if str(writer) not in cooldown:
        cooldown[str(writer)] = 0
        json.dump(cooldown, open('cooldown.txt', 'w'))

    fish = json.load(open('fish.txt', 'r'))

    if str(writer) not in fish:
        add_member(str(writer))

    forage = json.load(open('forage.txt', 'r'))

    if str(writer) not in forage:
        add_forage_member(str(writer))

    location = json.load(open('location.txt', 'r'))

    if str(writer) not in location:
        add_location_member(str(writer))

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
            embed=discord.Embed(title="Fishing Rod Shop", description="wee woo")
            embed.add_field(name="bamboo pole",value="bad rod // 500 coins", inline=False)
            embed.add_field(name="training rod",value="bald rod // 100 coins", inline=False)
            embed.add_field(name="fibreglass rod",value="not very bald rod // 2000 coins", inline=False)
            embed.add_field(name="iridium rod",value="haired rod // 7500 coins", inline=False)
        else:
            await ctx.send("You can't browse rods without being in the fish shop -_-")
    #if they just said $shop
    else:
        embed=discord.Embed(title="Shop", description="Please include a category that you would like to buy from.")
        embed.add_field(name="$shop Rods",value="Choose various different rods to buy!", inline=True)
        embed.add_field(name="$shop CropsC",value="hoose various different crops to buy!", inline=True)
    embed.set_footer(text='By: ||Art3mis||#0001 and Cinnamon「シナモン」 #2020')
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
async def bal(ctx):
    writer = str(ctx.message.author.id)
    embed = discord.Embed(title= "Your Balance", description="", color=0xefd7fc)
    embed.set_author(name=ctx.author, icon_url=ctx.message.author.avatar_url)
    #finding the money to display in embed
    oof = find_money(writer)
    embed.add_field(name="Coins", value=str(oof), inline=False)
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
@commands.cooldown(1, 30, commands.BucketType.user)
async def fish(ctx):
    writer = str(ctx.message.author.id)
    if find_fish("rod", writer) == "no rod":
        await ctx.send("You need a rod to fish, you bald man >:(.")

    else:
        if find_location(writer) == 'mountain':
            commonfishlist = commonfishlake
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

    if find_fish("rod", writer) != "no rod":
        rng = random.randint(1,100)
        if rng <= commonchance:
            fishtype = random.choice(commonfish2)
            fish = commonfish[fishtype]

        elif rng <= rarechance:

            fishtype = random.choice(rarefish2)
            fish = rarefish[fishtype]

        elif rng <= epicchance:

            fishtype = random.choice(epicfish2)
            fish = epicfish[fishtype]

        else:

            fishtype = random.choice(legfish2)
            fish = legfish[fishtype]
            
        add_fish(fishtype, 1, writer)

        await ctx.send(f"You reeled in a {fish}!")

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def forage(ctx):
    writer = str(ctx.message.author.id)
    rng = random.randint(1,1000)
    if rng <= 750:

        item = random.choice(commonforageables2)
        itemstring = commonforageables[item]

    else:

        item = random.choice(rareforageables2)
        itemstring = rareforageables[item]

    add_forageable(item, 1, writer)

    await ctx.send(f"You have foraged a {itemstring}!")

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
            end = 'You went mining, but then you realised you were in SCII instead of SDV. However, you cannot escape. Then, an oracle flies by and activates its pulsar beam...'
    base = '**Area scavenged: **`'+place+'`.'
    msg = base + ' ' + end
    await ctx.send(msg)

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
    await client.change_presence(activity=discord.Game(name='$help | v0.4.2'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Slow down <.<", description=f"This command can be used again in **{error.retry_after:.2f}**s.", color=0xdcf0b1)
        await ctx.send(embed=embed)

tokenfile = open("token.txt")
token = str(tokenfile.readline())
client.run(token)
