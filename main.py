import discord.ext.commands
import discord
import discord.ext.commands.view
import guides

token = open("token").read()

intents = discord.Intents()
intents.dm_messages = True
intents.message_content = True
intents.guild_messages = True
intents.all()

bot = discord.ext.commands.Bot(command_prefix="?",intents=intents)

@bot.event
async def on_ready():
    game = discord.CustomActivity("Helping people in ICSCS")
    cmds = await bot.tree.sync()
    await bot.change_presence(activity=game)
    print(len(cmds),"Commands synced !")

class GuideSelectionView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Introduction Guides")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides are to introduce you to ICSCS and helping to maintain the reactor!

**Select one the the catagories below to select your guide!**""",title="Introduction Guides")
        await interaction.response.edit_message(view=guides.InterductionGuides(),embed=embed)
    
    @discord.ui.button(label="Gameplay Guides")
    async def b2(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides are to introduce you to the gameplay mechanics of ICSCS

**Select one the the catagories below to select your guide!**""",title="Gameplay Guides")
        await interaction.response.edit_message(view=guides.GameplayGuides(),embed=embed)
    
    @discord.ui.button(label="Other Guides")
    async def b3(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides extra you dont really need them but here they are!

**Select one the the catagories below to select your guide!**""",title="Other Guides")
        await interaction.response.edit_message(view=guides.OtherGuides(),embed=embed)

@bot.tree.command(name="guide",description="Opens a guide from ICSCS")
async def guide(interaction: discord.Interaction):
    embed = discord.Embed(color=discord.Color.purple(),description=f"""Hi {interaction.user.mention}! I am guidley!
I have ported my guides from ICSCS to discord so you can still use the guides even when you are not in the game!

**Select one the the catagories below to select your guide!**""",title="Guides")
    
    view = GuideSelectionView()
    
    await interaction.response.send_message(embed=embed,view=view)

bot.run(token=token)