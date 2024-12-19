import discord

class GuideSelectionView(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Introduction Guides")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides are to introduce you to ICSCS and helping to maintain the reactor!

**Select one the the catagories below to select your guide!**""",title="Introduction Guides")
        await interaction.response.edit_message(view=InterductionGuides(),embed=embed)
    
    @discord.ui.button(label="Gameplay Guides")
    async def b2(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides are to introduce you to the gameplay mechanics of ICSCS

**Select one the the catagories below to select your guide!**""",title="Gameplay Guides")
        await interaction.response.edit_message(view=GameplayGuides(),embed=embed)
    
    @discord.ui.button(label="Other Guides")
    async def b3(self, interaction: discord.Interaction, button: discord.Button):
        embed = discord.Embed(color=discord.Color.purple(),description=f"""These guides extra you dont really need them but here they are!

**Select one the the catagories below to select your guide!**""",title="Other Guides")
        await interaction.response.edit_message(view=OtherGuides(),embed=embed)

class InterductionGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="More about sublevels")
    async def b1(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
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
        pass
    
class OtherGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Events")
    async def b1(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass
    
class GuideStartMenu(discord.ui.View):
    def __init__(self,guideclass,guidename="Guide",description="Guide Description"):
        self.guidename="Guide"
        self.description=description
        self.guideclass = guideclass
        super().__init__()
    
    @discord.ui.button(label="Start")
    async def b1(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.guideclass.startguide(interaction)
        
    @discord.ui.button(label="Close")
    async def b2(self,interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.purple(),description="**Select one the the catagories below to select your guide!**",title="Guides")
        await interaction.response.edit_message(embed=embed,view=GuideSelectionView())