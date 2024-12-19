import traceback
import discord
from .interductionguides.more_about_sublevels import *
from .interductionguides.gameplayguides import *
from .interductionguides.otherguides import *

class GuideSelectionView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Introduction Guides")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides are to introduce you to ICSCS and helping to maintain the reactor!

**Select one the the guides below to select your guide!**""",title="Introduction Guides")
        await interaction.response.edit_message(view=InterductionGuides(),embed=embed)
    
    @discord.ui.button(label="Gameplay Guides")
    async def b2(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides are to introduce you to the gameplay mechanics of ICSCS

**Select one the the guides below to select your guide!**""",title="Gameplay Guides")
        await interaction.response.edit_message(view=GameplayGuides(),embed=embed)
    
    @discord.ui.button(label="Other Guides")
    async def b3(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides extra you dont really need them but here they are!

**Select one the the guides below to select your guide!**""",title="Other Guides")
        await interaction.response.edit_message(view=OtherGuides(),embed=embed)

class InterductionGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="More about sublevels")
    async def b1(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = GuideStartMenu(None)
        embed = discord.Embed(title="More about sublevels",description="""This guide will show you the amount of sublevels in ICSCS and what they are used for!
**Press the buttons below to either start your guide or choose a different one**
""")
    
    @discord.ui.button(label="Traversing through places")
    async def b2(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Starting the reactor")
    async def b3(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Maintaining the reactor")
    async def b4(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

class GameplayGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Exploring the facility")
    async def b1(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Hunger & Energy")
    async def b2(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Working as an employee")
    async def b3(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Working in maintenance")
    async def b4(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Working as a security")
    async def b5(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
    @discord.ui.button(label="Working as a researcher")
    async def b6(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides extra you dont really need them but here they are!

**Select the buttons below to start or cancel**""",title="Working as a researcher")
    
class OtherGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Events")
    async def b1(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides extra you dont really need them but here they are!

**Select the buttons below to start or cancel**""",title="Other Guides")
        await interaction.response.edit_message(embed=embed,view=GuideStartMenu(None))
    
class GuideStartMenu(discord.ui.View):
    def __init__(self,guideclass):
        self.guideclass=guideclass
        super().__init__()
    
    @discord.ui.button(label="Start")
    async def b1(self,interaction: discord.Interaction, button: discord.ui.Button):
        try:
            self.guideclass.startguide(interaction)
        except:
            embed=discord.Embed(color=discord.Color.purple(),description="""Well something went wrong while starting the guide.

Please let @mas6y6 know if this is on accident.

*I am very early in development so not every guide is implemented yet*""",title="Oops!")
            await interaction.response.edit_message(embed=embed,ephemeral=True)
            traceback.print_exc()
        else:
            pass
        
    @discord.ui.button(label="Close")
    async def b2(self,interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.purple(),description="**Select one the the catagories below to select your guide!**",title="Guides")
        await interaction.response.edit_message(embed=embed,view=GuideSelectionView())