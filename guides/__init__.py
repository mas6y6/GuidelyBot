import discord

class InterductionGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="More about sublevels")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Traversing through places")
    async def b2(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Starting the reactor")
    async def b3(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Maintaining the reactor")
    async def b4(self, interaction: discord.Interaction, button: discord.Button):
        pass

class GameplayGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Exploring the facility")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Hunger & Energy")
    async def b2(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Working as an employee")
    async def b3(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Working in maintenance")
    async def b4(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Working as a security")
    async def b5(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
    @discord.ui.button(label="Working as a researcher")
    async def b6(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
class OtherGuides(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label="Events")
    async def b1(self, interaction: discord.Interaction, button: discord.Button):
        pass
    
class GuideStartMenu(discord.ui.View):
    def __init__(self,guideclass,guidename="Guide",description="Guide Description"):
        self.guidename="Guide"
        self.description=description
        super().__init__()
    
    @discord.ui.button(label="Start")
    async def b1(self,interaction: discord.Interaction, button: discord.Button):
        